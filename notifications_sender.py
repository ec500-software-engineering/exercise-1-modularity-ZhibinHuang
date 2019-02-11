# https://github.com/mmark9/ec500_spring19_misc/blob/develop/heart_monitor/notifications_sender.py #

import smtplib, ssl
import settings
from twilio.rest import Client


class NotificationSender(object):
    '''
    :developer Naelle
    Base class that defines shared attributes, methods
    :param message: object_instance of Message class containing message content and urgency
    :param recipient: string value of recipients number/email from Contact class
    returns: void function (sends message)
    :raises keyError: raises an exception
    '''

    def send_notification(self, message, recipient):
        pass


# We can define the individual notification senders in more detail later if needed
class MockSMSSender(NotificationSender):
    '''
    :param message: object_instance of Contact class
    returns: string with sms destination number
    :raises keyError: raises an exception
    '''

    def get_cell_number(self):
        pass

    def send_notification(self, message, recipient):
        print(
            'sms> TO: {}\n\t\t{}'.format(
                recipient.get_name(), message.get_msg_content())
        )


class MockEmailSender(NotificationSender):
    '''
    :param message: object_instance of Contact class
    returns: string with email destination
    :raises keyError: raises an exception
    '''

    def get_email(self):
        pass

    def send_notification(self, message, recipient):

        print(
            'email> TO: {}\n\t\t{}'.format(
                recipient.get_name(), message.get_msg_content())
        )
    


class MockTelegramSender(NotificationSender):
    '''
    :param message: object_instance of Contact class;
    returns: string with telegraph destination number
    :raises keyError: raises an exception
    '''



    def get_telegram_id(self):
        pass

    def send_notification(self, message, recipient):
        print(
            'telegram>> BOT > TO: {}\n\t\t{}'.format(
                recipient.get_name(), message.get_msg_content())
        )

        port = 587  # For starttls
        smtp_server = "smtp.gmail.com"
        message = """\
        Subject: Hi there
        This message is sent from alert."""

        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(settings.sender_email, settings.password)
            server.sendmail(settings.sender_email, settings.receiver_email, settings.message)

        account_sid = ''
        auth_token = ''
        client = Client(account_sid, auth_token)

        message = client.messages \
                .create(
                     body="Alert Message from the patient",
                     from_='+16176069471',
                     to= '+1'+settings.phone
                 )

        print(message.sid)
