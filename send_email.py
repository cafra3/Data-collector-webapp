from email.mime.text import MIMEText
import smtplib

def send_email(email, height, average_height, count):

    from_email=" "
    from_password=" "
    to_email=email

    subject="Height Data"
    message="Hey there, your height is <strong>%s</strong>. <br> Average height of the <strong>%s</strong> recorded heights is <strong>%s</strong>. <br> Thanks for your particpation." % (height, count, average_height)

    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
