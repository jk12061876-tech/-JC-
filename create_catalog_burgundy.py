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
        ("P00924-B21", "HPE 32GB DDR4-2933", "32GB", "DDR4-2933"),
        ("815100-B21", "HPE 32GB DDR4-2666", "32GB", "DDR4-2666"),
        ("P00930-B21", "HPE 64GB DDR4-2933", "64GB", "DDR4-2933"),
        ("P00926-B21", "HPE 64GB DDR4-2933 LR", "64GB", "DDR4-2933"),
        ("P11040-B21", "HPE 128GB DDR4-2933", "128GB", "DDR4-2933"),
        ("P00928-B21", "HPE 128GB DDR4-2933 3DS", "128GB", "DDR4-2933"),
    ]
    create_product_table_with_images(doc, hpe_g10_products, ["Part No.", "Description", "Capacity", "Spec"])

    g10plus_title = doc.add_paragraph()
    run = g10plus_title.add_run("▶ G10+ Series Memory")
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.color.rgb = RGBColor(126, 4, 29)
    run.font.name = 'Arial'

    hpe_g10plus_products = [
        ("P06033-B21", "HPE 32GB DDR4-3200", "32GB", "DDR4-3200"),
        ("P06035-B21", "HPE 64GB DDR4-3200", "64GB", "DDR4-3200"),
        ("P40007-B21", "HPE 32GB DDR4-3200 SR", "32GB", "DDR4-3200"),
        ("P06037-B21", "HPE 128GB DDR4-3200", "128GB", "DDR4-3200"),
        ("P06039-B21", "HPE 256GB DDR4-3200", "256GB", "DDR4-3200"),
    ]
    create_product_table_with_images(doc, hpe_g10plus_products, ["Part No.", "Description", "Capacity", "Spec"])

    g11_title = doc.add_paragraph()
    run = g11_title.add_run("▶ G11 Series Memory (DDR5)")
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.color.rgb = RGBColor(126, 4, 29)
    run.font.name = 'Arial'

    hpe_g11_products = [
        ("P64705-B21", "HPE 16GB DDR5-5600", "16GB", "DDR5-5600"),
        ("P64706-B21", "HPE 32GB DDR5-5600", "32GB", "DDR5-5600"),
        ("P64707-B21", "HPE 64GB DDR5-5600", "64GB", "DDR5-5600"),
        ("P64708-B21", "HPE 96GB DDR5-5600", "96GB", "DDR5-5600"),
        ("P64709-B21", "HPE 128GB DDR5-5600", "128GB", "DDR5-5600"),
        ("P43322-B21", "HPE 16GB DDR5-4800", "16GB", "DDR5-4800"),
        ("P43328-B21", "HPE 32GB DDR5-4800", "32GB", "DDR5-4800"),
        ("P43331-B21", "HPE 64GB DDR5-4800", "64GB", "DDR5-4800"),
        ("P43334-B21", "HPE 128GB DDR5-4800", "128GB", "DDR5-4800"),
        ("P43337-B21", "HPE 256GB DDR5-4800", "256GB", "DDR5-4800"),
    ]
    create_product_table_with_images(doc, hpe_g11_products, ["Part No.", "Description", "Capacity", "Spec"])

    doc.add_page_break()

    # ==================== Dell Server Memory ====================
    create_product_section_header(doc, "DELL SERVER MEMORY", "DDR4/DDR5 Series")

    dell_products = [
        ("AA601616", "Dell 32GB DDR4-2933", "32GB", "DDR4-2933"),
        ("AA601615", "Dell 64GB DDR4-2933", "64GB", "DDR4-2933"),
        ("AA783422", "Dell 32GB DDR4-3200", "32GB", "DDR4-3200"),
        ("AA783423", "Dell 64GB DDR4-3200", "64GB", "DDR4-3200"),
        ("AB445285", "Dell 128GB DDR4-3200", "128GB", "DDR4-3200"),
        ("AC239377", "Dell 16GB DDR5-4800", "16GB", "DDR5-4800"),
        ("AC239378", "Dell 32GB DDR5-4800", "32GB", "DDR5-4800"),
        ("AC239379", "Dell 64GB DDR5-4800", "64GB", "DDR5-4800"),
        ("AC830716", "Dell 16GB DDR5-5600", "16GB", "DDR5-5600"),
        ("AC830717", "Dell 32GB DDR5-5600", "32GB", "DDR5-5600"),
        ("AC830718", "Dell 64GB DDR5-5600", "64GB", "DDR5-5600"),
    ]
    create_product_table_with_images(doc, dell_products, ["Part No.", "Description", "Capacity", "Spec"])

    doc.add_page_break()

    # ==================== Lenovo Server Memory ====================
    create_product_section_header(doc, "LENOVO SERVER MEMORY", "ThinkSystem Series")

    lenovo_products = [
        ("4ZC7A08707", "Lenovo 16GB DDR4-2933", "16GB", "DDR4-2933"),
        ("4ZC7A08709", "Lenovo 32GB DDR4-2933", "32GB", "DDR4-2933"),
        ("4ZC7A08710", "Lenovo 64GB DDR4-2933", "64GB", "DDR4-2933"),
        ("4X77A08634", "Lenovo 32GB DDR4-3200", "32GB", "DDR4-3200"),
        ("4ZC7A15124", "Lenovo 64GB DDR4-3200", "64GB", "DDR4-3200"),
        ("4X77A85511", "Lenovo 16GB DDR5-4800", "16GB", "DDR5-4800"),
        ("4X77A77483", "Lenovo 32GB DDR5-4800", "32GB", "DDR5-4800"),
        ("4X77A77033", "Lenovo 64GB DDR5-4800", "64GB", "DDR5-4800"),
        ("4X77A77034", "Lenovo 128GB DDR5-4800", "128GB", "DDR5-4800"),
        ("4X77A88049", "Lenovo 32GB DDR5-5600", "32GB", "DDR5-5600"),
        ("4X77A88052", "Lenovo 64GB DDR5-5600", "64GB", "DDR5-5600"),
        ("4X77A88054", "Lenovo 128GB DDR5-5600", "128GB", "DDR5-5600"),
    ]
    create_product_table_with_images(doc, lenovo_products, ["Part No.", "Description", "Capacity", "Spec"])

    doc.add_page_break()

    # ==================== HPE Enterprise HDD ====================
    create_product_section_header(doc, "HPE ENTERPRISE HDD", "SAS HDD Series")

    hdd_title = doc.add_paragraph()
    run = hdd_title.add_run("▶ Enterprise 10K/15K SAS HDD")
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.color.rgb = RGBColor(126, 4, 29)
    run.font.name = 'Arial'

    hpe_hdd = [
        ("881457-B21", "HPE 2.4TB SAS 10K SFF", "2.4TB", "10K"),
        ("872481-B21", "HPE 1.8TB SAS 10K SFF", "1.8TB", "10K"),
        ("872479-B21", "HPE 1.2TB SAS 10K SFF", "1.2TB", "10K"),
        ("870759-B21", "HPE 900GB SAS 15K SFF", "900GB", "15K"),
        ("870757-B21", "HPE 600GB SAS 15K SFF", "600GB", "15K"),
        ("870753-B21", "HPE 300GB SAS 15K SFF", "300GB", "15K"),
    ]
    create_product_table_with_images(doc, hpe_hdd, ["Part No.", "Description", "Capacity", "Speed"])

    midline_title = doc.add_paragraph()
    run = midline_title.add_run("▶ Midline 7.2K SAS HDD")
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.color.rgb = RGBColor(126, 4, 29)
    run.font.name = 'Arial'

    hpe_midline = [
        ("P23863-B21", "HPE 16TB SAS 7.2K LFF", "16TB", "7.2K"),
        ("P09153-B21", "HPE 14TB SAS 7.2K LFF", "14TB", "7.2K"),
        ("881779-B21", "HPE 12TB SAS 7.2K LFF", "12TB", "7.2K"),
        ("857644-B21", "HPE 10TB SAS 7.2K LFF", "10TB", "7.2K"),
        ("819201-B21", "HPE 8TB SAS 7.2K LFF", "8TB", "7.2K"),
        ("861754-B21", "HPE 6TB SAS 7.2K LFF", "6TB", "7.2K"),
    ]
    create_product_table_with_images(doc, hpe_midline, ["Part No.", "Description", "Capacity", "Speed"])

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
