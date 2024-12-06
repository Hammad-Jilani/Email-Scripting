import pdfkit
from certificate import certificates
import os

def toPDF(name):
  html_content = certificates(name)
  html_file = f"{name}_Letter.html"
  with open(html_file,'w') as f:
    f.write(html_content)

  output = f"{name}_Cartificate.pdf"
  path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
  config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)
  options = {
    'disable-smart-shrinking': '',
    'no-stop-slow-scripts': '',
    'enable-local-file-access': '',
    'disable-javascript': '',
  }
  pdfkit.from_file(html_file,output,configuration=config,options=options)

  return output

