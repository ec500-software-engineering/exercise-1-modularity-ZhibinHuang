import time
import random
import threading
from common_types import SensorDataType
from common_types import Message, MessageUrgency


class RealTimeDataProcessor(threading.Thread):
    def __init__(self, in_queue, notification_man):
        super().__init__()
        self._in_queue = in_queue
        self._notification_man = notification_man

    # Can probably put these functions in a separate class
    @staticmethod
    def blood_pressure_is_normal(pressure_data):
        return 90 <= pressure_data.get_systolic() <= 120 \
               and 60 <= pressure_data.get_diastolic() <= 80

    @staticmethod
    def blood_pulse_is_normal(pulse_data):
        return 60 <= pulse_data.get_pulse() <= 100

    def run(self):
        '''
        In here we need to process data we receive from sensor read queue.
        If any problems are detected in the attached patient's vitals
        we issue a command to the notification manager
        :return:
        '''

        while True:
            incoming_data = self._in_queue.get(block=True)
            if incoming_data.get_type() == SensorDataType.BLOOD_PRESSURE:
                if not RealTimeDataProcessor.blood_pressure_is_normal(incoming_data):
                    self._notification_man.send_message(
                        Message(
                            '!!!! PATIENT ALERT BLOOD PRESSURE ABNORMAL !!!!',
                            MessageUrgency.HIGH_URGENCY
                        )
                    )
            elif incoming_data.get_type() == SensorDataType.BLOOD_PULSE:
                if not RealTimeDataProcessor.blood_pulse_is_normal(incoming_data):
                    self._notification_man.send_message(
                        Message(
                            '!!!! PATIENT ALERT PULSE IS ABNORMAL !!!!',
                            MessageUrgency.HIGH_URGENCY
                        )
                    )
            # yield quantum/time slice for other ready threads
            time.sleep(
                random.randint(1, 3)
            )
