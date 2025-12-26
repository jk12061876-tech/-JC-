const express = require('express');
const cron = require('node-cron');
const notifier = require('node-notifier');
const path = require('path');
const fs = require('fs');
const cors = require('cors');

const app = express();
const PORT = 3000;

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static('public'));

// Data file paths
const DATA_DIR = path.join(__dirname, 'data');
const SETTINGS_FILE = path.join(DATA_DIR, 'settings.json');
const PROGRESS_FILE = path.join(DATA_DIR, 'progress.json');

// Load learning content
const serverProducts = require('./data/server-products.json');
const foreignTrade = require('./data/foreign-trade.json');
const alibabaOperation = require('./data/alibaba-operation.json');

// Initialize settings
let settings = {
  pushTimes: ['09:00', '14:00', '19:00'], // 默认推送时间
  enabledCategories: ['server_products', 'foreign_trade', 'alibaba_operation'],
  notificationEnabled: true,
  browserNotification: true,
  soundEnabled: true
};

// Learning progress tracking
let progress = {
  currentLessonIndex: {},
  completedLessons: [],
  lastPushTime: null,
  totalLessons: 0,
  completedCount: 0
};

// Active cron jobs
let cronJobs = [];

// Load settings from file
function loadSettings() {
  try {
    if (fs.existsSync(SETTINGS_FILE)) {
      settings = JSON.parse(fs.readFileSync(SETTINGS_FILE, 'utf8'));
      console.log('Settings loaded successfully');
    } else {
      saveSettings();
    }
  } catch (error) {
    console.error('Error loading settings:', error);
  }
}

// Save settings to file
function saveSettings() {
  try {
    fs.writeFileSync(SETTINGS_FILE, JSON.stringify(settings, null, 2));
    console.log('Settings saved successfully');
  } catch (error) {
    console.error('Error saving settings:', error);
  }
}

// Load progress from file
function loadProgress() {
  try {
    if (fs.existsSync(PROGRESS_FILE)) {
      progress = JSON.parse(fs.readFileSync(PROGRESS_FILE, 'utf8'));
      console.log('Progress loaded successfully');
    } else {
      initializeProgress();
    }
  } catch (error) {
    console.error('Error loading progress:', error);
  }
}

// Save progress to file
function saveProgress() {
  try {
    fs.writeFileSync(PROGRESS_FILE, JSON.stringify(progress, null, 2));
  } catch (error) {
    console.error('Error saving progress:', error);
  }
}

// Initialize progress tracking
function initializeProgress() {
  const categories = ['server_products', 'foreign_trade', 'alibaba_operation'];
  categories.forEach(cat => {
    progress.currentLessonIndex[cat] = 0;
  });
  progress.totalLessons = countTotalLessons();
  saveProgress();
}

// Count total lessons
function countTotalLessons() {
  let count = 0;

  // Server products lessons
  Object.values(serverProducts.products).forEach(product => {
    if (product.lessons) {
      count += product.lessons.length;
    }
  });

  // Foreign trade lessons
  Object.values(foreignTrade.modules).forEach(module => {
    if (module.lessons) {
      count += module.lessons.length;
    }
  });

  // Alibaba operation lessons
  Object.values(alibabaOperation.modules).forEach(module => {
    if (module.lessons) {
      count += module.lessons.length;
    }
  });

  return count;
}

// Get all lessons as a flat array
function getAllLessons() {
  const lessons = [];

  // Server products
  Object.entries(serverProducts.products).forEach(([key, product]) => {
    if (product.lessons) {
      product.lessons.forEach(lesson => {
        lessons.push({
          ...lesson,
          category: 'server_products',
          categoryName: '服务器产品知识',
          subcategory: product.name,
          subcategoryEn: product.name_en
        });
      });
    }
  });

  // Foreign trade
  Object.entries(foreignTrade.modules).forEach(([key, module]) => {
    if (module.lessons) {
      module.lessons.forEach(lesson => {
        lessons.push({
          ...lesson,
          category: 'foreign_trade',
          categoryName: '外贸练习',
          subcategory: module.name,
          subcategoryEn: module.name_en
        });
      });
    }
  });

  // Alibaba operation
  Object.entries(alibabaOperation.modules).forEach(([key, module]) => {
    if (module.lessons) {
      module.lessons.forEach(lesson => {
        lessons.push({
          ...lesson,
          category: 'alibaba_operation',
          categoryName: '阿里国际站运营',
          subcategory: module.name,
          subcategoryEn: module.name_en
        });
      });
    }
  });

  return lessons;
}

