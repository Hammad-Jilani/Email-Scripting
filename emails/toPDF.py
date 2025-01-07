import pdfkit
from certificate import certificates
from PyPDF2 import PdfReader, PdfWriter
import os

def rotate_pdf_to_portrait(input_pdf, output_pdf):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for page in reader.pages:
        page.rotate(0)
        writer.add_page(page)

    with open(output_pdf, "wb") as f:
        writer.write(f)

def toPDF(name):
    html_content = certificates(name)
    html_file = f"{name}_Letter.html"

    with open(html_file, 'w') as f:
        f.write(html_content)

    output = f"{name}_Certificate.pdf"
    
    path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)
    
    options = {
        'page-size': 'A4',  
        'orientation': 'landscape', 
        'disable-smart-shrinking': '',
        'no-stop-slow-scripts': '',
        'enable-local-file-access': '',
        'disable-javascript': '',
    }

    pdfkit.from_file(html_file, output, configuration=config, options=options)

    rotated_output = f"{name}_Certificate_.pdf"
    rotate_pdf_to_portrait(output, rotated_output)

    os.remove(output)

    return rotated_output
