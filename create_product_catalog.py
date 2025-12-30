# -*- coding: utf-8 -*-
"""
Product Catalog Generator
Capri Blue Premium Color Scheme
"""

from docx import Document
from docx.shared import Inches, Pt, Cm, RGBColor, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn, nsdecls
from docx.oxml import parse_xml
import os

# Capri Blue Premium Color Scheme
CAPRI_BLUE = "015697"     # Capri Blue - Primary
CREAM_PINK = "FFF2DF"     # Cream Pink - Background
WHITE = "FFFFFF"
DARK_BLUE = "013A63"      # Dark Blue - Text

def set_cell_shading(cell, color):
    """Set cell background color"""
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_cell_border(cell, color="015697", size="4"):
    """Set cell border"""
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="{size}" w:color="{color}"/>'
        f'<w:left w:val="single" w:sz="{size}" w:color="{color}"/>'
        f'<w:bottom w:val="single" w:sz="{size}" w:color="{color}"/>'
        f'<w:right w:val="single" w:sz="{size}" w:color="{color}"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(tcBorders)

def set_no_border(cell):
    """Remove cell border"""
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:top w:val="nil"/>'
        f'<w:left w:val="nil"/>'
        f'<w:bottom w:val="nil"/>'
        f'<w:right w:val="nil"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(tcBorders)

def create_cover_page(doc):
    """Create cover page with Capri Blue theme"""

    # Full page background
    bg_table = doc.add_table(rows=1, cols=1)
    bg_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    bg_cell = bg_table.cell(0, 0)
    set_cell_shading(bg_cell, CAPRI_BLUE)
    set_no_border(bg_cell)

    para = bg_cell.paragraphs[0]
    para.alignment = WD_ALIGN_PARAGRAPH.CENTER

    para.add_run("\n\n\n\n\n")

    # Company Logo
    logo_run = para.add_run("[ LOGO ]\n\n\n")
    logo_run.font.size = Pt(18)
    logo_run.font.color.rgb = RGBColor(255, 242, 223)  # Cream Pink
    logo_run.font.name = 'Arial'

    # Company Name
    company_run = para.add_run("YOUR COMPANY NAME\n")
    company_run.font.size = Pt(36)
    company_run.font.bold = True
    company_run.font.color.rgb = RGBColor(255, 255, 255)  # White
    company_run.font.name = 'Arial'

    # Decorative line
    line_run = para.add_run("━━━━━━━━━━━━━━━━━━\n\n")
    line_run.font.size = Pt(14)
    line_run.font.color.rgb = RGBColor(255, 242, 223)

    # Main Title
    title_run = para.add_run("PRODUCT CATALOG\n")
    title_run.font.size = Pt(48)
    title_run.font.bold = True
    title_run.font.color.rgb = RGBColor(255, 255, 255)
    title_run.font.name = 'Arial'

    # Subtitle
    sub_run = para.add_run("Server Components & Solutions\n\n")
    sub_run.font.size = Pt(18)
    sub_run.font.color.rgb = RGBColor(255, 242, 223)
    sub_run.font.name = 'Arial'

    # Year
    year_run = para.add_run("2024 - 2025\n\n\n\n\n")
    year_run.font.size = Pt(16)
    year_run.font.color.rgb = RGBColor(255, 242, 223)

    # Bottom decorative line
    bottom_line = para.add_run("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n")
    bottom_line.font.size = Pt(10)
    bottom_line.font.color.rgb = RGBColor(255, 242, 223)

    # Contact Info
    contact_run = para.add_run("Tel: XXX-XXXX-XXXX  |  Email: example@company.com\n")
    contact_run.font.size = Pt(11)
    contact_run.font.color.rgb = RGBColor(255, 255, 255)
    contact_run.font.name = 'Arial'

    address_run = para.add_run("Address: Your Company Address\n\n\n")
    address_run.font.size = Pt(11)
    address_run.font.color.rgb = RGBColor(255, 255, 255)
    address_run.font.name = 'Arial'

    doc.add_page_break()

