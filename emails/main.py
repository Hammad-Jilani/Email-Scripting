import openpyxl
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from concurrent.futures import ThreadPoolExecutor
from htmlContent import HtmlContent

path = "C:\\Users\\CoreCom\\Downloads\\final.xlsx"

work = openpyxl.load_workbook(path)
sheet = work.active

gmail_user = ''
gmail_password = ''

def send_email(i):
  email_receiver = sheet.cell(row=i,column=2).value
  
  if email_receiver is not None:
    
    msg = MIMEMultipart('alternative')
    msg['From'] = gmail_user
    msg['To'] = email_receiver
    msg['Subject'] = "TGD'24: TLC's Flagship Event - Don't Miss Out!"
    html_email = HtmlContent()
    msg.attach(MIMEText(html_email,'html'))

    pdf_filename = r'C:\Users\CoreCom\Downloads\tlc.pdf'
    with open(pdf_filename, 'rb') as pdf_file:
      pdf_attachment = MIMEApplication(pdf_file.read(), _subtype='pdf')
      pdf_attachment.add_header('Content-Disposition', f'attachment; filename="TGD details"')
      msg.attach(pdf_attachment)
    
    
    try:
      server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
      server.login(gmail_user, gmail_password)
      server.sendmail(gmail_user, email_receiver, msg.as_string())
      server.close()
      sheet.cell(row=i,column=18).value="Send"
      print(f"Email send to {email_receiver}")
      work.save(path)

    except Exception as e:
      sheet.cell(row=i,column=18).value='Unsend'
      print(e)
      print(f"Did not send to {email_receiver}")
      work.save(path)
    
with ThreadPoolExecutor(max_workers=2) as executor:
    futures = [executor.submit(send_email, i) for i in range(1, sheet.max_row + 1)]