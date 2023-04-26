import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send_email(user_name, email, reset_code):
    '''
    send_email(user_name, email, reset_code)
    send reset code email
    '''
    # set email host, sender and receiver
    host_name = "smtp.gmail.com"
    host_port = 465
    sender_email = '3900forgenius@gmail.com'
    sender_password = 'forGenius100'
    receivers = [email]

    # set email title and subject
    Title = 'Reset Code Sent!'
    subject = 'Here is your Reset Code ' + reset_code

    # set email message info
    message = MIMEText(subject, 'plain', 'utf-8')
    message['From'] = Header("3900forGenius", 'utf-8')
    message['To'] = Header(user_name, 'utf-8')
    message['Subject'] = Header(Title, 'utf-8')

    # send email
    server = smtplib.SMTP_SSL(host_name, host_port)
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receivers, message.as_string())
    server.quit()


def send_email_register(user_name, email, reset_code):
    '''
    send_email_register(user_name, email, reset_code)
    send registration code email
    '''
    # set email host, sender and receiver
    host_name = "smtp.gmail.com"
    host_port = 465
    sender_email = '3900forgenius@gmail.com'
    sender_password = 'forGenius100'
    receivers = [email]

    # set email title and subject
    Title = 'Registration Code Sent!'
    subject = 'Here is your Registration Code ' + reset_code

    # set email message info
    message = MIMEText(subject, 'plain', 'utf-8')
    message['From'] = Header("3900forGenius", 'utf-8')
    message['To'] = Header(user_name, 'utf-8')
    message['Subject'] = Header(Title, 'utf-8')

    # send email
    server = smtplib.SMTP_SSL(host_name, host_port)
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receivers, message.as_string())
    server.quit()


def send_email_share(user_name, email, data, receiver):
    '''
    send_email_share(user_name, email, data, receiver)
    send share order email
    '''
    # set email host, sender and receiver
    host_name = "smtp.gmail.com"
    host_port = 465
    sender_email = '3900forgenius@gmail.com'
    sender_password = 'forGenius100'
    receivers = [email]

    # set email title and subject
    Title = user_name + ' Share order to you'
    subject = data

    # set email message info
    message = MIMEText(subject, 'html', 'utf-8')
    message['From'] = Header(user_name, 'utf-8')
    message['To'] = Header(receiver, 'utf-8')
    message['Subject'] = Header(Title, 'utf-8')

    # send email
    server = smtplib.SMTP_SSL(host_name, host_port)
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receivers, message.as_string())
    server.quit()