// Get next lesson to push
function getNextLesson() {
  const allLessons = getAllLessons();
  const enabledLessons = allLessons.filter(lesson =>
    settings.enabledCategories.includes(lesson.category)
  );

  if (enabledLessons.length === 0) {
    return null;
  }

  // Get lessons not yet completed
  const incompleteLessons = enabledLessons.filter(lesson =>
    !progress.completedLessons.includes(lesson.id)
  );

  if (incompleteLessons.length === 0) {
    // Reset progress if all completed
    progress.completedLessons = [];
    saveProgress();
    return enabledLessons[0];
  }

  return incompleteLessons[0];
}

// Get random lesson for variety
function getRandomLesson() {
  const allLessons = getAllLessons();
  const enabledLessons = allLessons.filter(lesson =>
    settings.enabledCategories.includes(lesson.category)
  );

  if (enabledLessons.length === 0) {
    return null;
  }

  const randomIndex = Math.floor(Math.random() * enabledLessons.length);
  return enabledLessons[randomIndex];
}

// Send notification
function sendNotification(lesson) {
  if (!settings.notificationEnabled || !lesson) {
    return;
  }

  const title = `📚 学习时间到！`;
  const message = `${lesson.categoryName} - ${lesson.subcategory}\n${lesson.title}`;

  // Desktop notification
  notifier.notify({
    title: title,
    message: message,
    sound: settings.soundEnabled,
    wait: true,
    timeout: 30
  }, (err, response) => {
    if (err) {
      console.error('Notification error:', err);
    }
  });

  // Log the push
  console.log(`[${new Date().toLocaleString()}] Pushed lesson: ${lesson.title}`);

  // Update progress
  progress.lastPushTime = new Date().toISOString();
  if (!progress.completedLessons.includes(lesson.id)) {
    progress.completedLessons.push(lesson.id);
    progress.completedCount = progress.completedLessons.length;
  }
  saveProgress();

  // Emit to connected clients via SSE
  broadcastLesson(lesson);
}

// SSE clients
let sseClients = [];

// Broadcast lesson to all connected SSE clients
function broadcastLesson(lesson) {
  const data = JSON.stringify({
    type: 'lesson',
    lesson: lesson,
    timestamp: new Date().toISOString()
  });

  sseClients.forEach(client => {
    client.write(`data: ${data}\n\n`);
  });
}

// Setup cron jobs for push times
function setupCronJobs() {
  // Clear existing jobs
  cronJobs.forEach(job => job.stop());
  cronJobs = [];

  // Create new jobs for each push time
  settings.pushTimes.forEach(time => {
    const [hour, minute] = time.split(':');
    const cronExpression = `${minute} ${hour} * * *`;

    const job = cron.schedule(cronExpression, () => {
      const lesson = getNextLesson();
      sendNotification(lesson);
    }, {
      timezone: "Asia/Shanghai"
    });

    cronJobs.push(job);
    console.log(`Scheduled push at ${time}`);
  });
}

// API Routes

// Get settings
app.get('/api/settings', (req, res) => {
  res.json(settings);
});

// Update settings
app.post('/api/settings', (req, res) => {
  settings = { ...settings, ...req.body };
  saveSettings();
  setupCronJobs();
  res.json({ success: true, settings });
});

// Get progress
app.get('/api/progress', (req, res) => {
  res.json({
    ...progress,
    totalLessons: countTotalLessons()
  });
});

// Reset progress
app.post('/api/progress/reset', (req, res) => {
  progress.completedLessons = [];
  progress.completedCount = 0;
  saveProgress();
  res.json({ success: true });
});

