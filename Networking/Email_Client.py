import smtplib
from email.mime.text import MIMEText

body = "This is a test message. How are you?"

msg = MIMEText(body)
msg['From'] = "yourmail@gmail.com"
msg['To'] = "yourmail@gmial.com"
msg['Subject'] = "Hello"

server = smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

server.login("yourmail@gmail.com", "Password")

server.send_message(msg)

print("Mail Sent")

server.quit()

'''By Ankush Chavan'''