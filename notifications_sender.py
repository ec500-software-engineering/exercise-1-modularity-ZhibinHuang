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
