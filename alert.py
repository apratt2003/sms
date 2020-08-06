import smtplib
import os

def sendsms(sendto, subjecttxt, bodytxt):
    email = os.environ.get('GMAIL')
    password = os.environ.get('GMAIL_KEY')

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(email, password)
        msg = f'Subject: {subjecttxt}\n\n{bodytxt}'
        smtp.sendmail(email, sendto, msg)

if __name__ == '__main__':
    recipient = os.environ.get('MOBILE')
    sendsms(sendto=recipient, subjecttxt="this is a better subject", bodytxt='this is the body')