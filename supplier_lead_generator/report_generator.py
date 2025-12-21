#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
客户报告生成器 - 生成专业的客户开发报告
"""

import json
from datetime import datetime
from typing import List, Dict
import pandas as pd


class ReportGenerator:
    """生成客户开发报告"""

    def __init__(self):
        self.report_date = datetime.now().strftime('%Y-%m-%d')

    def generate_markdown_report(self, leads: List[Dict]) -> str:
        """
        生成Markdown格式的客户报告
        """
        report = f"""# 客户线索开发报告

生成日期: {self.report_date}
总线索数: {len(leads)}

---

## 📊 执行摘要

本报告包含来自5个目标国家的潜在客户线索:
- 🇵🇪 秘鲁 (Peru)
- 🇧🇴 玻利维亚 (Bolivia)
- 🇪🇬 埃及 (Egypt)
- 🇰🇿 哈萨克斯坦 (Kazakhstan)
- 🇦🇪 阿联酋 (UAE)

每个国家5个中小型企业客户，共25个线索。

---

## 📋 按国家分类的客户列表

"""

        # 按国家分组
        countries = {}
        for lead in leads:
            country = lead.get('country', 'Unknown')
            if country not in countries:
                countries[country] = []
            countries[country].append(lead)

        # 为每个国家生成详细报告
        for country, country_leads in countries.items():
            country_cn = country_leads[0].get('country_cn', country)
            report += f"\n### {country_cn} ({country})\n\n"

            for i, lead in enumerate(country_leads, 1):
                report += f"#### 线索 #{i}: {lead.get('company_name', 'N/A')}\n\n"

                # 基本信息
                report += "**基本信息:**\n"
                report += f"- 线索ID: `{lead.get('lead_id', 'N/A')}`\n"
                report += f"- 公司名称: {lead.get('company_name', 'N/A')}\n"
                report += f"- 行业: {lead.get('industry', 'N/A')}\n"
                report += f"- 公司规模: {lead.get('company_size', 'N/A')}\n\n"

                # 联系信息
                contact = lead.get('contact_info', {})
                report += "**联系方式:**\n"
                report += f"- 📧 邮箱: {contact.get('email', 'N/A')}\n"
                report += f"- 📱 电话: {contact.get('phone', 'N/A')}\n"
                report += f"- 💬 WhatsApp: {contact.get('whatsapp', 'N/A')}\n"
                report += f"- 🌐 网站: {contact.get('website', 'N/A')}\n"
                report += f"- 💼 LinkedIn: {contact.get('linkedin_company', 'N/A')}\n\n"

                # 联系人
                if 'contact_person' in contact:
                    person = contact['contact_person']
                    report += "**关键联系人:**\n"
                    report += f"- 姓名: {person.get('name', 'N/A')}\n"
                    report += f"- 职位: {person.get('title', 'N/A')}\n"
                    report += f"- 邮箱: {person.get('email', 'N/A')}\n"
                    report += f"- LinkedIn: {person.get('linkedin', 'N/A')}\n\n"

                # 采购状态
                sourcing = lead.get('sourcing_status', {})
                report += "**采购状态:**\n"
                report += f"- 状态: {sourcing.get('status', 'N/A')}\n"
                report += f"- 证据: {sourcing.get('evidence', 'N/A')}\n"
                report += f"- 需求产品: {sourcing.get('products_needed', 'N/A')}\n\n"

                # 数据收集指导
                if 'data_collection_guide' in lead:
                    report += "**数据收集指导:**\n"
                    guide = lead['data_collection_guide']
                    for step_key, step_data in guide.items():
                        if isinstance(step_data, dict):
                            report += f"- {step_data.get('action', '')}\n"

                    report += "\n"

                # 推荐数据源
                if 'recommended_sources' in lead:
                    report += "**推荐数据源:**\n"
                    for source in lead['recommended_sources']:
                        if isinstance(source, dict):
                            priority = source.get('priority', 'Medium')
                            name = source.get('source', 'Unknown')
                            report += f"- [{priority}] {name}\n"

                    report += "\n"

                # 背调清单
                if 'due_diligence_checklist' in lead:
                    report += "**背调清单:**\n"
                    checklist = lead['due_diligence_checklist']
                    for check_key, check_data in checklist.items():
                        if isinstance(check_data, dict):
                            task = check_data.get('task', '')
                            status = check_data.get('status', '')
                            report += f"- [ ] {task} - {status}\n"

                    report += "\n"

                # 元数据
                metadata = lead.get('metadata', {})
                report += "**线索状态:**\n"
                report += f"- 数据质量: {metadata.get('data_quality', 0)}%\n"
                report += f"- 完成状态: {metadata.get('completion_status', 'N/A')}\n"
                report += f"- 下一步: {metadata.get('next_action', 'N/A')}\n\n"

                report += "---\n\n"

        # 添加附录
        report += self._generate_appendix()

        return report

    def _generate_appendix(self) -> str:
        """生成报告附录"""
        appendix = """
## 📚 附录

### A. 数据收集方法

本报告中的客户线索使用以下合法公开来源:

1. **LinkedIn** - 公司页面和专业人士资料
2. **Google搜索** - 公开的商业信息
3. **B2B平台** - Alibaba, TradeKey, Global Sources等
4. **商会目录** - 各国商会的公开会员名录
5. **政府数据库** - 公开的公司注册信息
6. **贸易展会** - 参展商公开名单
7. **行业协会** - 公开的会员目录

