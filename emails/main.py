import openpyxl
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from concurrent.futures import ThreadPoolExecutor
from htmlContent import HtmlContent
from confirmation import confirmation
from qawwali import qawwali
from huzaifa import delegates
from last import last
from allotments import allotments
from allotment2 import allotment2
from toPDF import toPDF
path = "C:\\Users\\CoreCom\\Downloads\\final.xlsx"

work = openpyxl.load_workbook(path)
sheet = work.active

gmail_user = 'hjilani15@gmail.com'
gmail_password = 'sefs sffw mksu chca'

def send_email(i):
  gmail_receiver = sheet.cell(row=i,column=1).value
  
  if gmail_receiver is not None:
    name = sheet.cell(row=i,column=2).value
    # committee = sheet.cell(row=i,column=2).value
    # allotment = sheet.cell(row=i,column=3).value
    msg = MIMEMultipart('alternative')
    msg['From'] = gmail_user
    msg['To'] = gmail_receiver
    # msg['Subject'] = "TGD'24: TLC's Flagship Event - Don't Miss Out!"
    # msg['Subject'] = "Confirmation: Grand Debate Participation"
    msg['Subject'] ="Allotment Details for The Grand Debate'24"

    # msg['Subject'] = "Payment Verification Confirmed - Collect TGD Qawali Pass"
    # msg['Subject'] ="Invitation to Participate in The Grand Debate - A Premier MUN-Style Competition"

    # html_email = confirmation(sheet.cell(row=i,column=1).value)
    # html_email = qawwali(sheet.cell(row=i,column=1).value)
    # html_email = delegates(sheet.cell(row=i,column=3).value)
    # msg['Subject']= "The Grand Debate Invitation"
    # html_email = last()
    # html_email=allotment2(name,committee,allotment)
    # msg.attach(MIMEText(html_email,'html'))

    # pdf_filename = r"C:\Users\CoreCom\Downloads\The Grand Debate '24.pdf"
    # with open(pdf_filename, 'rb') as pdf_file:
    #   pdf_attachment = MIMEApplication(pdf_file.read(), _subtype='pdf')
    #   pdf_attachment.add_header('Content-Disposition', f'attachment; filename="The Grand Debate 24"')
    #   msg.attach(pdf_attachment)


    output = toPDF(name)

    with open(output, 'rb') as file:
      attach = MIMEApplication(file.read(), _subtype='pdf')
      attach.add_header('Content-Disposition', 'attachment', filename=output)
      msg.attach(attach)
    
    try:
      server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
      server.login(gmail_user, gmail_password)
      server.sendmail(gmail_user, gmail_receiver, msg.as_string())
      server.close()
      sheet.cell(row=i,column=4).value="Send"
      
      print(f"Email send to {gmail_receiver}")
      work.save(path)

    except Exception as e:
      sheet.cell(row=i,column=4).value='Unsend'
      print(e)
      print(f"Did not send to {gmail_receiver}")
      work.save(path)
    
with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(send_email, i) for i in range(1, sheet.max_row + 1)]