def create_company_intro_page(doc):
    """Create company introduction page"""
    title = doc.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = title.add_run("ABOUT US")
    run.font.size = Pt(28)
    run.font.bold = True
    run.font.color.rgb = RGBColor(1, 86, 151)
    run.font.name = 'Arial'

    subtitle = doc.add_paragraph()
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = subtitle.add_run("Company Profile")
    run.font.size = Pt(14)
    run.font.color.rgb = RGBColor(1, 58, 99)
    run.font.name = 'Arial'

    doc.add_paragraph()

    # Company intro box
    intro_table = doc.add_table(rows=1, cols=1)
    intro_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = intro_table.cell(0, 0)
    set_cell_shading(cell, CREAM_PINK)
    set_cell_border(cell, CAPRI_BLUE, "8")

    cell_para = cell.paragraphs[0]
    run = cell_para.add_run("""
    Company Introduction

    [Enter your company introduction here, including establishment date,
    main business, and development history.

    Suggested content:
    • Year of establishment and development history
    • Main products and service scope
    • Company size and team strength
    • Core competitive advantages
    • Service philosophy and business principles]

    """)
    run.font.size = Pt(12)
    run.font.color.rgb = RGBColor(1, 58, 99)
    run.font.name = 'Arial'

    doc.add_paragraph()
    doc.add_paragraph()

    # Our Advantages
    adv_title = doc.add_paragraph()
    adv_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = adv_title.add_run("OUR ADVANTAGES")
    run.font.size = Pt(20)
    run.font.bold = True
    run.font.color.rgb = RGBColor(1, 86, 151)
    run.font.name = 'Arial'

    doc.add_paragraph()

    # Advantages table 2x2
    adv_table = doc.add_table(rows=2, cols=2)
    adv_table.alignment = WD_TABLE_ALIGNMENT.CENTER

    advantages = [
        ("Genuine Products", "All products are original with full warranty"),
        ("Competitive Pricing", "Direct from manufacturer, best prices"),
        ("Technical Support", "Professional team, pre & after sales service"),
        ("Fast Delivery", "Sufficient stock, same-day shipping")
    ]

    for i, (title_text, desc) in enumerate(advantages):
        row = i // 2
        col = i % 2
        cell = adv_table.cell(row, col)
        set_cell_shading(cell, CREAM_PINK)
        set_cell_border(cell, CAPRI_BLUE, "4")
        para = cell.paragraphs[0]

        title_run = para.add_run("■ " + title_text + "\n")
        title_run.font.size = Pt(14)
        title_run.font.bold = True
        title_run.font.color.rgb = RGBColor(1, 86, 151)
        title_run.font.name = 'Arial'

        desc_run = para.add_run(desc)
        desc_run.font.size = Pt(11)
        desc_run.font.color.rgb = RGBColor(1, 58, 99)
        desc_run.font.name = 'Arial'

    doc.add_page_break()

def create_packaging_page(doc):
    """Create packaging display page"""
    title = doc.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = title.add_run("PACKAGING DISPLAY")
    run.font.size = Pt(28)
    run.font.bold = True
    run.font.color.rgb = RGBColor(1, 86, 151)
    run.font.name = 'Arial'

    subtitle = doc.add_paragraph()
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = subtitle.add_run("Product Packaging Showcase")
    run.font.size = Pt(14)
    run.font.color.rgb = RGBColor(1, 58, 99)
    run.font.name = 'Arial'

    doc.add_paragraph()

    # Packaging images - 2 rows x 3 columns
    for row_num in range(2):
        row_table = doc.add_table(rows=2, cols=3)
        row_table.alignment = WD_TABLE_ALIGNMENT.CENTER

        # Image row
        for col in range(3):
            cell = row_table.cell(0, col)
            set_cell_shading(cell, CREAM_PINK)
            set_cell_border(cell, CAPRI_BLUE, "4")
            cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            para = cell.paragraphs[0]
            para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = para.add_run(f"\n\n[ Image {row_num * 3 + col + 1} ]\n\n")
            run.font.size = Pt(12)
            run.font.color.rgb = RGBColor(1, 86, 151)
            run.font.name = 'Arial'

        # Title row
        for col in range(3):
            cell = row_table.cell(1, col)
            set_cell_shading(cell, CAPRI_BLUE)
            set_no_border(cell)
            para = cell.paragraphs[0]
            para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = para.add_run(f"Package {row_num * 3 + col + 1}")
            run.font.size = Pt(10)
            run.font.bold = True
            run.font.color.rgb = RGBColor(255, 255, 255)
            run.font.name = 'Arial'

        doc.add_paragraph()

    doc.add_page_break()

