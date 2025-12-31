# -*- coding: utf-8 -*-
"""
Product Catalog Generator
Burgundy Premium Color Scheme
With product image placeholders
"""

from docx import Document
from docx.shared import Inches, Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml.ns import qn, nsdecls
from docx.oxml import parse_xml

# Premium Color Scheme
CREAM = "EFDFCE"          # Cream - Background
BURGUNDY = "7E041D"       # Burgundy Red - Accent
DARK_GRAY = "363636"      # Dark Gray - Text
WHITE = "FFFFFF"

def set_cell_shading(cell, color):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_cell_border(cell, color="7E041D", size="4"):
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
    """Create cover page with cream background"""
    bg_table = doc.add_table(rows=1, cols=1)
    bg_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    bg_cell = bg_table.cell(0, 0)
    set_cell_shading(bg_cell, CREAM)
    set_no_border(bg_cell)

    para = bg_cell.paragraphs[0]
    para.alignment = WD_ALIGN_PARAGRAPH.CENTER

    para.add_run("\n\n\n\n\n")

    logo_run = para.add_run("[ LOGO ]\n\n\n")
    logo_run.font.size = Pt(18)
    logo_run.font.color.rgb = RGBColor(126, 4, 29)
    logo_run.font.name = 'Arial'

    company_run = para.add_run("YOUR COMPANY NAME\n")
    company_run.font.size = Pt(36)
    company_run.font.bold = True
    company_run.font.color.rgb = RGBColor(54, 54, 54)
    company_run.font.name = 'Arial'

    line_run = para.add_run("━━━━━━━━━━━━━━━━━━\n\n")
    line_run.font.size = Pt(14)
    line_run.font.color.rgb = RGBColor(126, 4, 29)

    title_run = para.add_run("PRODUCT CATALOG\n")
    title_run.font.size = Pt(48)
    title_run.font.bold = True
    title_run.font.color.rgb = RGBColor(126, 4, 29)
    title_run.font.name = 'Arial'

    sub_run = para.add_run("Server Components & Solutions\n\n")
    sub_run.font.size = Pt(18)
    sub_run.font.color.rgb = RGBColor(54, 54, 54)
    sub_run.font.name = 'Arial'

    year_run = para.add_run("2024 - 2025\n\n\n\n\n")
    year_run.font.size = Pt(16)
    year_run.font.color.rgb = RGBColor(126, 4, 29)

    bottom_line = para.add_run("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n")
    bottom_line.font.size = Pt(10)
    bottom_line.font.color.rgb = RGBColor(126, 4, 29)

    contact_run = para.add_run("Tel: XXX-XXXX-XXXX  |  Email: example@company.com\n")
    contact_run.font.size = Pt(11)
    contact_run.font.color.rgb = RGBColor(54, 54, 54)
    contact_run.font.name = 'Arial'

    address_run = para.add_run("Address: Your Company Address\n\n\n")
    address_run.font.size = Pt(11)
    address_run.font.color.rgb = RGBColor(54, 54, 54)
    address_run.font.name = 'Arial'

    doc.add_page_break()

