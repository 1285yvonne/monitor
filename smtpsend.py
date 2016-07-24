#! /usr/bin/env python

import smtplib
import string

class Smtpsent(object):
    
    def __init__(self,SUBJECT,HOST="smtp.163.com",TO="user@user.com",FROM="user@163.com"):
        self.host = HOST
        self.subject = SUBJECT
        self.to = TO
        self.fromwhom = FROM
        self.server = smtplib.SMTP()

    def sendemail(self,text):
        server_conn = self.server
        server_conn.connect(self.host,"25")
        server_conn.starttls()
        server_conn.login(self.fromwhom,"password")

        email_body = string.join((
        "From:%s" % self.fromwhom,
        "To:%s" % self.to,
        "Subject:%s" % self.subject,
        "",
        text),"\r\n")

        server_conn.sendmail(self.fromwhom,[self.to],email_body)

        server_conn.quit()

if __name__=='__main__':
    print 'test'
