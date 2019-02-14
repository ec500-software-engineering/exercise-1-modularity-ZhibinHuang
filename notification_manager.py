from common_types import MessageUrgency


class NotificationManager(object):
    """
    :developer: Josh
    This class uses urgency to dictate which messaging mediums get used
        LOW_URGENCY = 0
        MEDIUM_URGENCY = 1
        HIGH_URGENCY = 2
    """

    def __init__(self, main_contact):
        self._main_contact = main_contact

    def send_message(self, msg):
        raise NotImplementedError


class FlexibleNotificationManager(NotificationManager):

    def __init__(self, main_contact, sms_sender, telegram_sender, email_sender):
        super().__init__(main_contact)
        self._sms_sender = sms_sender
        self._telegram_sender = telegram_sender
        self._email_sender = email_sender

    def send_message(self, msg):
        if msg.get_urgency() == MessageUrgency.HIGH_URGENCY:
            self._sms_sender.send_notification(msg, self._main_contact)
            self._telegram_sender.send_notification(msg, self._main_contact)
        elif msg.get_urgency() == MessageUrgency.MEDIUM_URGENCY:
            self._telegram_sender.send_notification(msg, self._main_contact)
        elif msg.get_urgency() == MessageUrgency.LOW_URGENCY:
            self._email_sender.send_notification(msg, self._main_contact)
