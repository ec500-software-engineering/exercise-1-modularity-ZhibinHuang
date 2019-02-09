#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Copyright Zhibin Huang hzhibin@bu.edu 2019#

import smtplib
import email.mime.text

# before sending the email, please set your google account appropriately
# https://support.google.com/mail/answer/7126229?visit_id=636850886287440267-775077852&hl=en&rd=1
# https://support.google.com/accounts/answer/6010255?p=lsa_blocked&hl=en&visit_id=636850859255386124-2120851622&rd=1

# for sending message content and urgency level #
class Message(object):
    def __init__(self, content, urgency):
        self._content = content
        self._urgency = urgency

    def get_msg_content(self):
        return self._content

    def get_urgency(self):
        return self._urgency

# for general information #
class Contact(object):
    def __init__(self, name, sms_info, email_info):
        self._name = name
        self._sms_info = sms_info
        self._email_info = email_info

    def get_name(self):
        return self._name

    def get_email(self):
        return self._email_info

    def get_sms(self):
        return self._sms_info

# function to send google email via SMTP #
def Send_Email(name,content,destination):
    mail_username = 'hzhibin@bu.edu' # your email %%%%%%%%%%%%%%%%%%%%
    mail_password = '*********' # email password  %%%%%%%%%%%%%%%%%%%%
    from_addr = mail_username
    to_addrs = destination

    # HOST & PORT
    HOST = 'smtp.gmail.com'
    PORT = 587

    # Create SMTP Object
    smtp = smtplib.SMTP()
    print('connecting ...')

    # show the debug log
    smtp.set_debuglevel(1)

    # connect
    try:
        print
        smtp.connect(HOST, PORT)
    except:
        print('CONNECT ERROR ****')
    # gmail uses SSL
    smtp.starttls()
    # login with username & password
    try:
        print('loginning ...')
        smtp.login(mail_username, mail_password)
    except:
        print('LOGIN ERROR ****')
    # fill content with MIMEText's object
    msg = email.mime.text.MIMEText(content)
    msg['From'] = from_addr
    msg['To'] = ''.join(to_addrs)
    msg['Subject'] = 'Emergency for ' + name # message subject
    print(msg.as_string())
    smtp.sendmail(from_addr, to_addrs, msg.as_string())
    smtp.quit()

if __name__ == '__main__':
    mes = Message('There is an Emergency, please contact the hospital!',1)
    con = Contact('Kevin','6173318***','hzhibin@bu.edu') # change it to the email you want to sent %%%%%%%%%%%%%%%%%%
    Send_Email(con.get_name(),mes.get_msg_content(),con.get_email())