def create_company_intro_page(doc):
    """Create company introduction page"""
    title = doc.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = title.add_run("ABOUT US")
    run.font.size = Pt(28)
    run.font.bold = True
    run.font.color.rgb = RGBColor(126, 4, 29)
    run.font.name = 'Arial'

    doc.add_paragraph()

    intro_table = doc.add_table(rows=1, cols=1)
    intro_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = intro_table.cell(0, 0)
    set_cell_shading(cell, CREAM)
    set_cell_border(cell, BURGUNDY, "8")

    cell_para = cell.paragraphs[0]
    run = cell_para.add_run("""
    Company Introduction

    [Enter your company introduction here]

    • Year of establishment and development history
    • Main products and service scope
    • Company size and team strength
    • Core competitive advantages
    • Service philosophy

    """)
    run.font.size = Pt(12)
    run.font.color.rgb = RGBColor(54, 54, 54)
    run.font.name = 'Arial'

    doc.add_paragraph()

    adv_title = doc.add_paragraph()
    adv_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = adv_title.add_run("OUR ADVANTAGES")
    run.font.size = Pt(20)
    run.font.bold = True
    run.font.color.rgb = RGBColor(126, 4, 29)
    run.font.name = 'Arial'

    doc.add_paragraph()

    adv_table = doc.add_table(rows=2, cols=2)
    adv_table.alignment = WD_TABLE_ALIGNMENT.CENTER

    advantages = [
        ("Genuine Products", "Original products with full warranty"),
        ("Competitive Pricing", "Direct from manufacturer"),
        ("Technical Support", "Professional pre & after sales service"),
        ("Fast Delivery", "Same-day shipping available")
    ]

    for i, (title_text, desc) in enumerate(advantages):
        row = i // 2
        col = i % 2
        cell = adv_table.cell(row, col)
        set_cell_shading(cell, CREAM)
        set_cell_border(cell, DARK_GRAY, "4")
        para = cell.paragraphs[0]

        title_run = para.add_run("■ " + title_text + "\n")
        title_run.font.size = Pt(14)
        title_run.font.bold = True
        title_run.font.color.rgb = RGBColor(126, 4, 29)
        title_run.font.name = 'Arial'

        desc_run = para.add_run(desc)
        desc_run.font.size = Pt(11)
        desc_run.font.color.rgb = RGBColor(54, 54, 54)
        desc_run.font.name = 'Arial'

    doc.add_page_break()

def create_product_section_header(doc, title, subtitle):
    """Create product section header"""
    header_table = doc.add_table(rows=1, cols=1)
    header_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = header_table.cell(0, 0)
    set_cell_shading(cell, BURGUNDY)
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
    run.font.color.rgb = RGBColor(54, 54, 54)
    run.font.name = 'Arial'

    doc.add_paragraph()

def create_product_table_with_images(doc, products, columns):
    """Create product table with image placeholders"""
    # Add "Image" column at the beginning
    full_columns = ["Image"] + columns

    table = doc.add_table(rows=1, cols=len(full_columns))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER

    # Header row
    header_row = table.rows[0]
    for i, col_name in enumerate(full_columns):
        cell = header_row.cells[i]
        set_cell_shading(cell, BURGUNDY)
        set_no_border(cell)
        para = cell.paragraphs[0]
        para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = para.add_run(col_name)
        run.font.size = Pt(9)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)
        run.font.name = 'Arial'

    # Data rows with image placeholders
    for idx, product in enumerate(products):
        row = table.add_row()
        bg_color = WHITE if idx % 2 == 0 else CREAM

        # Image placeholder cell (first column)
        img_cell = row.cells[0]
        set_cell_shading(img_cell, bg_color)
        set_cell_border(img_cell, BURGUNDY, "2")
        img_cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
        img_para = img_cell.paragraphs[0]
        img_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        img_run = img_para.add_run("[IMG]")
        img_run.font.size = Pt(7)
        img_run.font.color.rgb = RGBColor(126, 4, 29)
        img_run.font.name = 'Arial'

        # Product data columns
        for i, value in enumerate(product):
            cell = row.cells[i + 1]  # +1 because first column is image
            set_cell_shading(cell, bg_color)
            set_cell_border(cell, BURGUNDY, "2")
            para = cell.paragraphs[0]
            run = para.add_run(str(value))
            run.font.size = Pt(8)
            run.font.color.rgb = RGBColor(54, 54, 54)
            run.font.name = 'Arial'

    doc.add_paragraph()

