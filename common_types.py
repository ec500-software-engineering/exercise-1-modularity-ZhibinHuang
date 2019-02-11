from enum import Enum


'''
The idea is that urgency can help the notification manager decide what
messaging medium is the most appropriate or if a message calls for multiple
mediums to be used
'''


class MessageUrgency(Enum):
    LOW_URGENCY = 0
    MEDIUM_URGENCY = 1
    HIGH_URGENCY = 2


class SensorDataType(Enum):
    BLOOD_OXYGEN = 0
    BLOOD_PULSE = 1
    BLOOD_PRESSURE = 2


class Message(object):
    def __init__(self, content, urgency):
        self._content = content
        self._urgency = urgency

    def get_msg_content(self):
        return self._content

    def get_urgency(self):
        return self._urgency


class RawData(object):
    def __init__(self, timestamp, data_type):
        self._timestamp = timestamp
        self._data_type = data_type

    def get_type(self):
        return self._data_type

    def get_timestamp(self):
        return self._timestamp


class BloodPulseData(RawData):
    def __init__(self, pulse, timestamp):
        super().__init__(timestamp, SensorDataType.BLOOD_PULSE)
        self._pulse = pulse

    def get_pulse(self):
        return self._pulse


class BloodOxygenData(RawData):
    def __init__(self, oxy_level, timestamp):
        super().__init__(timestamp, SensorDataType.BLOOD_OXYGEN)
        self._oxy_level = oxy_level

    def get_oxy(self):
        return self._oxy_level


class BloodPressureData(RawData):
    def __init__(self, systolic, diastolic, timestamp):
        super().__init__(timestamp, SensorDataType.BLOOD_PRESSURE)
        self._systolic = systolic
        self._diastolic = diastolic

    def get_systolic(self):
        return self._systolic

    def get_diastolic(self):
        return self._diastolic


class QueueSensorData(object):

    def __init__(self, sensor_data, data_type):
        self._sensor_data = sensor_data
        self._data_type = data_type

    def get_sensor_data(self):
        return self._sensor_data

    def get_sensor_type(self):
        return self._sensor_data


class Contact(object):
    def __init__(self, name, sms_info, telegram_info, email_info):
        self._name = name
        self._sms_info = sms_info
        self._telegram_info = telegram_info
        self._email_info = email_info

    def get_name(self):
        return self._name

    def get_telegram(self):
        return self._telegram_info

    def get_sms(self):
        return self._sms_info

    def get_email_info(self):
        return self._email_info