def create_catalog_page(doc):
    """Create product catalog index page"""
    title = doc.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = title.add_run("CONTENTS")
    run.font.size = Pt(28)
    run.font.bold = True
    run.font.color.rgb = RGBColor(1, 86, 151)
    run.font.name = 'Arial'

    subtitle = doc.add_paragraph()
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = subtitle.add_run("Product Categories")
    run.font.size = Pt(14)
    run.font.color.rgb = RGBColor(1, 58, 99)
    run.font.name = 'Arial'

    doc.add_paragraph()
    doc.add_paragraph()

    catalog_items = [
        ("01", "HPE Server Memory", "DDR4/DDR5 Series"),
        ("02", "Dell Server Memory", "DDR4/DDR5 Series"),
        ("03", "Lenovo Server Memory", "ThinkSystem Series"),
        ("04", "HPE Enterprise HDD", "SAS HDD Series"),
        ("05", "More Products", "Coming Soon...")
    ]

    for num, title_text, desc in catalog_items:
        item_table = doc.add_table(rows=1, cols=3)
        item_table.alignment = WD_TABLE_ALIGNMENT.CENTER

        # Number
        cell0 = item_table.cell(0, 0)
        set_cell_shading(cell0, CAPRI_BLUE)
        set_no_border(cell0)
        para0 = cell0.paragraphs[0]
        para0.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run0 = para0.add_run(num)
        run0.font.size = Pt(18)
        run0.font.bold = True
        run0.font.color.rgb = RGBColor(255, 255, 255)
        run0.font.name = 'Arial'

        # Title
        cell1 = item_table.cell(0, 1)
        set_cell_shading(cell1, CREAM_PINK)
        set_cell_border(cell1, CAPRI_BLUE, "2")
        para1 = cell1.paragraphs[0]
        run1 = para1.add_run("  " + title_text)
        run1.font.size = Pt(16)
        run1.font.bold = True
        run1.font.color.rgb = RGBColor(1, 58, 99)
        run1.font.name = 'Arial'

        # Description
        cell2 = item_table.cell(0, 2)
        set_cell_shading(cell2, WHITE)
        set_cell_border(cell2, CAPRI_BLUE, "2")
        para2 = cell2.paragraphs[0]
        run2 = para2.add_run("  " + desc)
        run2.font.size = Pt(12)
        run2.font.color.rgb = RGBColor(1, 86, 151)
        run2.font.name = 'Arial'

        doc.add_paragraph()

    doc.add_page_break()

def create_product_section_header(doc, title, subtitle):
    """Create product section header"""
    header_table = doc.add_table(rows=1, cols=1)
    header_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = header_table.cell(0, 0)
    set_cell_shading(cell, CAPRI_BLUE)
    set_no_border(cell)

    para = cell.paragraphs[0]
    para.alignment = WD_ALIGN_PARAGRAPH.CENTER

    run = para.add_run("  " + title + "  ")
    run.font.size = Pt(22)
    run.font.bold = True
    run.font.color.rgb = RGBColor(255, 255, 255)
    run.font.name = 'Arial'

    sub = doc.add_paragraph()
    sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = sub.add_run(subtitle)
    run.font.size = Pt(12)
    run.font.color.rgb = RGBColor(1, 58, 99)
    run.font.name = 'Arial'

    doc.add_paragraph()

def create_product_table(doc, products, columns):
    """Create product list table"""
    table = doc.add_table(rows=1, cols=len(columns))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER

    # Header row
    header_row = table.rows[0]
    for i, col_name in enumerate(columns):
        cell = header_row.cells[i]
        set_cell_shading(cell, CAPRI_BLUE)
        set_no_border(cell)
        para = cell.paragraphs[0]
        para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = para.add_run(col_name)
        run.font.size = Pt(10)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)
        run.font.name = 'Arial'

    # Data rows
    for idx, product in enumerate(products):
        row = table.add_row()
        bg_color = WHITE if idx % 2 == 0 else CREAM_PINK

        for i, value in enumerate(product):
            cell = row.cells[i]
            set_cell_shading(cell, bg_color)
            set_cell_border(cell, CAPRI_BLUE, "2")
            para = cell.paragraphs[0]
            run = para.add_run(str(value))
            run.font.size = Pt(9)
            run.font.color.rgb = RGBColor(1, 58, 99)
            run.font.name = 'Arial'

    doc.add_paragraph()