// Get all lessons
app.get('/api/lessons', (req, res) => {
  const lessons = getAllLessons();
  res.json(lessons);
});

// Get lessons by category
app.get('/api/lessons/:category', (req, res) => {
  const { category } = req.params;
  const lessons = getAllLessons().filter(lesson => lesson.category === category);
  res.json(lessons);
});

// Get single lesson by ID
app.get('/api/lesson/:id', (req, res) => {
  const { id } = req.params;
  const lesson = getAllLessons().find(lesson => lesson.id === id);
  if (lesson) {
    res.json(lesson);
  } else {
    res.status(404).json({ error: 'Lesson not found' });
  }
});

// Get next lesson
app.get('/api/next-lesson', (req, res) => {
  const lesson = getNextLesson();
  res.json(lesson);
});

// Get random lesson
app.get('/api/random-lesson', (req, res) => {
  const lesson = getRandomLesson();
  res.json(lesson);
});

// Mark lesson as completed
app.post('/api/lesson/:id/complete', (req, res) => {
  const { id } = req.params;
  if (!progress.completedLessons.includes(id)) {
    progress.completedLessons.push(id);
    progress.completedCount = progress.completedLessons.length;
    saveProgress();
  }
  res.json({ success: true, progress });
});

// Manually trigger a push
app.post('/api/push', (req, res) => {
  const lesson = getNextLesson();
  sendNotification(lesson);
  res.json({ success: true, lesson });
});

// SSE endpoint for real-time updates
app.get('/api/events', (req, res) => {
  res.setHeader('Content-Type', 'text/event-stream');
  res.setHeader('Cache-Control', 'no-cache');
  res.setHeader('Connection', 'keep-alive');

  // Send initial connection message
  res.write(`data: ${JSON.stringify({ type: 'connected' })}\n\n`);

  // Add client to list
  sseClients.push(res);

  // Remove client on disconnect
  req.on('close', () => {
    sseClients = sseClients.filter(client => client !== res);
  });
});

// Get categories structure
app.get('/api/categories', (req, res) => {
  const categories = {
    server_products: {
      name: '服务器产品知识',
      name_en: 'Server Products',
      subcategories: Object.entries(serverProducts.products).map(([key, value]) => ({
        key,
        name: value.name,
        name_en: value.name_en,
        lessonCount: value.lessons ? value.lessons.length : 0
      }))
    },
    foreign_trade: {
      name: '外贸练习',
      name_en: 'Foreign Trade Practice',
      subcategories: Object.entries(foreignTrade.modules).map(([key, value]) => ({
        key,
        name: value.name,
        name_en: value.name_en,
        lessonCount: value.lessons ? value.lessons.length : 0
      }))
    },
    alibaba_operation: {
      name: '阿里国际站运营',
      name_en: 'Alibaba Operation',
      subcategories: Object.entries(alibabaOperation.modules).map(([key, value]) => ({
        key,
        name: value.name,
        name_en: value.name_en,
        lessonCount: value.lessons ? value.lessons.length : 0
      }))
    }
  };
  res.json(categories);
});

// Search lessons
app.get('/api/search', (req, res) => {
  const { q } = req.query;
  if (!q) {
    return res.json([]);
  }

  const query = q.toLowerCase();
  const lessons = getAllLessons().filter(lesson =>
    lesson.title.toLowerCase().includes(query) ||
    (lesson.content && lesson.content.toLowerCase().includes(query)) ||
    (lesson.title_en && lesson.title_en.toLowerCase().includes(query))
  );

  res.json(lessons);
});

// Initialize and start server
loadSettings();
loadProgress();
setupCronJobs();

app.listen(PORT, () => {
  console.log(`
╔════════════════════════════════════════════════════════╗
║     📚 学习推送系统已启动 Learning Push System         ║
╠════════════════════════════════════════════════════════╣
║  访问地址: http://localhost:${PORT}                       ║
║  推送时间: ${settings.pushTimes.join(', ')}
║  总课程数: ${countTotalLessons()} 课
╚════════════════════════════════════════════════════════╝
  `);
});

module.exports = app;