def main():
    doc = Document()

    sections = doc.sections
    for section in sections:
        section.top_margin = Cm(1.5)
        section.bottom_margin = Cm(1.5)
        section.left_margin = Cm(1.5)
        section.right_margin = Cm(1.5)

    # Cover
    create_cover_page(doc)

    # Company intro
    create_company_intro_page(doc)

    # ==================== HPE Server Memory ====================
    create_product_section_header(doc, "HPE SERVER MEMORY", "DDR4/DDR5 Series")

    g10_title = doc.add_paragraph()
    run = g10_title.add_run("▶ G10 Series Memory")
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.color.rgb = RGBColor(126, 4, 29)
    run.font.name = 'Arial'

    hpe_g10_products = [
        ("P00924-B21", "HPE 32GB (1x32GB) Dual rank x4 DDR4-2933 CAS-21-21-21 registered smart memory kit", "32GB", "DDR4-2933"),
        ("815100-B21", "HPE 32GB (1x32GB) Dual rank x4 DDR4-2666 CAS-19-19-19 registered smart memory kit", "32GB", "DDR4-2666"),
        ("P00930-B21", "HPE 64GB (1x64GB) Dual rank x4 DDR4-2933 CAS-21-21-21 registered smart memory kit", "64GB", "DDR4-2933"),
        ("P00926-B21", "HPE 64GB (1x64GB) quad rank x4 DDR4-2933 CAS-21-21-21 load reduced smart memory kit", "64GB", "DDR4-2933"),
        ("815101-B21", "HPE 64GB (1x64GB) quad rank x4 DDR4-2666 CAS-19-19-19 load reduced smart memory kit", "64GB", "DDR4-2666"),
        ("P11040-B21", "HPE 128GB (1x128GB) quad rank x4 DDR4-2933 CAS-24-21-21 load reduced smart memory kit", "128GB", "DDR4-2933"),
        ("P00928-B21", "HPE 128GB (1x128GB) octal rank x4 DDR4-2933 CAS-24-21-21 load reduced 3DS smart memory kit", "128GB", "DDR4-2933"),
        ("815102-B21", "HPE 128GB (1x128GB) octal rank x4 DDR4-2666 CAS-22-19-19 3DS load reduced smart memory kit", "128GB", "DDR4-2666"),
    ]
    create_product_table_with_images(doc, hpe_g10_products, ["Part No.", "Description", "Capacity", "Spec"])

    g10plus_title = doc.add_paragraph()
    run = g10plus_title.add_run("▶ G10+ Series Memory")
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.color.rgb = RGBColor(126, 4, 29)
    run.font.name = 'Arial'

    hpe_g10plus_products = [
        ("P06033-B21", "HPE 32GB (1x32GB) dual rank x4 DDR4-3200 CAS-22-22-22 registered smart memory kit", "32GB", "DDR4-3200"),
        ("P06035-B21", "HPE 64GB (1x64GB) dual rank x4 DDR4-3200 CAS-22-22-22 registered smart memory kit", "64GB", "DDR4-3200"),
        ("P40007-B21", "HPE 32GB (1x32GB) single rank x4 DDR4-3200 CAS-22-22-22 registered smart memory kit", "32GB", "DDR4-3200"),
        ("P06037-B21", "HPE 128GB (1x128GB) quad rank x4 DDR4-3200 CAS-22-22-22 load reduced smart memory kit", "128GB", "DDR4-3200"),
        ("P06039-B21", "HPE 256GB (1x256GB) octal rank x4 DDR4-3200 CAS-26-22-22 3DS load reduced smart memory kit", "256GB", "DDR4-3200"),
    ]
    create_product_table_with_images(doc, hpe_g10plus_products, ["Part No.", "Description", "Capacity", "Spec"])

    g11_title = doc.add_paragraph()
    run = g11_title.add_run("▶ G11 Series Memory (DDR5)")
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.color.rgb = RGBColor(126, 4, 29)
    run.font.name = 'Arial'

    hpe_g11_products = [
        ("P64705-B21", "HPE 16GB (1x16GB) Single Rank x8 DDR5-5600 CAS-46-45-45 EC8 Registered Smart Memory Kit", "16GB", "DDR5-5600"),
        ("P64706-B21", "HPE 32GB (1x32GB) Dual Rank x8 DDR5-5600 CAS-46-45-45 EC8 Registered Smart Memory Kit", "32GB", "DDR5-5600"),
        ("P64707-B21", "HPE 64GB (1x64GB) Dual Rank x4 DDR5-5600 CAS-46-45-45 EC8 Registered Smart Memory Kit", "64GB", "DDR5-5600"),
        ("P64708-B21", "HPE 96GB (1x96GB) Dual Rank x4 DDR5-5600 CAS-45-45-45 EC8 Registered Smart Memory Kit", "96GB", "DDR5-5600"),
        ("P64709-B21", "HPE 128GB (1x128GB) Quad Rank x4 DDR5-5600 CAS-52-45-45 EC8 Registered 3DS Smart Memory Kit", "128GB", "DDR5-5600"),
        ("P43322-B21", "HPE 16GB (1x16GB) Single Rank x8 DDR5-4800 CAS-40-39-39 EC8 Registered Smart Memory Kit", "16GB", "DDR5-4800"),
        ("P43328-B21", "HPE 32GB (1x32GB) Dual Rank x8 DDR5-4800 CAS-40-39-39 EC8 Registered Smart Memory Kit", "32GB", "DDR5-4800"),
        ("P43331-B21", "HPE 64GB (1x64GB) Dual Rank x4 DDR5-4800 CAS-40-39-39 EC8 Registered Smart Memory Kit", "64GB", "DDR5-4800"),
        ("P66675-B21", "HPE 96GB 2Rx4 PC5-4800B-R Smart Kit", "96GB", "DDR5-4800"),
        ("P43334-B21", "HPE 128GB (1x128GB) Quad Rank x4 DDR5-4800 CAS-46-39-39 EC8 Registered 3DS Smart Memory Kit", "128GB", "DDR5-4800"),
        ("P43337-B21", "HPE 256GB (1x256GB) Octal Rank x4 DDR5-4800 CAS-46-39-39 EC8 Registered 3DS Smart Memory Kit", "256GB", "DDR5-4800"),
    ]
    create_product_table_with_images(doc, hpe_g11_products, ["Part No.", "Description", "Capacity", "Spec"])

    doc.add_page_break()

    # ==================== Dell Server Memory ====================
    create_product_section_header(doc, "DELL SERVER MEMORY", "DDR4/DDR5 Series")

    dell_products = [
        ("AA601616", "SNP8WKDYC/32G 32GB PC4-23400 DDR4-2933MHz 2Rx4 R640/R740/R840/R940/T640", "32GB", "DDR4-2933"),
        ("AA601615", "SNPW403YC/64G 64GB 2Rx4 DDR4 RDIMM 2933 MT/s R640/R740/R840/R940/T640", "64GB", "DDR4-2933"),
        ("AA579531", "SNP8WKDYC/32G 32GB 2Rx4 2933MHz PC4-23400 R640/R740/R840/R940/T640", "32GB", "DDR4-2933"),
        ("AA579530", "SNPW403YC/64G 64GB 2Rx4 DDR4 RDIMM 2933 MT/s R640/R740/R840/R940/T640", "64GB", "DDR4-2933"),
        ("AA783422", "SNP75X1VC/32G 32GB 2Rx4 DDR4 RDIMM 3200 MT/s R6515/R6525/R740/R840/R940/T640/R740XD/R7515/R7525", "32GB", "DDR4-3200"),
        ("AA783423", "SNPP2MYX/64G 64GB 2RX4 DDR4 RDIMM 3200 MT/s R6515/R6525/R7515/C6525/R7525", "64GB", "DDR4-3200"),
        ("AA799110", "SNPP2MYX/64G 64GB 2Rx4 DDR4 RDIMM 3200 MT/s R6515/R6525/R7515/C6525/R7525", "64GB", "DDR4-3200"),
        ("AA810828", "SNPP2MYX/64G 64GB 2Rx4 DDR4 RDIMM 3200 MT/s R640/R740/R840/R940/T640", "64GB", "DDR4-3200"),
        ("AB445285", "SNP7JXF5C/128G 128GB 4Rx4 DDR4 LRDIMM 3200 MT/s R640/R740/R840/R940/T640", "128GB", "DDR4-3200"),
        ("AC239377", "SNP1V1N1C/16G 16GB 1Rx8 DDR5 RDIMM 4800 MT/s R660/R760/R6615/R7625", "16GB", "DDR5-4800"),
        ("AC239378", "SNPW08W9C/32G 32GB 2Rx8 DDR5 RDIMM 4800 MT/s R660/R760/R6615/R7625", "32GB", "DDR5-4800"),
        ("AC239379", "SNP152K5C/64G 64GB 2Rx4 DDR5 RDIMM 4800 MT/s R660/R760/R860/R960", "64GB", "DDR5-4800"),
        ("AC830716", "SNPSD48RC/16G 16GB PC5-44800 DDR5-5600MHz 1Rx8 RDIMM", "16GB", "DDR5-5600"),
        ("AC958788", "SNPXH68MC/16G 16G 1Rx8 DDR5 UDIMM 5600 MT/s", "16GB", "DDR5-5600"),
        ("AC774043", "SNP8D9M0C/32G 32G 2RX8 PC5 5600B-E DDR5 ECC UDIMM", "32GB", "DDR5-5600"),
        ("AC830717", "SNPP8XPWC/32G 32GB 2RX8 PC5-44800 DDR5-5600B ECC RDIMM", "32GB", "DDR5-5600"),
        ("AC830718", "SNP58F3NC/64G 64GB 2Rx4 PC5-44800B-R DDR5-5600 RDIMM", "64GB", "DDR5-5600"),
        ("AC888060", "SNP5DR48C/16G 16GB DDR5-5600 ECC RDIMM", "16GB", "DDR5-5600"),
    ]
    create_product_table_with_images(doc, dell_products, ["Part No.", "Description", "Capacity", "Spec"])

    doc.add_page_break()

    # ==================== Lenovo Server Memory ====================
    create_product_section_header(doc, "LENOVO SERVER MEMORY", "ThinkSystem Series")

    lenovo_products = [
        ("4ZC7A08707", "ThinkSystem 01KR353 16GB 1Rx4 PC4-2933Y", "16GB", "DDR4-2933"),
        ("4ZC7A08709", "ThinkSystem 01KR355 32G 2RX4 PC4-2933Y DDR4 REG ECC", "32GB", "DDR4-2933"),
        ("4ZC7A08710", "ThinkSystem 01KR356 64G 2Rx4 PC4-2933Y RECC", "64GB", "DDR4-2933"),
        ("4X77A08634", "ThinkSystem 02JK239 32G 2RX8 DDR4 3200 RDIMM", "32GB", "DDR4-3200"),
        ("4X77A08633", "ThinkSystem 02JK237 32GB 2Rx4 PC4-3200AA", "32GB", "DDR4-3200"),
        ("4ZC7A15124", "ThinkSystem 02JG340 64G 2RX4 PC4-3200AA-RDIMM", "64GB", "DDR4-3200"),
        ("4X77A08635", "ThinkSystem 02JK971 64G 2VX4 DDR4 3200", "64GB", "DDR4-3200"),
        ("4X77A77496", "ThinkSystem 03GX401 32GB PC4-3200AA ECC UDIMM", "32GB", "DDR4-3200"),
        ("4X77A85511", "ThinkSystem 16GB TruDDR5 4800 MHz(1Rx8)", "16GB", "DDR5-4800"),
        ("4X77A77483", "ThinkSystem 32GB TruDDR5 4800MHz(1Rx4)", "32GB", "DDR5-4800"),
        ("4X77A88512", "ThinkSystem 32GB TruDDR5 4800MHz (2Rx8)", "32GB", "DDR5-4800"),
        ("4X77A77031", "ThinkSystem 32GB TruDDR5 4800MHz(2Rx8)", "32GB", "DDR5-4800"),
        ("4X77A81440", "ThinkSystem 03KL461 32G TruDDR5 2RX8 4800", "32GB", "DDR5-4800"),
        ("4X77A81442", "ThinkSystem 03GX338 64G TruDDR5 2RX4 PC5 4800B", "64GB", "DDR5-4800"),
        ("4X77A77033", "ThinkSystem 64GB TruDDR5 4800MHz(2Rx4)", "64GB", "DDR5-4800"),
        ("4X77A77034", "ThinkSystem 128GB TruDDR5 4800MHz 4Rx4 3DS RDIMM", "128GB", "DDR5-4800"),
        ("4X77A77035", "ThinkSystem 256GB TruDDR5 4800MHz(8Rx4)", "256GB", "DDR5-4800"),
        ("4X77A88049", "ThinkSystem 32GB TruDDR5 5600MHz(1Rx4)", "32GB", "DDR5-5600"),
        ("4X77A88051", "ThinkSystem 32GB TruDDR5 5600MHz(2Rx8)", "32GB", "DDR5-5600"),
        ("4X77A90992", "ThinkSystem 64GB TruDDR5 5600MHz 2Rx4", "64GB", "DDR5-5600"),
        ("4X77A88052", "ThinkSystem 64GB TruDDR5 5600MHz(2Rx4)", "64GB", "DDR5-5600"),
        ("4X77A93887", "ThinkSystem 128GB TruDDR5 5600MHz (2Rx4)RDIMM", "128GB", "DDR5-5600"),
        ("4X77A88054", "ThinkSystem 128GB TruDDR5 5600MHz(4Rx4)", "128GB", "DDR5-5600"),
        ("4X77A88055", "ThinkSystem 256GB TruDDR5 5600 MHz (8Rx4) 3DS RDIMM", "256GB", "DDR5-5600"),
    ]
    create_product_table_with_images(doc, lenovo_products, ["Part No.", "Description", "Capacity", "Spec"])

    doc.add_page_break()

    # ==================== HPE Enterprise HDD ====================
    create_product_section_header(doc, "HPE ENTERPRISE HDD", "SAS HDD Series")

    # Enterprise 10K SFF
    hdd_title1 = doc.add_paragraph()
    run = hdd_title1.add_run("▶ Enterprise 10K SFF (2.5-inch)")
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.color.rgb = RGBColor(126, 4, 29)
    run.font.name = 'Arial'

    hpe_10k_sff = [
        ("881457-B21", "HPE 2.4TB SAS 12G Enterprise 10K SFF SC 3-year warranty 512e Digitally Signed (DS) firmware HDD", "2.4TB", "10K"),
        ("872481-B21", "HPE 1.8TB SAS 12G Enterprise 10K SFF SC 3-year warranty 512e DS firmware HDD", "1.8TB", "10K"),
        ("872479-B21", "HPE 1.2TB SAS 12G Enterprise 10K SFF SC 3-year warranty DS firmware HDD", "1.2TB", "10K"),
        ("872477-B21", "HPE 600GB SAS 12G Enterprise 10K SFF SC 3-year warranty DS firmware HDD", "600GB", "10K"),
        ("872475-B21", "HPE 300GB SAS 12G Enterprise 10K SFF SC 3-year warranty DS firmware HDD", "300GB", "10K"),
    ]
    create_product_table_with_images(doc, hpe_10k_sff, ["Part No.", "Description", "Capacity", "Speed"])

    # Enterprise 15K SFF
    hdd_title2 = doc.add_paragraph()
    run = hdd_title2.add_run("▶ Enterprise 15K SFF (2.5-inch)")
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.color.rgb = RGBColor(126, 4, 29)
    run.font.name = 'Arial'

    hpe_15k_sff = [
        ("870759-B21", "HPE 900GB SAS 12G Enterprise 15K SFF SC 3-year warranty DS firmware HDD", "900GB", "15K"),
        ("870757-B21", "HPE 600GB SAS 12G Enterprise 15K SFF SC 3-year warranty DS firmware HDD", "600GB", "15K"),
        ("870753-B21", "HPE 300GB SAS 12G Enterprise 15K SFF SC 3-year warranty DS firmware HDD", "300GB", "15K"),
    ]
    create_product_table_with_images(doc, hpe_15k_sff, ["Part No.", "Description", "Capacity", "Speed"])

    # Midline 7.2K SFF
    hdd_title3 = doc.add_paragraph()
    run = hdd_title3.add_run("▶ Midline 7.2K SFF (2.5-inch)")
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.color.rgb = RGBColor(126, 4, 29)
    run.font.name = 'Arial'

    hpe_72k_sff = [
        ("765466-B21", "HPE 2TB SAS 12G Midline 7.2K SFF SC 1-year warranty 512e HDD", "2TB", "7.2K"),
        ("832514-B21", "HPE 1TB SAS 12G Midline 7.2K SFF SC 1-year warranty DS firmware HDD", "1TB", "7.2K"),
    ]
    create_product_table_with_images(doc, hpe_72k_sff, ["Part No.", "Description", "Capacity", "Speed"])

    # Midline 7.2K LFF
    hdd_title4 = doc.add_paragraph()
    run = hdd_title4.add_run("▶ Midline 7.2K LFF (3.5-inch)")
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.color.rgb = RGBColor(126, 4, 29)
    run.font.name = 'Arial'

    hpe_72k_lff = [
        ("P23863-B21", "HPE 16TB SAS 12G Business Critical 7.2K LFF SC 1-year warranty 512e ISE HDD", "16TB", "7.2K"),
        ("P09153-B21", "HPE 14TB SAS 12G Midline 7.2K LFF SC 1-year warranty Helium 512e DS firmware HDD", "14TB", "7.2K"),
        ("881779-B21", "HPE 12TB SAS 12G Midline 7.2K LFF SC 1-year warranty Helium 512e DS firmware HDD", "12TB", "7.2K"),
        ("857644-B21", "HPE 10TB SAS 12G Midline 7.2K LFF SC 1-year warranty Helium 512e DS firmware HDD", "10TB", "7.2K"),
        ("819201-B21", "HPE 8TB SAS 12G Midline 7.2K LFF SC 1-year warranty 512e DS firmware HDD", "8TB", "7.2K"),
        ("861754-B21", "HPE 6TB SAS 12G Midline 7.2K LFF SC 1-year warranty 512e HDD", "6TB", "7.2K"),
    ]
    create_product_table_with_images(doc, hpe_72k_lff, ["Part No.", "Description", "Capacity", "Speed"])

    doc.add_page_break()

    # Mission Critical SFF BC
    hdd_title5 = doc.add_paragraph()
    run = hdd_title5.add_run("▶ Mission Critical 10K/15K SFF BC")
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.color.rgb = RGBColor(126, 4, 29)
    run.font.name = 'Arial'

    hpe_mc_sff = [
        ("P28352-B21", "HPE 2.4TB SAS 12G mission critical 10K SFF BC 3-year warranty 512e HDD", "2.4TB", "10K"),
        ("P28586-B21", "HPE 1.2TB SAS 12G mission critical 10K SFF BC 3-year warranty HDD", "1.2TB", "10K"),
        ("P28028-B21", "HPE 300GB SAS 12G mission critical 15K SFF BC 3-year warranty HDD", "300GB", "15K"),
        ("P40430-B21", "HPE 300GB SAS 12G mission critical 10K SFF BC 3-year warranty HDD", "300GB", "10K"),
    ]
    create_product_table_with_images(doc, hpe_mc_sff, ["Part No.", "Description", "Capacity", "Speed"])

    # Business Critical 7.2K LFF LP
    hdd_title6 = doc.add_paragraph()
    run = hdd_title6.add_run("▶ Business Critical 7.2K LFF LP (3.5-inch)")
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.color.rgb = RGBColor(126, 4, 29)
    run.font.name = 'Arial'

    hpe_bc_lff = [
        ("P37669-B21", "HPE 18TB SAS 12G business critical 7.2K LFF LP 1-year warranty 512e ISE HDD", "18TB", "7.2K"),
        ("P23608-B21", "HPE 16TB SAS 12G business critical 7.2K LFF LP 1-year warranty 512e ISE HDD", "16TB", "7.2K"),
        ("P09155-B21", "HPE 14TB SAS 12G MDL 7.2K LFF LP 1-year warranty helium 512e Digitally Signed (DS) firmware HDD", "14TB", "7.2K"),
        ("881781-B21", "HPE 12TB SAS 12G MDL 7.2K LFF LP 1-year warranty helium 512e DS firmware HDD", "12TB", "7.2K"),
        ("P09149-B21", "HPE 10TB SAS 12G MDL 7.2K LFF LP 1-year warranty 512e DS firmware HDD", "10TB", "7.2K"),
        ("834031-B21", "HPE 8TB SAS 12G MDL 7.2K LFF LP 1-year warranty 512e DS firmware HDD", "8TB", "7.2K"),
        ("861746-B21", "HPE 6TB SAS 12G MDL 7.2K LFF LP 1-year warranty 512e HDD", "6TB", "7.2K"),
    ]
    create_product_table_with_images(doc, hpe_bc_lff, ["Part No.", "Description", "Capacity", "Speed"])

    doc.add_page_break()

    # ==================== Contact Page ====================
    contact_bg = doc.add_table(rows=1, cols=1)
    contact_bg.alignment = WD_TABLE_ALIGNMENT.CENTER
    bg_cell = contact_bg.cell(0, 0)
    set_cell_shading(bg_cell, CREAM)
    set_no_border(bg_cell)

    para = bg_cell.paragraphs[0]
    para.alignment = WD_ALIGN_PARAGRAPH.CENTER

    para.add_run("\n\n\n")

    title_run = para.add_run("CONTACT US\n")
    title_run.font.size = Pt(28)
    title_run.font.bold = True
    title_run.font.color.rgb = RGBColor(126, 4, 29)
    title_run.font.name = 'Arial'

    line_run = para.add_run("━━━━━━━━━━━━━━━━━━\n\n\n")
    line_run.font.color.rgb = RGBColor(126, 4, 29)

    doc.add_paragraph()

    contact_table = doc.add_table(rows=5, cols=2)
    contact_table.alignment = WD_TABLE_ALIGNMENT.CENTER

    contact_info = [
        ("Phone", "XXX-XXXX-XXXX"),
        ("WhatsApp", "XXX-XXXX-XXXX"),
        ("Email", "example@company.com"),
        ("Website", "www.yourcompany.com"),
        ("Address", "Your Company Address"),
    ]

    for i, (label, value) in enumerate(contact_info):
        cell0 = contact_table.cell(i, 0)
        set_cell_shading(cell0, BURGUNDY)
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
        set_cell_border(cell1, BURGUNDY, "2")
        para1 = cell1.paragraphs[0]
        run1 = para1.add_run("  " + value)
        run1.font.size = Pt(12)
        run1.font.color.rgb = RGBColor(54, 54, 54)
        run1.font.name = 'Arial'

    doc.add_paragraph()

    qr_table = doc.add_table(rows=1, cols=1)
    qr_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    qr_cell = qr_table.cell(0, 0)
    set_cell_shading(qr_cell, CREAM)
    set_cell_border(qr_cell, BURGUNDY, "4")
    qr_para = qr_cell.paragraphs[0]
    qr_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = qr_para.add_run("\n\n[ QR Code ]\n\n")
    run.font.size = Pt(14)
    run.font.color.rgb = RGBColor(126, 4, 29)
    run.font.name = 'Arial'

    # Save
    output_path = "/home/user/-JC-/Product_Catalog_Burgundy.docx"
    doc.save(output_path)
    print(f"✅ Product Catalog created: {output_path}")
    return output_path

if __name__ == "__main__":
    main()
