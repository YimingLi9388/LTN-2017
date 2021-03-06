'''
Created on Aug 30, 2017

@author: Hossein
'''

import os 

MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 587
MAIL_USERNAME = 'ltn.ericsson@gmail.com'

MAIL_PASSWORD = os.environ['MAIL_PASSWORD']

def send_email(data_file_name):
  ''' 
  19.1.14. email: Examples
  https://docs.python.org/3.4/library/email-examples.html
  '''

  import smtplib
  from os.path import basename
  from email.mime.application import MIMEApplication
  from email.mime.multipart import MIMEMultipart
  from email.mime.text import MIMEText 
 
  from_addr = MAIL_USERNAME
  to_addr = ["hossein.seyedmehdi@gmail.com", "hossein.seyedmehdi@ericsson.com"]
  to_addr_str = ''
  for addr in to_addr: 
    to_addr_str += addr + ', '
  msg = MIMEMultipart()
  msg['From'] = from_addr
  msg['To'] = to_addr_str
  msg['Subject'] = "Test email for LTN"
   
  body = "The Email Body"
  msg.attach(MIMEText(body, 'plain'))
  
  #Attach the file 
  with open(data_file_name, "rb") as fil:
    part = MIMEApplication(
        fil.read(),
        Name = basename(data_file_name) )
  # After the file is closed
  part['Content-Disposition'] = 'attachment; filename="%s"' % basename(data_file_name)
  msg.attach(part)
   
  server = smtplib.SMTP(MAIL_SERVER, MAIL_PORT)
  server.starttls()
  server.login(from_addr, MAIL_PASSWORD)
  text = msg.as_string()
  for addr in to_addr:
    server.sendmail(from_addr, addr, text)
  server.quit()
  
  return
  
