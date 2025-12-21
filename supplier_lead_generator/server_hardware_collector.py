#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
服务器硬件专用客户线索收集器
Product: HP/Dell/Lenovo Server Hardware (Memory, CPU, HDD, SSD, RAID Card, Motherboard, PSU)
"""

import json
from datetime import datetime
from typing import List, Dict

class ServerHardwareLeadCollector:
    """服务器硬件客户开发专用工具"""

    def __init__(self):
        self.product_categories = {
            'Server Memory': ['DDR3', 'DDR4', 'DDR5', 'ECC RAM'],
            'Server Processor': ['Intel Xeon', 'AMD EPYC', 'CPU'],
            'Server Hard Drive': ['2.5in SFF HDD', '3.5in LFF HDD', 'Enterprise SSD', 'NVMe SSD'],
            'Server Card': ['RAID Card', 'HBA Card', 'Network Card', 'Storage Controller'],
            'Server Motherboard': ['Dual Socket Motherboard', 'Server Board'],
            'Server Power Supply': ['Redundant PSU', 'Hot-swap PSU']
        }

        self.brands = ['HP', 'HPE', 'Dell', 'Lenovo', 'IBM']

        self.target_customers = {
            'Data Centers': '数据中心',
            'IT Service Providers': 'IT服务提供商',
            'Cloud Providers': '云服务商',
            'System Integrators': '系统集成商',
            'IT Resellers': 'IT经销商',
            'Enterprise IT Departments': '企业IT部门',
            'Hosting Companies': '托管服务商',
            'Telecom Companies': '电信公司'
        }

    def generate_search_queries(self, country: str) -> List[str]:
        """
        生成针对服务器硬件的搜索查询
        """
        queries = [
            # 通用服务器硬件买家
            f'{country} server hardware importers',
            f'{country} data center equipment buyers',
            f'{country} IT hardware distributors',
            f'{country} server parts suppliers looking to buy',

            # 品牌特定
            f'{country} HP server parts buyers',
            f'{country} Dell server hardware importers',
            f'{country} Lenovo server components distributors',

            # 产品特定
            f'{country} server memory DDR4 DDR5 buyers',
            f'{country} server hard drive SSD importers',
            f'{country} RAID card HBA card buyers',
            f'{country} server power supply distributors',

            # 客户类型
            f'{country} data center companies contact',
            f'{country} cloud service providers',
            f'{country} IT system integrators',
            f'{country} server resellers distributors',

            # B2B平台查询
            f'{country} server hardware buyer inquiry',
            f'{country} looking for server parts supplier',

            # LinkedIn查询
            f'site:linkedin.com "{country}" "data center" OR "IT infrastructure"',
            f'site:linkedin.com "{country}" "server" "procurement manager"',
        ]

        return queries

    def get_target_industries(self, country: str) -> Dict:
        """
        获取目标行业信息
        """
        industries = {
            'Peru': ['Mining IT', 'Banking', 'Telecommunications', 'Government IT', 'Education'],
            'Bolivia': ['Government IT', 'Telecom', 'Banking', 'Mining IT', 'Energy'],
            'Egypt': ['Telecom', 'Banking', 'Government IT', 'Oil & Gas IT', 'Education'],
            'Kazakhstan': ['Oil & Gas IT', 'Banking', 'Telecom', 'Government IT', 'Mining IT'],
            'UAE': ['Data Centers', 'Cloud Providers', 'Banking', 'Government IT', 'Telecom', 'Retail IT']
        }

        return industries.get(country, [])

    def create_lead_template(self, country: str, lead_number: int) -> Dict:
        """
        创建服务器硬件客户线索模板
        """
        country_info = {
            'Peru': {'name_cn': '秘鲁', 'phone': '+51', 'domain': '.pe'},
            'Bolivia': {'name_cn': '玻利维亚', 'phone': '+591', 'domain': '.bo'},
            'Egypt': {'name_cn': '埃及', 'phone': '+20', 'domain': '.eg'},
            'Kazakhstan': {'name_cn': '哈萨克斯坦', 'phone': '+7', 'domain': '.kz'},
            'UAE': {'name_cn': '阿联酋', 'phone': '+971', 'domain': '.ae'}
        }

        info = country_info[country]
        industries = self.get_target_industries(country)

        lead = {
            'lead_id': f'{country}_SERVER_{lead_number:03d}',
            'country': country,
            'country_cn': info['name_cn'],
            'collection_date': datetime.now().isoformat(),

            # 基本信息
            'company_info': {
                'company_name': '[待搜索]',
                'company_name_local': '[当地语言名称]',
                'business_type': f'[建议: {", ".join(list(self.target_customers.values())[:3])}]',
                'target_industry': f'[建议: {", ".join(industries[:3])}]',
                'company_size': 'SME (11-500人)',
                'website': f'[通常以 {info["domain"]} 结尾]',
                'address': '[完整地址]',
                'year_established': '[年份]'
            },

            # 联系信息
            'contact_info': {
                'primary_email': '[如: info@company.com, sales@company.com]',
                'secondary_email': '[备用邮箱]',
                'phone': f'[格式: {info["phone"]} XXXXXXXXX]',
                'whatsapp': f'[通常与电话相同: {info["phone"]} XXXXXXXXX]',
                'linkedin_company': '[LinkedIn公司页面]',
                'contact_person': {
                    'name': '[采购经理/IT经理姓名]',
                    'title': '[如: IT Procurement Manager, Data Center Manager]',
                    'email': '[个人邮箱]',
                    'phone': '[直拨电话]',
                    'whatsapp': '[个人WhatsApp]',
                    'linkedin': '[个人LinkedIn URL]'
                }
            },

            # 采购需求
            'procurement_needs': {
                'looking_for_supplier': True,
                'has_stable_supplier': '[需确认: 如果有稳定供应商则跳过]',
                'products_interested': {
                    'Server Memory': '[是否需要: DDR3/DDR4/DDR5]',
                    'Server CPU': '[是否需要: Intel Xeon / AMD EPYC]',
                    'Server HDD/SSD': '[是否需要: 2.5"/3.5" HDD, Enterprise SSD]',
                    'RAID/HBA Card': '[是否需要]',
                    'Server Motherboard': '[是否需要]',
                    'Server PSU': '[是否需要]'
                },
                'preferred_brands': '[HP/Dell/Lenovo - 询问偏好]',
                'purchase_volume': '[月度/年度采购量]',
                'budget_range': '[预算范围]',
                'urgency': '[紧急/常规]'
            },

            # 采购证据
            'sourcing_evidence': {
                'evidence_type': '[从哪里发现的]',
                'evidence_details': '[具体证据]',
                'sources': [
                    '[ ] B2B平台买家询盘',
                    '[ ] LinkedIn招聘IT采购职位',
                    '[ ] 公司网站采购页面',
                    '[ ] 贸易展会参展',
                    '[ ] 新闻报道扩张/新项目',
                    '[ ] 政府采购公告'
                ]
            },

            # 数据收集指南
            'collection_guide': {
                'step1_search': {
                    'action': '在搜索引擎查找',
                    'queries': self.generate_search_queries(country)[:5],
                    'what_to_find': '公司名称、网站、基本联系方式'
                },
                'step2_linkedin': {
                    'action': 'LinkedIn深度搜索',
                    'company_search': f'"{country}" AND ("data center" OR "IT infrastructure" OR "server")',
                    'people_search': 'IT Manager, Procurement Manager, CTO',
                    'what_to_collect': '公司页面、关键人员、联系方式'
                },
                'step3_website': {
                    'action': '访问公司网站',
                    'what_to_check': [
                        '联系页面 (Contact Us)',
                        '关于我们 (About)',
                        '服务/产品页面',
                        '采购/供应商页面'
                    ],
                    'what_to_collect': '官方邮箱、电话、业务范围'
                },
                'step4_b2b': {
                    'action': '检查B2B平台',
                    'platforms': [
                        f'Alibaba: https://www.alibaba.com/trade/search?SearchText={country}+server+hardware',
                        'TradeKey: 搜索买家询盘',
                        'Global Sources: 查看采购需求'
                    ],
                    'what_to_find': '买家询盘、采购需求、联系方式'
                },
                'step5_verify': {
                    'action': '验证联系方式',
                    'tools': [
                        'Hunter.io - 邮箱验证',
                        'WhatsApp - 验证号码是否有WhatsApp',
                        'LinkedIn - 验证人员真实性'
                    ]
                }
            },

            # 背调清单
            'due_diligence': {
                'company_verification': {
                    'task': '公司注册验证',
                    'status': '待完成',
                    'how': f'在{country}官方注册处查询',
                    'findings': '[记录发现]'
                },
                'business_legitimacy': {
                    'task': '业务合法性检查',
                    'status': '待完成',
                    'checks': [
                        '[ ] 网站存在且活跃',
                        '[ ] LinkedIn公司页面存在',
                        '[ ] Google可以搜到公司',
                        '[ ] 有办公地址',
                        '[ ] 域名年龄 > 1年'
                    ]
                },
                'financial_check': {
                    'task': '财务状况检查',
                    'status': '待完成',
                    'indicators': [
                        '[ ] 公司规模和员工数',
                        '[ ] 办公地点档次',
                        '[ ] 网站专业度',
                        '[ ] 是否有其他供应商',
                        '[ ] 信用报告 (如可获得)'
                    ]
                },
                'it_capability': {
                    'task': 'IT采购能力评估',
                    'status': '待完成',
                    'indicators': [
                        '[ ] 是否有IT部门',
                        '[ ] 是否有数据中心',
                        '[ ] 是否经营IT业务',
                        '[ ] 是否有服务器相关业务',
                        '[ ] 技术人员规模'
                    ]
                },
                'reputation_check': {
                    'task': '声誉调查',
                    'status': '待完成',
                    'sources': [
                        '[ ] Google新闻搜索',
                        '[ ] 社交媒体检查',
                        '[ ] 客户评价',
                        '[ ] 行业论坛',
                        '[ ] Better Business Bureau等'
                    ]
                },
                'risk_assessment': {
                    'overall_risk': '[低/中/高]',
                    'red_flags': [],
                    'green_flags': [],
                    'recommendation': '[推荐/谨慎/不推荐]',
                    'notes': '[其他备注]'
                }
            },

            # 优先级评分
            'priority_score': {
                'total_score': 0,
                'factors': {
                    'company_size': 0,  # 0-20分
                    'industry_fit': 0,  # 0-20分
                    'sourcing_urgency': 0,  # 0-20分
                    'contact_quality': 0,  # 0-20分
                    'business_legitimacy': 0  # 0-20分
                },
                'priority_level': '[高/中/低]'
            },

            # 元数据
            'metadata': {
                'created_date': datetime.now().isoformat(),
                'last_updated': datetime.now().isoformat(),
                'data_quality': '0%',
                'completion_status': '待收集',
                'assigned_to': '[销售人员]',
                'follow_up_date': '[跟进日期]',
                'status': 'New Lead',
                'notes': []
            }
        }

        return lead

    def generate_all_leads(self) -> Dict:
        """
        生成所有国家的线索
        """
        countries = ['Peru', 'Bolivia', 'Egypt', 'Kazakhstan', 'UAE']
        all_leads = []

        for country in countries:
            print(f"\n{'='*70}")
            print(f"📍 生成 {country} 服务器硬件客户线索模板")
            print(f"{'='*70}")

            for i in range(1, 6):  # 每国5个
                lead = self.create_lead_template(country, i)
                all_leads.append(lead)
                print(f"  ✓ 线索 {i}/5: {lead['lead_id']}")

        result = {
            'product_info': {
                'product_type': 'Server Hardware Components',
                'categories': self.product_categories,
                'brands': self.brands,
                'condition': 'Brand New',
                'target_customers': self.target_customers
            },
            'leads': all_leads,
            'total_leads': len(all_leads),
            'countries_covered': countries,
            'generated_date': datetime.now().isoformat(),
            'next_steps': [
                '1. 使用提供的搜索查询在Google/LinkedIn搜索',
                '2. 检查B2B平台的服务器硬件买家询盘',
                '3. 收集完整的联系信息 (邮箱、电话、WhatsApp)',
                '4. 验证公司是否正在寻找供应商',
                '5. 执行背景调查',
                '6. 评估优先级',
                '7. 开始联系'
            ]
        }

        return result


def main():
    """主函数"""
    collector = ServerHardwareLeadCollector()
    result = collector.generate_all_leads()

    # 保存结果
    output_file = 'server_hardware_leads.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"\n{'='*70}")
    print(f"✅ 已生成 {result['total_leads']} 个服务器硬件客户线索模板")
    print(f"📁 保存到: {output_file}")
    print(f"{'='*70}")
    print(f"\n📌 产品类型:")
    for category, items in result['product_info']['categories'].items():
        print(f"  • {category}: {', '.join(items)}")
    print(f"\n🎯 目标客户类型:")
    for cust_type, cust_cn in result['product_info']['target_customers'].items():
        print(f"  • {cust_type} ({cust_cn})")

    return result


if __name__ == "__main__":
    main()