### B. 背景调查指南

对每个潜在客户进行以下尽职调查:

#### 1. 公司验证
- 在当地公司注册处验证公司存在
- 确认公司法律状态和注册日期
- 检查公司董事和股东信息(如果公开)

#### 2. 在线存在验证
- 检查公司网站的真实性和活跃度
- 验证社交媒体账户
- 检查域名注册信息和年龄

#### 3. 信用检查
- 使用Dun & Bradstreet或当地信用机构
- 检查付款历史和信用评级
- 查看任何法律诉讼记录

#### 4. 贸易历史
- 在贸易数据库查询进出口记录
- 确认他们的采购模式
- 识别现有供应商

#### 5. 声誉调查
- Google新闻搜索
- 客户评价和testimonials
- 行业内声誉

### C. 联系最佳实践

#### 首次联系
- 使用专业的邮件模板
- 提及你是如何发现他们的(LinkedIn, B2B平台等)
- 简明扼要地介绍你的产品/服务
- 提供价值主张

#### WhatsApp沟通
- 仅在获得许可后使用WhatsApp
- 保持专业性
- 避免垃圾信息
- 尊重不同时区

#### 跟进策略
- 第一次联系后等待3-5个工作日
- 最多跟进3次
- 提供额外价值(案例研究、样品等)

### D. 合规性说明

**数据保护:**
- 所有数据来源于公开渠道
- 符合GDPR和各国数据保护法规
- 仅用于合法商业目的
- 尊重opt-out请求

**营销许可:**
- 仅联系有明确商业需求的公司
- 提供清晰的取消订阅选项
- 遵守CAN-SPAM和类似法规

### E. 数据源链接

#### 秘鲁 (Peru)
- SUNARP: https://www.sunarp.gob.pe
- Lima Chamber of Commerce: https://www.camaralima.org.pe

#### 玻利维亚 (Bolivia)
- FUNDEMPRESA: https://www.fundempresa.org.bo
- CAINCO: https://www.cainco.org.bo

#### 埃及 (Egypt)
- GAFI: https://www.investinegypt.gov.eg
- Federation of Egyptian Chambers: https://www.fedcoc.org.eg

#### 哈萨克斯坦 (Kazakhstan)
- E-Gov Business Registry: https://www.egov.kz
- Chamber of Commerce: https://www.chamber.kz

#### 阿联酋 (UAE)
- Dubai DED: https://www.dubaided.gov.ae
- Dubai Chamber: https://www.dubaichamber.com

---

*报告生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
*系统: 供应商客户线索开发系统 v1.0*
"""
        return appendix

    def generate_excel_report(self, leads: List[Dict], filename: str):
        """
        生成Excel格式的报告
        """
        # 扁平化数据结构以适应Excel
        flattened_leads = []

        for lead in leads:
            contact = lead.get('contact_info', {})
            person = contact.get('contact_person', {})
            sourcing = lead.get('sourcing_status', {})
            metadata = lead.get('metadata', {})

            flat_lead = {
                '线索ID': lead.get('lead_id', ''),
                '国家': lead.get('country_cn', ''),
                '公司名称': lead.get('company_name', ''),
                '行业': lead.get('industry', ''),
                '公司规模': lead.get('company_size', ''),
                '邮箱': contact.get('email', ''),
                '电话': contact.get('phone', ''),
                'WhatsApp': contact.get('whatsapp', ''),
                '网站': contact.get('website', ''),
                'LinkedIn': contact.get('linkedin_company', ''),
                '联系人姓名': person.get('name', ''),
                '联系人职位': person.get('title', ''),
                '联系人邮箱': person.get('email', ''),
                '采购状态': sourcing.get('status', ''),
                '需求产品': sourcing.get('products_needed', ''),
                '数据质量': metadata.get('data_quality', 0),
                '完成状态': metadata.get('completion_status', ''),
                '下一步行动': metadata.get('next_action', '')
            }

            flattened_leads.append(flat_lead)

        # 创建DataFrame
        df = pd.DataFrame(flattened_leads)

        # 保存到Excel
        with pd.ExcelWriter(filename, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='客户线索', index=False)

            # 按国家分组的sheet
            for country in df['国家'].unique():
                country_df = df[df['国家'] == country]
                country_df.to_excel(writer, sheet_name=country[:30], index=False)

        print(f"✅ Excel报告已生成: {filename}")


def main():
    """主函数"""
    # 读取线索数据
    try:
        with open('customer_leads_template.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            leads = data.get('leads', [])
    except FileNotFoundError:
        print("❌ 未找到 customer_leads_template.json")
        print("请先运行 data_collector.py 生成线索数据")
        return

    # 生成报告
    generator = ReportGenerator()

    # 生成Markdown报告
    markdown_report = generator.generate_markdown_report(leads)
    with open('客户开发报告.md', 'w', encoding='utf-8') as f:
        f.write(markdown_report)
    print("✅ Markdown报告已生成: 客户开发报告.md")

    # 生成Excel报告
    try:
        generator.generate_excel_report(leads, '客户开发报告.xlsx')
    except Exception as e:
        print(f"⚠️  Excel报告生成失败: {e}")
        print("提示: 需要安装 openpyxl: pip install openpyxl")

    print(f"\n📊 报告生成完成!")
    print(f"   - Markdown: 客户开发报告.md")
    print(f"   - Excel: 客户开发报告.xlsx (如果成功)")


if __name__ == "__main__":
    main()
