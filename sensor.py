import random

'''
These classes model drivers that provide discrete readings of hardware
'''


class BloodPressureSensor(object):
    @staticmethod
    def get_blood_pressure_data():
        '''
        Credit to eunghee@bu.edu
        :return:
        '''
        return random.randint(70, 140), random.randint(40, 90)


class BloodPulseSensor(object):

    @staticmethod
    def get_blood_pulse_data():
        '''
        Credit to eunghee@bu.edu
        :return:
        '''
        return random.randint(49, 111)


class BloodOxygenSensor(object):

    @staticmethod
    def get_blood_oxygen_data():
        '''
        Credit to eunghee@bu.edu
        :return:
        '''
        return random.randint(0, 100)
