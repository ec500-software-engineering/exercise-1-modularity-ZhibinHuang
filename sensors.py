import time
import sensor
import datetime
from threading import Thread
from common_types import BloodOxygenData, BloodPressureData, BloodPulseData


class SensorReader(Thread):
    '''
    :developer Zeyu Fu
    This is the base class for the individual sensor, describing the basic operations.
    Later we can decide to forgo the base class and just define the derived classes
    :param data_source: object of class BloodPulseData | BloodOxygenData | BloodPressureData;
    :returns: uint32_t value of blood pulse | blood oxygen level | blood pressure
    :raises keyError: raises an exception
    :param display_handler: object of DisplayHandler, defining the display destination
    :returns: void function (Call display function to display updated data)
    :raises keyError: raises an exception
    :param out_queue: queue object from data processor
    :param check_interval: unsigned int value of reading interval (sec)
    :returns: queue object containing new data from sensors
    :raises keyError: raises an exception
    :param Table: database table
    :returns: void function (add new instance to data table)
    :raises keyError: raises an exception
    '''

    def __init__(self, sample_frequency, proc_queue, display_handler):
        super().__init__()
        self._sample_freq = sample_frequency
        self._data_proc_queue = proc_queue
        self._display = display_handler


class BloodOxygenSensorReader(SensorReader):
    '''
    :developer: N/A
    This class decodes read data from a hardware sensor and forwards it the
    realtime data processor for vitals analysis. Additionally
    '''

    def run(self):
        cur_time = old_time = time.time()
        while True:
            if (cur_time - old_time) >= self._sample_freq:
                old_time = cur_time
                oxy_raw = sensor.BloodOxygenSensor.get_blood_oxygen_data()
                oxy_data = BloodOxygenData(
                    oxy_raw,
                    datetime.datetime.now()
                )
                self._data_proc_queue.put(oxy_data, block=False)
                # we would decode and encode here
                self._display.display_blood_oxygen(oxy_raw)
            cur_time = time.time()


class BloodPressureSensorReader(SensorReader):
    '''
    :developer: N/A
    This class decodes read data from a hardware sensor and forwards it the
    realtime data processor for vitals analysis. Additionally
    '''
    def run(self):
        cur_time = old_time = time.time()
        while True:
            if (cur_time - old_time) >= self._sample_freq:
                old_time = cur_time
                raw_data = sensor.BloodPressureSensor.get_blood_pressure_data()
                pressure_data = BloodPressureData(
                    raw_data[0],
                    raw_data[1],
                    datetime.datetime.now()
                )
                self._data_proc_queue.put(pressure_data, block=False)
                self._display.display_blood_pressure(raw_data[0], raw_data[1])
            cur_time = time.time()


class BloodPulseSensorReader(SensorReader):
    '''
    :developer: N/A
    This class decodes read data from a hardware sensor and forwards it the
    realtime data processor for vitals analysis. Additionally
    '''
    def run(self):
        cur_time = old_time = time.time()
        while True:
            if (cur_time - old_time) >= self._sample_freq:
                old_time = cur_time
                pulse_data_raw = sensor.BloodPulseSensor.get_blood_pulse_data()
                pulse_data = BloodPulseData(
                    pulse_data_raw,
                    datetime.datetime.now()
                )
                self._data_proc_queue.put(pulse_data, block=False)
                self._display.display_blood_pulse(pulse_data_raw)
            cur_time = time.time()