def main():
    """Main function"""
    doc = Document()

    # Page margins
    sections = doc.sections
    for section in sections:
        section.top_margin = Cm(1.5)
        section.bottom_margin = Cm(1.5)
        section.left_margin = Cm(2)
        section.right_margin = Cm(2)

    # Create cover
    create_cover_page(doc)

    # Create company intro
    create_company_intro_page(doc)

    # Create packaging page
    create_packaging_page(doc)

    # Create catalog index
    create_catalog_page(doc)

    # ==================== HPE Server Memory ====================
    create_product_section_header(doc, "HPE SERVER MEMORY", "DDR4/DDR5 Series")

    g10_title = doc.add_paragraph()
    run = g10_title.add_run("▶ G10 Series Memory")
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.color.rgb = RGBColor(1, 86, 151)
    run.font.name = 'Arial'

    hpe_g10_products = [
        ("P00924-B21", "HPE 32GB Dual rank x4 DDR4-2933", "32GB", "DDR4-2933", "CAS-21-21-21"),
        ("815100-B21", "HPE 32GB Dual rank x4 DDR4-2666", "32GB", "DDR4-2666", "CAS-19-19-19"),
        ("P00930-B21", "HPE 64GB Dual rank x4 DDR4-2933", "64GB", "DDR4-2933", "CAS-21-21-21"),
        ("P00926-B21", "HPE 64GB Quad rank x4 DDR4-2933", "64GB", "DDR4-2933", "Load reduced"),
        ("P11040-B21", "HPE 128GB Quad rank x4 DDR4-2933", "128GB", "DDR4-2933", "Load reduced"),
        ("815101-B21", "HPE 64GB Quad rank x4 DDR4-2666", "64GB", "DDR4-2666", "Load reduced"),
        ("P00928-B21", "HPE 128GB Octal rank x4 DDR4-2933", "128GB", "DDR4-2933", "3DS"),
        ("815102-B21", "HPE 128GB Octal rank x4 DDR4-2666", "128GB", "DDR4-2666", "3DS"),
    ]
    create_product_table(doc, hpe_g10_products, ["Part Number", "Description", "Capacity", "Spec", "Type"])

    g10plus_title = doc.add_paragraph()
    run = g10plus_title.add_run("▶ G10+ Series Memory")
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.color.rgb = RGBColor(1, 86, 151)
    run.font.name = 'Arial'

    hpe_g10plus_products = [
        ("P06033-B21", "HPE 32GB Dual rank x4 DDR4-3200", "32GB", "DDR4-3200", "CAS-22-22-22"),
        ("P06035-B21", "HPE 64GB Dual rank x4 DDR4-3200", "64GB", "DDR4-3200", "CAS-22-22-22"),
        ("P40007-B21", "HPE 32GB Single rank x4 DDR4-3200", "32GB", "DDR4-3200", "Registered"),
        ("P06037-B21", "HPE 128GB Quad rank x4 DDR4-3200", "128GB", "DDR4-3200", "Load reduced"),
        ("P06039-B21", "HPE 256GB Octal rank x4 DDR4-3200", "256GB", "DDR4-3200", "3DS"),
    ]
    create_product_table(doc, hpe_g10plus_products, ["Part Number", "Description", "Capacity", "Spec", "Type"])

    g11_title = doc.add_paragraph()
    run = g11_title.add_run("▶ G11 Series Memory (DDR5)")
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.color.rgb = RGBColor(1, 86, 151)
    run.font.name = 'Arial'

    hpe_g11_products = [
        ("P64705-B21", "HPE 16GB Single Rank x8 DDR5-5600", "16GB", "DDR5-5600", "P65253-001"),
        ("P64706-B21", "HPE 32GB Dual Rank x8 DDR5-5600", "32GB", "DDR5-5600", "P65254-001"),
        ("P64707-B21", "HPE 64GB Dual Rank x4 DDR5-5600", "64GB", "DDR5-5600", "P65255-001"),
        ("P64708-B21", "HPE 96GB Dual Rank x4 DDR5-5600", "96GB", "DDR5-5600", "P65256-001"),
        ("P64709-B21", "HPE 128GB Quad Rank x4 DDR5-5600", "128GB", "DDR5-5600", "P65257-001"),
        ("P43322-B21", "HPE 16GB Single Rank x8 DDR5-4800", "16GB", "DDR5-4800", "P48499-001"),
        ("P43328-B21", "HPE 32GB Dual Rank x8 DDR5-4800", "32GB", "DDR5-4800", "P48501-001"),
        ("P43331-B21", "HPE 64GB Dual Rank x4 DDR5-4800", "64GB", "DDR5-4800", "P48502-001"),
        ("P66675-B21", "HPE 96GB 2Rx4 PC5-4800B-R Smart Kit", "96GB", "DDR5-4800", "P67364-001"),
        ("P43334-B21", "HPE 128GB Quad Rank x4 DDR5-4800", "128GB", "DDR5-4800", "P48503-001"),
        ("P43337-B21", "HPE 256GB Octal Rank x4 DDR5-4800", "256GB", "DDR5-4800", "P48504-001"),
    ]
    create_product_table(doc, hpe_g11_products, ["Part Number", "Description", "Capacity", "Spec", "Spare P/N"])

    doc.add_page_break()

    # ==================== Dell Server Memory ====================
    create_product_section_header(doc, "DELL SERVER MEMORY", "DDR4/DDR5 Series")

    dell_products = [
        ("AA601616", "SNP8WKDYC/32G 32GB PC4-23400 DDR4-2933MHz", "32GB", "DDR4-2933", "2Rx4"),
        ("AA601615", "SNPW403YC/64G 64GB DDR4 RDIMM 2933 MT/s", "64GB", "DDR4-2933", "2Rx4"),
        ("AA579531", "SNP8WKDYC/32G 32-GB 2Rx4 2933MHz PC4-23400", "32GB", "DDR4-2933", "2Rx4"),
        ("AA579530", "SNPW403YC/64G 64GB DDR4 RDIMM 2933 MT/s", "64GB", "DDR4-2933", "2Rx4"),
        ("AA783422", "SNP75X1VC/32G 32GB DDR4 RDIMM 3200 MT/s", "32GB", "DDR4-3200", "2Rx4"),
        ("AA783423", "SNPP2MYX/64G 64GB DDR4 RDIMM 3200 MT/s", "64GB", "DDR4-3200", "2Rx4"),
        ("AA799110", "SNPP2MYX/64G 64GB DDR4 RDIMM 3200 MT/s", "64GB", "DDR4-3200", "2Rx4"),
        ("AA810828", "SNPP2MYX/64G 64GB DDR4 RDIMM 3200 MT/s", "64GB", "DDR4-3200", "2Rx4"),
        ("AB445285", "SNP7JXF5C/128G 128GB DDR4 LRDIMM 3200 MT/s", "128GB", "DDR4-3200", "4Rx4"),
        ("AC239377", "SNP1V1N1C/16G 16GB DDR5 RDIMM 4800 MT/s", "16GB", "DDR5-4800", "1Rx8"),
        ("AC239378", "SNPW08W9C/32G 32GB DDR5 RDIMM 4800 MT/s", "32GB", "DDR5-4800", "2Rx8"),
        ("AC239379", "SNP152K5C/64G 64GB DDR5 RDIMM 4800 MT/s", "64GB", "DDR5-4800", "2Rx4"),
        ("AC830716", "SNPSD48RC/16G 16GB PC5-44800 DDR5-5600MHz", "16GB", "DDR5-5600", "1Rx8"),
        ("AC958788", "SNPXHJ68MC/16G AC958788 16G DDR5 UDIMM 5600 MT/s", "16GB", "DDR5-5600", "1Rx8"),
        ("AC774043", "SNP8D9M0C/32G 32G 2RX8 PC5 5600B-E DDR5 ECC UDIMM", "32GB", "DDR5-5600", "2Rx8"),
        ("AC830717", "SNPP8XPWC/32G 32GB 2RX8 PC5-44800 DDR5-5600B ECC RDIMM", "32GB", "DDR5-5600", "2Rx8"),
        ("AC830718", "SNP58F3NC/64G 64GB 2Rx4 PC5-44800B-R DDR5-5600 RDIMM", "64GB", "DDR5-5600", "2Rx4"),
        ("AC888060", "SNP5DR48C/16G 16GB DDR5-5600 ECC RDIMM", "16GB", "DDR5-5600", "1Rx8"),
    ]
    create_product_table(doc, dell_products, ["Part Number", "Description", "Capacity", "Spec", "Rank"])

    doc.add_page_break()

    # ==================== Lenovo Server Memory ====================
    create_product_section_header(doc, "LENOVO SERVER MEMORY", "ThinkSystem Series")

    lenovo_products = [
        ("4ZC7A08707", "ThinkSystem 01KR353 16GB 1Rx4 PC4-2933Y", "16GB", "DDR4-2933", "1Rx4"),
        ("4ZC7A08709", "ThinkSystem 01KR355 32GB 2RX4 PC4-2933Y DDR4 REG ECC", "32GB", "DDR4-2933", "2Rx4"),
        ("4ZC7A08710", "ThinkSystem 01KR356 64GB 2Rx4 PC4-2933Y RECC", "64GB", "DDR4-2933", "2Rx4"),
        ("4X77A08634", "ThinkSystem 02JK239 32GB 2RX8 DDR4 3200 RDIMM", "32GB", "DDR4-3200", "2Rx8"),
        ("4X77A08633", "ThinkSystem 02JK237 32GB 2Rs4 PC4-3200AA", "32GB", "DDR4-3200", "2Rs4"),
        ("4ZC7A15124", "ThinkSystem 02JG340 64GB 2RX4 PC4-3200AA-RDIMM", "64GB", "DDR4-3200", "2Rx4"),
        ("4X77A08635", "ThinkSystem 02JK971 64G 2RX4 DDR4 3200", "64GB", "DDR4-3200", "2Rx4"),
        ("4X77A77496", "ThinkSystem 03GX401 32GB PC4-3200AA ECC UDIMM", "32GB", "DDR4-3200", "ECC UDIMM"),
        ("4X77A85511", "ThinkSystem 16GB TruDDR5 4800 MHz (1Rx8)", "16GB", "DDR5-4800", "1Rx8"),
        ("4X77A77483", "ThinkSystem 32GB TruDDR5 4800MHz (1Rx4)", "32GB", "DDR5-4800", "1Rx4"),
        ("4X77A88512", "ThinkSystem 32GB TruDDR5 4800MHz (2Rx8)", "32GB", "DDR5-4800", "2Rx8"),
        ("4X77A77031", "ThinkSystem 32GB TruDDR5 4800MHz (2Rx8)", "32GB", "DDR5-4800", "2Rx8"),
        ("4X77A81440", "ThinkSystem 03KL461 32G TruDDR5 2RX8 4800", "32GB", "DDR5-4800", "2Rx8"),
        ("4X77A81442", "ThinkSystem 03GX338 64G TruDDR5 2RX4 PC5 4800B", "64GB", "DDR5-4800", "2Rx4"),
        ("4X77A77033", "ThinkSystem 64GB TruDDR5 4800MHz (2Rx4)", "64GB", "DDR5-4800", "2Rx4"),
        ("4X77A77034", "ThinkSystem 128GB TruDDR5 4800MHz 4Rx4 3DS RDIMM", "128GB", "DDR5-4800", "4Rx4"),
        ("4X77A77035", "ThinkSystem 256GB TruDDR5 4800MHz (8Rx4)", "256GB", "DDR5-4800", "8Rx4"),
        ("4X77A88049", "ThinkSystem 32GB TruDDR5 5600MHz (1Rx4)", "32GB", "DDR5-5600", "1Rx4"),
        ("4X77A88051", "ThinkSystem 32GB TruDDR5 5600MHz (2Rx8)", "32GB", "DDR5-5600", "2Rx8"),
        ("4X77A90992", "ThinkSystem 64GB TruDDR5 5600MHz 2Rx4", "64GB", "DDR5-5600", "2Rx4"),
        ("4X77A88052", "ThinkSystem 64GB TruDDR5 5600MHz (2Rx4)", "64GB", "DDR5-5600", "2Rx4"),
        ("4X77A93887", "ThinkSystem 128GB TruDDR5 5600MHz (2Rx4) RDIMM", "128GB", "DDR5-5600", "2Rx4"),
        ("4X77A88054", "ThinkSystem 128GB TruDDR5 5600MHz (4Rx4)", "128GB", "DDR5-5600", "4Rx4"),
        ("4X77A88055", "ThinkSystem 256GB TruDDR5 5600 MHz (8Rx4) 3DS RDIMM", "256GB", "DDR5-5600", "8Rx4"),
    ]
    create_product_table(doc, lenovo_products, ["Part Number", "Description", "Capacity", "Spec", "Rank"])

    doc.add_page_break()

    # ==================== HPE Enterprise HDD ====================
    create_product_section_header(doc, "HPE ENTERPRISE HDD", "SAS HDD Series")

    enterprise_title = doc.add_paragraph()
    run = enterprise_title.add_run("▶ Enterprise 10K/15K SAS HDD (2.5\" SFF)")
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.color.rgb = RGBColor(1, 86, 151)
    run.font.name = 'Arial'

    hpe_hdd_enterprise = [
        ("881457-B21", "HPE 2.4TB SAS 12G Enterprise 10K SFF 512e DS firmware HDD", "2.4TB", "10K", "SFF 2.5\""),
        ("872481-B21", "HPE 1.8TB SAS 12G Enterprise 10K SFF 512e DS firmware HDD", "1.8TB", "10K", "SFF 2.5\""),
        ("872479-B21", "HPE 1.2TB SAS 12G Enterprise 10K SFF DS firmware HDD", "1.2TB", "10K", "SFF 2.5\""),
        ("870759-B21", "HPE 900GB SAS 12G Enterprise 15K SFF DS firmware HDD", "900GB", "15K", "SFF 2.5\""),
        ("870757-B21", "HPE 600GB SAS 12G Enterprise 15K SFF DS firmware HDD", "600GB", "15K", "SFF 2.5\""),
        ("872477-B21", "HPE 600GB SAS 12G Enterprise 10K SFF DS firmware HDD", "600GB", "10K", "SFF 2.5\""),
        ("870753-B21", "HPE 300GB SAS 12G Enterprise 15K SFF DS firmware HDD", "300GB", "15K", "SFF 2.5\""),
        ("872475-B21", "HPE 300GB SAS 12G Enterprise 10K SFF DS firmware HDD", "300GB", "10K", "SFF 2.5\""),
    ]
    create_product_table(doc, hpe_hdd_enterprise, ["Part Number", "Description", "Capacity", "Speed", "Form Factor"])

    midline_title = doc.add_paragraph()
    run = midline_title.add_run("▶ Midline 7.2K SAS HDD")
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.color.rgb = RGBColor(1, 86, 151)
    run.font.name = 'Arial'

    hpe_hdd_midline = [
        ("765466-B21", "HPE 2TB SAS 12G Midline 7.2K SFF 512e HDD", "2TB", "7.2K", "SFF 2.5\""),
        ("832514-B21", "HPE 1TB SAS 12G Midline 7.2K SFF DS firmware HDD", "1TB", "7.2K", "SFF 2.5\""),
        ("P23863-B21", "HPE 16TB SAS 12G Business Critical 7.2K LFF 512e ISE HDD", "16TB", "7.2K", "LFF 3.5\""),
        ("P09153-B21", "HPE 14TB SAS 12G Midline 7.2K LFF Helium 512e DS firmware HDD", "14TB", "7.2K", "LFF 3.5\""),
        ("881779-B21", "HPE 12TB SAS 12G Midline 7.2K LFF Helium 512e DS firmware HDD", "12TB", "7.2K", "LFF 3.5\""),
        ("857644-B21", "HPE 10TB SAS 12G Midline 7.2K LFF Helium 512e DS firmware HDD", "10TB", "7.2K", "LFF 3.5\""),
        ("819201-B21", "HPE 8TB SAS 12G Midline 7.2K LFF DS firmware HDD", "8TB", "7.2K", "LFF 3.5\""),
        ("861754-B21", "HPE 6TB SAS 12G Midline 7.2K LFF HDD", "6TB", "7.2K", "LFF 3.5\""),
    ]
    create_product_table(doc, hpe_hdd_midline, ["Part Number", "Description", "Capacity", "Speed", "Form Factor"])

    mc_title = doc.add_paragraph()
    run = mc_title.add_run("▶ Mission Critical SAS HDD")
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.color.rgb = RGBColor(1, 86, 151)
    run.font.name = 'Arial'

    hpe_hdd_mc = [
        ("P28352-B21", "HPE 2.4TB SAS 12G mission critical 10K SFF BC 3-year warranty 512e HDD", "2.4TB", "10K", "SFF"),
        ("P28586-B21", "HPE 1.2TB SAS 12G mission critical 10K SFF BC 3-year warranty HDD", "1.2TB", "10K", "SFF"),
        ("P28028-B21", "HPE 300GB SAS 12G mission critical 15K SFF BC 3-year warranty HDD", "300GB", "15K", "SFF"),
        ("P40430-B21", "HPE 300GB SAS 12G mission critical 10K SFF BC 3-year warranty HDD", "300GB", "10K", "SFF"),
        ("P37669-B21", "HPE 18TB SAS 12G business critical 7.2K LFF LP 1-year warranty 512e ISE HDD", "18TB", "7.2K", "LFF"),
        ("P23608-B21", "HPE 16TB SAS 12G business critical 7.2K LFF LP 1-year warranty 512e ISE HDD", "16TB", "7.2K", "LFF"),
        ("P09155-B21", "HPE 14TB SAS 12G MDL 7.2K LFF LP 1-year warranty helium 512e DS firmware HDD", "14TB", "7.2K", "LFF"),
        ("881781-B21", "HPE 12TB SAS 12G MDL 7.2K LFF LP 1-year warranty helium 512e DS firmware HDD", "12TB", "7.2K", "LFF"),
        ("P09149-B21", "HPE 10TB SAS 12G MDL 7.2K LFF LP 1-year warranty helium 512e DS firmware HDD", "10TB", "7.2K", "LFF"),
        ("834031-B21", "HPE 8TB SAS 12G MDL 7.2K LFF LP 1-year warranty 512e DS firmware HDD", "8TB", "7.2K", "LFF"),
        ("861746-B21", "HPE 6TB SAS 12G MDL 7.2K LFF LP 1-year warranty 512e HDD", "6TB", "7.2K", "LFF"),
    ]
    create_product_table(doc, hpe_hdd_mc, ["Part Number", "Description", "Capacity", "Speed", "Form Factor"])

    doc.add_page_break()

    # ==================== Contact Us Page ====================
    contact_bg = doc.add_table(rows=1, cols=1)
    contact_bg.alignment = WD_TABLE_ALIGNMENT.CENTER
    bg_cell = contact_bg.cell(0, 0)
    set_cell_shading(bg_cell, CREAM_PINK)
    set_no_border(bg_cell)

    para = bg_cell.paragraphs[0]
    para.alignment = WD_ALIGN_PARAGRAPH.CENTER

    para.add_run("\n\n\n")

    title_run = para.add_run("CONTACT US\n")
    title_run.font.size = Pt(28)
    title_run.font.bold = True
    title_run.font.color.rgb = RGBColor(1, 86, 151)
    title_run.font.name = 'Arial'

    sub_run = para.add_run("Get In Touch\n\n")
    sub_run.font.size = Pt(14)
    sub_run.font.color.rgb = RGBColor(1, 58, 99)
    sub_run.font.name = 'Arial'

    line_run = para.add_run("━━━━━━━━━━━━━━━━━━\n\n\n")
    line_run.font.color.rgb = RGBColor(1, 86, 151)

    doc.add_paragraph()

    # Contact info table
    contact_table = doc.add_table(rows=5, cols=2)
    contact_table.alignment = WD_TABLE_ALIGNMENT.CENTER

    contact_info = [
        ("Phone", "XXX-XXXX-XXXX"),
        ("Mobile", "XXX-XXXX-XXXX"),
        ("Email", "example@company.com"),
        ("Website", "www.yourcompany.com"),
        ("Address", "Your Company Address"),
    ]

    for i, (label, value) in enumerate(contact_info):
        cell0 = contact_table.cell(i, 0)
        set_cell_shading(cell0, CAPRI_BLUE)
        set_no_border(cell0)
        para0 = cell0.paragraphs[0]
        para0.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run0 = para0.add_run(label)
        run0.font.size = Pt(12)
        run0.font.bold = True
        run0.font.color.rgb = RGBColor(255, 255, 255)
        run0.font.name = 'Arial'

        cell1 = contact_table.cell(i, 1)
        set_cell_shading(cell1, WHITE)
        set_cell_border(cell1, CAPRI_BLUE, "2")
        para1 = cell1.paragraphs[0]
        run1 = para1.add_run("  " + value)
        run1.font.size = Pt(12)
        run1.font.color.rgb = RGBColor(1, 58, 99)
        run1.font.name = 'Arial'

    doc.add_paragraph()
    doc.add_paragraph()

    # QR Code placeholder
    qr_table = doc.add_table(rows=1, cols=1)
    qr_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    qr_cell = qr_table.cell(0, 0)
    set_cell_shading(qr_cell, CREAM_PINK)
    set_cell_border(qr_cell, CAPRI_BLUE, "4")
    qr_para = qr_cell.paragraphs[0]
    qr_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = qr_para.add_run("\n\n[ QR Code ]\n\n")
    run.font.size = Pt(14)
    run.font.color.rgb = RGBColor(1, 86, 151)
    run.font.name = 'Arial'

    scan_para = doc.add_paragraph()
    scan_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = scan_para.add_run("Scan to connect")
    run.font.size = Pt(12)
    run.font.color.rgb = RGBColor(1, 58, 99)
    run.font.name = 'Arial'

    # Save document
    output_path = "/home/user/-JC-/Product_Catalog.docx"
    doc.save(output_path)
    print(f"✅ Product Catalog created: {output_path}")
    return output_path

if __name__ == "__main__":
    main()
