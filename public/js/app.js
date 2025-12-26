// API Base URL
const API_BASE = '';

// State
let currentLesson = null;
let allLessons = [];
let settings = {};
let progress = {};
let categories = {};

// Initialize app
document.addEventListener('DOMContentLoaded', async () => {
  await Promise.all([
    loadSettings(),
    loadProgress(),
    loadCategories(),
    loadAllLessons()
  ]);

  setupTabNavigation();
  setupSSE();
  requestNotificationPermission();
  renderDashboard();
  renderAllTabs();
});

// API Functions
async function apiGet(endpoint) {
  const response = await fetch(`${API_BASE}/api${endpoint}`);
  return response.json();
}

async function apiPost(endpoint, data) {
  const response = await fetch(`${API_BASE}/api${endpoint}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });
  return response.json();
}

// Load data
async function loadSettings() {
  settings = await apiGet('/settings');
}

async function loadProgress() {
  progress = await apiGet('/progress');
  updateStats();
}

async function loadCategories() {
  categories = await apiGet('/categories');
}

async function loadAllLessons() {
  allLessons = await apiGet('/lessons');
}

// Update stats display
function updateStats() {
  document.getElementById('totalLessons').textContent = progress.totalLessons || 0;
  document.getElementById('completedLessons').textContent = progress.completedCount || 0;

  const percent = progress.totalLessons > 0
    ? Math.round((progress.completedCount / progress.totalLessons) * 100)
    : 0;
  document.getElementById('progressPercent').textContent = `${percent}%`;

  // Calculate next push time
  updateNextPushTime();
}

function updateNextPushTime() {
  const now = new Date();
  const currentMinutes = now.getHours() * 60 + now.getMinutes();

  let nextTime = null;
  let minDiff = Infinity;

  settings.pushTimes?.forEach(time => {
    const [h, m] = time.split(':').map(Number);
    const timeMinutes = h * 60 + m;
    let diff = timeMinutes - currentMinutes;
    if (diff <= 0) diff += 24 * 60; // next day

    if (diff < minDiff) {
      minDiff = diff;
      nextTime = time;
    }
  });

  document.getElementById('nextPushTime').textContent = nextTime || '--:--';
}

// Tab Navigation
function setupTabNavigation() {
  const tabBtns = document.querySelectorAll('.tab-btn');
  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const tabId = btn.dataset.tab;
      switchTab(tabId);
    });
  });
}

function switchTab(tabId) {
  // Update buttons
  document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.tab === tabId);
  });

  // Update panes
  document.querySelectorAll('.tab-pane').forEach(pane => {
    pane.classList.toggle('active', pane.id === tabId);
  });
}

// Render Dashboard
function renderDashboard() {
  loadNextLesson();
  renderCategoryProgress();
}

async function loadNextLesson() {
  const lesson = await apiGet('/next-lesson');
  if (lesson) {
    currentLesson = lesson;
    renderCurrentLesson(lesson);
  }
}

async function loadRandomLesson() {
  const lesson = await apiGet('/random-lesson');
  if (lesson) {
    currentLesson = lesson;
    renderCurrentLesson(lesson);
  }
}

function renderCurrentLesson(lesson) {
  const container = document.getElementById('currentLessonContent');
  if (!lesson) {
    container.innerHTML = '<p class="loading">暂无学习内容</p>';
    return;
  }

  let html = `
    <div class="lesson-category">${lesson.categoryName} - ${lesson.subcategory}</div>
    <h3 class="lesson-title">${lesson.title}</h3>
  `;

  if (lesson.content) {
    html += `<p class="lesson-content">${lesson.content}</p>`;
  }

  if (lesson.key_points) {
    html += `
      <div class="lesson-key-points">
        <h4>关键要点</h4>
        <ul>
          ${lesson.key_points.map(point => `<li>${point}</li>`).join('')}
        </ul>
      </div>
    `;
  }

  if (lesson.english_terms) {
    html += `
      <div class="english-terms">
        <h4>英文术语</h4>
        <div class="term-list">
          ${Object.entries(lesson.english_terms).map(([cn, en]) =>
    `<div class="term-item"><span class="term-cn">${cn}:</span> <span class="term-en">${en}</span></div>`
  ).join('')}
        </div>
      </div>
    `;
  }

  container.innerHTML = html;
}

function renderCategoryProgress() {
  const container = document.getElementById('categoryProgress');
  const categoryData = [
    { name: '服务器产品', key: 'server_products' },
    { name: '外贸练习', key: 'foreign_trade' },
    { name: '阿里国际站', key: 'alibaba_operation' }
  ];

  let html = '';
  categoryData.forEach(cat => {
    const catLessons = allLessons.filter(l => l.category === cat.key);
    const completed = catLessons.filter(l => progress.completedLessons?.includes(l.id)).length;
    const total = catLessons.length;
    const percent = total > 0 ? Math.round((completed / total) * 100) : 0;

    html += `
      <div class="progress-item">
        <div class="progress-label">
          <span>${cat.name}</span>
          <span>${completed}/${total}</span>
        </div>
        <div class="progress-bar">
          <div class="progress-fill" style="width: ${percent}%"></div>
        </div>
      </div>
    `;
  });

  container.innerHTML = html;
}

// Render all tabs
function renderAllTabs() {
  renderServerProducts();
  renderForeignTrade();
  renderAlibabaOps();
  renderAllLessons();
}

function renderServerProducts() {
  const lessons = allLessons.filter(l => l.category === 'server_products');
  renderLessonsGrid('serverProductsLessons', lessons);
}

function renderForeignTrade() {
  const lessons = allLessons.filter(l => l.category === 'foreign_trade');
  renderLessonsGrid('foreignTradeLessons', lessons);
}

function renderAlibabaOps() {
  const lessons = allLessons.filter(l => l.category === 'alibaba_operation');
  renderLessonsGrid('alibabaOpsLessons', lessons);
}

function renderAllLessons() {
  const container = document.getElementById('allLessonsList');
  let html = '';

  allLessons.forEach(lesson => {
    const isCompleted = progress.completedLessons?.includes(lesson.id);
    html += `
      <div class="lesson-list-item" onclick="openLesson('${lesson.id}')">
        <div class="lesson-list-info">
          <span class="lesson-list-category">${lesson.subcategory}</span>
          <span class="lesson-list-title">${lesson.title}</span>
        </div>
        <span>${isCompleted ? '✅' : ''}</span>
      </div>
    `;
  });

  container.innerHTML = html;
}

function renderLessonsGrid(containerId, lessons) {
  const container = document.getElementById(containerId);

  // Group by subcategory
  const groups = {};
  lessons.forEach(lesson => {
    const key = lesson.subcategory;
    if (!groups[key]) groups[key] = [];
    groups[key].push(lesson);
  });

  let html = '';
  Object.entries(groups).forEach(([subcategory, groupLessons]) => {
    html += `<h3 style="grid-column: 1/-1; margin: 1rem 0 0.5rem; color: var(--text-secondary);">${subcategory}</h3>`;
    groupLessons.forEach(lesson => {
      const isCompleted = progress.completedLessons?.includes(lesson.id);
      html += `
        <div class="lesson-card ${isCompleted ? 'completed' : ''}" onclick="openLesson('${lesson.id}')">
          <div class="lesson-card-header">
            <span class="lesson-card-category">${lesson.subcategoryEn || ''}</span>
            <span class="lesson-card-status">${isCompleted ? '✅' : '📖'}</span>
          </div>
          <h4 class="lesson-card-title">${lesson.title}</h4>
          <p class="lesson-card-desc">${lesson.content || ''}</p>
        </div>
      `;
    });
  });

  container.innerHTML = html;
}

// Search
function searchLessons() {
  const query = document.getElementById('searchInput').value.toLowerCase();
  const container = document.getElementById('allLessonsList');

  const filtered = allLessons.filter(lesson =>
    lesson.title.toLowerCase().includes(query) ||
    (lesson.content && lesson.content.toLowerCase().includes(query)) ||
    lesson.subcategory.toLowerCase().includes(query)
  );

  let html = '';
  filtered.forEach(lesson => {
    const isCompleted = progress.completedLessons?.includes(lesson.id);
    html += `
      <div class="lesson-list-item" onclick="openLesson('${lesson.id}')">
        <div class="lesson-list-info">
          <span class="lesson-list-category">${lesson.subcategory}</span>
          <span class="lesson-list-title">${lesson.title}</span>
        </div>
        <span>${isCompleted ? '✅' : ''}</span>
      </div>
    `;
  });

  container.innerHTML = html || '<p class="loading">未找到匹配的课程</p>';
}

// Lesson Modal
async function openLesson(lessonId) {
  const lesson = await apiGet(`/lesson/${lessonId}`);
  if (!lesson) return;

  currentLesson = lesson;
  document.getElementById('modalTitle').textContent = lesson.title;

  let html = `
    <div class="lesson-category">${lesson.categoryName} - ${lesson.subcategory}</div>
  `;

  if (lesson.title_en) {
    html += `<p style="color: var(--text-secondary); margin-bottom: 1rem;">${lesson.title_en}</p>`;
  }

  if (lesson.content) {
    html += `<p class="lesson-content">${lesson.content}</p>`;
  }

  if (lesson.key_points) {
    html += `
      <div class="lesson-key-points">
        <h4>关键要点</h4>
        <ul>
          ${lesson.key_points.map(point => `<li>${point}</li>`).join('')}
        </ul>
      </div>
    `;
  }

  if (lesson.english_terms) {
    html += `
      <div class="english-terms">
        <h4>英文术语 / English Terms</h4>
        <div class="term-list">
          ${Object.entries(lesson.english_terms).map(([cn, en]) =>
    `<div class="term-item"><span class="term-cn">${cn}:</span> <span class="term-en">${en}</span></div>`
  ).join('')}
        </div>
      </div>
    `;
  }

  // Practice scenarios
  if (lesson.practice_scenario) {
    html += `
      <div class="practice-box">
        <h4>练习场景</h4>
        <pre>${lesson.practice_scenario.scenario}</pre>
        ${lesson.practice_scenario.best_answer ? `<p><strong>参考答案:</strong> ${lesson.practice_scenario.best_answer}</p>` : ''}
      </div>
    `;
  }

  // Templates
  if (lesson.template) {
    html += `
      <div class="template-box">
        <h4>模板参考</h4>
        ${lesson.template.subject ? `<p><strong>Subject:</strong> ${lesson.template.subject}</p>` : ''}
        <pre>${lesson.template.body || ''}</pre>
      </div>
    `;
  }

  // QA pairs
  if (lesson.qa_pairs) {
    html += `<div class="lesson-key-points"><h4>常见问答</h4>`;
    lesson.qa_pairs.forEach(qa => {
      html += `
        <div style="margin-bottom: 1rem;">
          <p><strong>Q:</strong> ${qa.question}</p>
          <p><strong>中文:</strong> ${qa.answer_cn}</p>
          <p><strong>English:</strong> ${qa.answer_en}</p>
        </div>
      `;
    });
    html += `</div>`;
  }

  document.getElementById('modalBody').innerHTML = html;
  document.getElementById('lessonModal').classList.add('show');
}

function closeModal() {
  document.getElementById('lessonModal').classList.remove('show');
}

async function markComplete() {
  if (!currentLesson) return;

  await apiPost(`/lesson/${currentLesson.id}/complete`);
  progress = await apiGet('/progress');
  updateStats();
  renderCategoryProgress();
  renderAllTabs();
  closeModal();

  showToast('学习完成！', `已完成: ${currentLesson.title}`);
}

// Settings Modal
function showSettings() {
  renderPushTimes();
  updateSettingsCheckboxes();
  document.getElementById('settingsModal').classList.add('show');
}

function closeSettingsModal() {
  document.getElementById('settingsModal').classList.remove('show');
}

function renderPushTimes() {
  const container = document.getElementById('pushTimesContainer');
  let html = '<div class="time-input-group">';

  settings.pushTimes?.forEach((time, index) => {
    html += `
      <div class="time-input-wrapper">
        <input type="time" value="${time}" onchange="updatePushTime(${index}, this.value)">
        <button class="time-remove" onclick="removePushTime(${index})">&times;</button>
      </div>
    `;
  });

  html += '</div>';
  container.innerHTML = html;
}

function addPushTime() {
  if (settings.pushTimes.length >= 5) {
    alert('最多只能设置5个推送时间');
    return;
  }
  settings.pushTimes.push('12:00');
  renderPushTimes();
}

function removePushTime(index) {
  if (settings.pushTimes.length <= 1) {
    alert('至少保留一个推送时间');
    return;
  }
  settings.pushTimes.splice(index, 1);
  renderPushTimes();
}

function updatePushTime(index, value) {
  settings.pushTimes[index] = value;
}

function updateSettingsCheckboxes() {
  document.getElementById('cat_server_products').checked =
    settings.enabledCategories?.includes('server_products');
  document.getElementById('cat_foreign_trade').checked =
    settings.enabledCategories?.includes('foreign_trade');
  document.getElementById('cat_alibaba_operation').checked =
    settings.enabledCategories?.includes('alibaba_operation');
  document.getElementById('notificationEnabled').checked = settings.notificationEnabled;
  document.getElementById('soundEnabled').checked = settings.soundEnabled;
}

async function saveSettings() {
  const enabledCategories = [];
  if (document.getElementById('cat_server_products').checked) {
    enabledCategories.push('server_products');
  }
  if (document.getElementById('cat_foreign_trade').checked) {
    enabledCategories.push('foreign_trade');
  }
  if (document.getElementById('cat_alibaba_operation').checked) {
    enabledCategories.push('alibaba_operation');
  }

  settings.enabledCategories = enabledCategories;
  settings.notificationEnabled = document.getElementById('notificationEnabled').checked;
  settings.soundEnabled = document.getElementById('soundEnabled').checked;

  await apiPost('/settings', settings);
  closeSettingsModal();
  updateNextPushTime();
  showToast('设置已保存', '推送时间和类别已更新');
}

// Manual push
async function triggerPush() {
  const result = await apiPost('/push');
  if (result.lesson) {
    currentLesson = result.lesson;
    renderCurrentLesson(result.lesson);
    showToast('推送成功', result.lesson.title);
  }
}

// SSE for real-time updates
function setupSSE() {
  const eventSource = new EventSource(`${API_BASE}/api/events`);

  eventSource.onmessage = (event) => {
    const data = JSON.parse(event.data);

    if (data.type === 'lesson') {
      currentLesson = data.lesson;
      renderCurrentLesson(data.lesson);
      showBrowserNotification(data.lesson);
      showToast('新学习内容', data.lesson.title);
      loadProgress();
    }
  };

  eventSource.onerror = () => {
    console.log('SSE connection error, will retry...');
  };
}

// Browser notifications
function requestNotificationPermission() {
  if ('Notification' in window && Notification.permission === 'default') {
    Notification.requestPermission();
  }
}

function showBrowserNotification(lesson) {
  if ('Notification' in window && Notification.permission === 'granted') {
    new Notification('📚 学习时间到！', {
      body: `${lesson.categoryName} - ${lesson.title}`,
      icon: 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><text y=".9em" font-size="90">📚</text></svg>',
      tag: 'learning-notification'
    });
  }
}

// Toast notifications
function showToast(title, message) {
  document.getElementById('toastTitle').textContent = title;
  document.getElementById('toastMessage').textContent = message;
  document.getElementById('toast').classList.add('show');

  setTimeout(() => {
    hideToast();
  }, 5000);
}

function hideToast() {
  document.getElementById('toast').classList.remove('show');
}

// Expose functions to global scope
window.switchTab = switchTab;
window.loadRandomLesson = loadRandomLesson;
window.openLesson = openLesson;
window.closeModal = closeModal;
window.markComplete = markComplete;
window.showSettings = showSettings;
window.closeSettingsModal = closeSettingsModal;
window.addPushTime = addPushTime;
window.removePushTime = removePushTime;
window.updatePushTime = updatePushTime;
window.saveSettings = saveSettings;
window.triggerPush = triggerPush;
window.searchLessons = searchLessons;
window.hideToast = hideToast;
