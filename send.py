#!/usr/bin/python3

import smtplib
def send(data):
    sender = 'risserver@tj.com'
    receivers = ['your_email@do.com']
    message = """From: From ris server <ris_server@tj.com>
    To: To David <your_email@do.com>
    Subject: GPU

    We got GPU
    """
    message+=data
    try:
       smtpObj = smtplib.SMTP('localhost')
       smtpObj.sendmail(sender, receivers, message)         
       print("Successfully sent email")
    except SMTPException:
       print("Error: unable to send email")
