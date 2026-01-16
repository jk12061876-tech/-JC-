# 🚀 供应商客户线索开发系统

专业的客户开发工具,帮助你从合法公开渠道收集潜在客户信息,并进行背景调查。

## 📋 功能特点

✅ **合法合规** - 仅使用公开信息源,符合GDPR和数据保护法规
✅ **多国支持** - 秘鲁、玻利维亚、埃及、哈萨克斯坦、阿联酋
✅ **系统化流程** - 从搜索到背调的完整工作流
✅ **专业报告** - 自动生成Markdown和Excel格式报告
✅ **详细指导** - 每个线索都有具体的数据收集指南

## 🎯 目标客户

- 中小型企业 (SME, 11-500人)
- 正在寻找供应商的公司
- 有采购需求的进口商/贸易公司

## 📦 安装

### 1. 克隆或下载此项目

```bash
cd supplier_lead_generator
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

## 🔧 使用方法

### 快速开始

运行完整流程:

```bash
# 1. 生成客户线索模板和收集指导
python data_collector.py

# 2. 生成专业报告
python report_generator.py
```

### 分步使用

#### 步骤1: 生成线索模板

```bash
python data_collector.py
```

这将生成 `customer_leads_template.json`,包含:
- 25个客户线索模板 (每国5个)
- 详细的数据收集指导
- 推荐的数据源列表
- 背调清单

#### 步骤2: 手动收集数据

打开 `customer_leads_template.json`,按照每个线索的指导:

1. **LinkedIn搜索** - 查找公司和关键联系人
2. **访问网站** - 收集联系方式和业务信息
3. **B2B平台** - 查看买家询盘和采购需求
4. **商会目录** - 获取会员企业信息
5. **背景调查** - 验证公司真实性和信誉

#### 步骤3: 执行背景调查

```bash
python due_diligence.py
```

对收集的客户进行尽职调查:
- 公司注册验证
- 在线存在检查
- 贸易历史查询
- 信用评级
- 声誉调查

#### 步骤4: 生成报告

```bash
python report_generator.py
```

自动生成:
- `客户开发报告.md` - Markdown格式详细报告
- `客户开发报告.xlsx` - Excel表格 (可选)

## 📊 数据来源

系统使用以下合法公开数据源:

### 官方政府数据库

| 国家 | 数据源 | 类型 |
|------|--------|------|
| 🇵🇪 秘鲁 | SUNARP | 公司注册 |
| 🇧🇴 玻利维亚 | FUNDEMPRESA | 商业登记 |
| 🇪🇬 埃及 | GAFI | 投资局 |
| 🇰🇿 哈萨克斯坦 | E-Gov | 商业注册 |
| 🇦🇪 阿联酋 | DED | 经济发展局 |

### 商业平台

- **LinkedIn** - 公司页面和专业人士资料
- **Google** - 公开商业信息搜索
- **Alibaba** - 买家询盘和目录
- **TradeKey** - B2B买家数据库
- **Global Sources** - 采购需求

### 商会和行业协会

- 各国商会公开会员名录
- 行业协会成员目录
- 贸易展会参展商名单

## 🔍 搜索策略示例

### LinkedIn搜索

```
搜索: "Peru" AND ("procurement" OR "import" OR "purchasing")
筛选:
- 位置: Peru
- 公司规模: 11-50, 51-200, 201-500
- 行业: 你的目标行业
```

### Google搜索

```
"Peru" import companies contact
"Bolivia" procurement managers email
"Egypt" trading companies directory
"Kazakhstan" chamber of commerce members
"UAE" importers directory
```

### B2B平台

```
Alibaba: https://www.alibaba.com/buyer/search?country=Peru
TradeKey: https://www.tradekey.com/buyers/peru/
```

## 📋 背调清单

对每个客户执行以下检查:

- [ ] **公司验证** - 在官方注册处查询
- [ ] **网站检查** - 域名年龄、SSL证书、内容
- [ ] **社交媒体** - LinkedIn、Facebook活跃度
- [ ] **贸易历史** - 进出口记录 (ImportGenius/Panjiva)
- [ ] **新闻搜索** - Google新闻、行业报道
- [ ] **信用检查** - D&B或当地信用机构
- [ ] **联系验证** - 邮箱格式、电话有效性

## 💡 最佳实践

### 数据收集

1. **从高质量来源开始** - LinkedIn和官方商会优先
2. **交叉验证信息** - 从多个来源确认同一信息
3. **记录数据来源** - 标注每条信息的出处
4. **定期更新** - 联系信息可能会变化

### 联系客户

1. **个性化沟通** - 提及你如何发现他们的
2. **提供价值** - 不只是推销,提供有用信息
3. **尊重隐私** - 仅使用公开的联系方式
4. **遵守法规** - CAN-SPAM, GDPR等

### 质量管理

1. **数据质量评分** - 0-100分制
2. **完成度跟踪** - 标记每个线索的完成状态
3. **优先级排序** - 高质量线索优先跟进
4. **定期清理** - 删除无效或低质量线索

## 🛡️ 合规性

### GDPR合规

- ✅ 仅收集公开信息
- ✅ 合法商业目的
- ✅ 数据主体权利
- ✅ 提供opt-out选项

### 数据保护

- 🔒 本地存储,加密保护
- 🔒 不共享给第三方
- 🔒 定期审查和清理
- 🔒 遵守各国数据保护法

## 📁 文件结构

```
supplier_lead_generator/
├── README.md                          # 本文件
├── requirements.txt                   # Python依赖
├── data_collector.py                  # 数据收集器
├── due_diligence.py                   # 背调模块
├── report_generator.py                # 报告生成器
├── web_search.py                      # 网络搜索工具
├── main.py                           # 主程序
├── customer_leads_template.json       # 生成的线索模板
├── search_strategies.json             # 搜索策略
├── 客户开发报告.md                    # Markdown报告
└── 客户开发报告.xlsx                  # Excel报告
```

## 🔧 高级功能

### 自定义搜索

编辑 `data_collector.py` 中的参数:

```python
# 修改每国线索数量
self.leads_per_country = 10  # 默认5

