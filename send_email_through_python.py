import smtplib
server=smtplib.SMTP ('smtp.gmail.com',587)
server.starttls()
server.login('enter your gmail_username','enter the gmail_passkey')
server.sendmail('to whom you wanna send','hello brother')
print('mailsent')