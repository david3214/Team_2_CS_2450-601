'''
    Generates pay reports.
'''

from fpdf import FPDF
from tkinter import filedialog
from Employee.Employee import Employee
from Config.fetch_resource import fetch_resource

WIDTH = 210
HEIGHT = 297
MARGIN = 15
BORDER_MARGIN = 10

def set_fonts(pdf, type="header"):
    if type == "header":
        pdf.set_font('Arial', 'B', 40)
        pdf.set_text_color(11,99,116)
    elif type == "heading2":
        pdf.set_font('Arial', 'B', 22)
        pdf.set_text_color(89,145,145)
    elif type == "heading3":
        pdf.set_text_color(11,99,116)
        pdf.set_font('Arial', 'B', 12)
    else:
        pdf.set_text_color(0,0,0)
        pdf.set_font('Arial', '', 13)

def create_heading(pdf, emp):
    pdf.image(str(fetch_resource("./Resources/images/border.png").absolute()), BORDER_MARGIN, MARGIN, WIDTH-(BORDER_MARGIN * 2))

    pdf.ln(MARGIN)
    set_fonts(pdf, "header")
    pdf.cell(WIDTH - (BORDER_MARGIN * 2), 20, "Pay Report", border = 0, ln = 1, align = 'C')
    
    set_fonts(pdf, "heading2")
    pdf.cell(MARGIN)
    pdf.cell(WIDTH - (BORDER_MARGIN * 2), 10, f"Employee: {emp.Name}", 0, 1, 'L')

    set_fonts(pdf, "heading3")
    pdf.cell(MARGIN)
    pdf.cell(WIDTH - (BORDER_MARGIN * 2), 6, f"Employee ID: {emp.EmpID}", 0, 1, 'L')

    pdf.cell(MARGIN)
    pdf.cell(WIDTH - (BORDER_MARGIN * 2), 6, f"Title: {emp.Title}", 0, 1, 'L')

    pdf.cell(MARGIN)
    pdf.cell(WIDTH - (BORDER_MARGIN * 2), 6, f"Department: {emp.Dept}", 0, 1, 'L')

    # Just for spacing
    pdf.cell(MARGIN)
    pdf.cell(WIDTH - (BORDER_MARGIN * 2), 6, f"", 0, 1, 'L')

def create_payment_info(pdf, emp):
    set_fonts(pdf, "")
    cell_width = (WIDTH - (MARGIN * 2 + BORDER_MARGIN * 2)) / 4
    pdf.cell(MARGIN)
    pdf.cell(cell_width, 8, f"Payment Type:", 0, 0, 'L')
    pdf.cell(cell_width, 8, f"{emp.PayMethod}", 0, 0, 'L')
    pdf.cell(cell_width, 8, f"Salary Wage:", 0, 0, 'L')
    pdf.cell(cell_width, 8, f"${'{:.2f}'.format(float(emp.Salary))}", 0, 1, 'L')

    # Bank Info: 433898-4976 Hourly Wage: $50.00
    pdf.cell(MARGIN)
    pdf.cell(cell_width, 8, f"Bank Info:", 0, 0, 'L')
    pdf.cell(cell_width, 8, f"{emp.BankInfo}", 0, 0, 'L')
    pdf.cell(cell_width, 8, f"Hourly Wage:", 0, 0, 'L')
    pdf.cell(cell_width, 8, f"${'{:.2f}'.format(float(emp.Hourly))}", 0, 1, 'L')

    # Route #: 48786143-K Commissions:	25
    pdf.cell(MARGIN)
    pdf.cell(cell_width, 8, f"Route #:", 0, 0, 'L')
    pdf.cell(cell_width, 8, f"{emp.Route}", 0, 0, 'L')
    pdf.cell(cell_width, 8, f"Commissions:", 0, 0, 'L')
    pdf.cell(cell_width, 8, f"{emp.Commission}", 0, 1, 'L')

def generate_pay_report(emp):
    
    pdf = FPDF() # A4 (210 by 297 mm)
    pdf.add_page()
    create_heading(pdf, emp)
    create_payment_info(pdf, emp)
    pdf.image(str(fetch_resource("./Resources/images/employee-image.png").absolute()), 25, 110, WIDTH - (MARGIN * 2 + BORDER_MARGIN * 2))
    
    pdfPath = filedialog.asksaveasfilename(defaultextension = "*.pdf", filetypes = (("PDF Files", "*.pdf"),))
    if pdfPath:
        pdf.output(pdfPath, 'F')