# 添加特定行业
industry = "Electronics"  # 指定行业
```

### 批量背调

```python
from due_diligence import DueDiligenceChecker

checker = DueDiligenceChecker()
reports = checker.batch_due_diligence(leads)
```

## ❓ 常见问题

### Q: 这是网络爬虫吗?
A: 不是。这是一个数据收集指导系统,告诉你去哪里找公开信息,但需要你手动收集。

### Q: 如何获取WhatsApp号码?
A: WhatsApp号码通常与公司电话相同。从网站、LinkedIn或B2B平台获取公司电话后,验证是否开通WhatsApp。

### Q: 如何确认客户正在找供应商?
A: 查看:
- B2B平台的买家询盘
- LinkedIn上的采购职位招聘
- 公司网站的采购页面
- 贸易展会参展记录

### Q: 数据质量如何保证?
A:
- 使用多个来源交叉验证
- 执行完整的背景调查
- 验证联系方式有效性
- 定期更新信息

## 📞 支持

遇到问题?

1. 检查 `search_strategies.json` 获取详细搜索指导
2. 参考 `customer_leads_template.json` 中的收集指南
3. 查看生成的报告中的"附录"部分

## 🚀 下一步

1. 运行 `python data_collector.py` 生成线索模板
2. 按照指导手动收集真实数据
3. 运行 `python due_diligence.py` 执行背调
4. 生成专业报告: `python report_generator.py`
5. 开始联系你的潜在客户!

## ⚖️ 免责声明

本工具仅用于合法商业目的。使用者需:
- 遵守所有适用的数据保护法律
- 仅收集和使用公开信息
- 尊重隐私权和opt-out请求
- 遵守反垃圾邮件法规

---

**版本**: 1.0
**最后更新**: 2025-12-21
**许可**: MIT
