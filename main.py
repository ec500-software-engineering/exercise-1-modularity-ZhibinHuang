#https://github.com/ec500-software-engineering/exercise-1-modularity-mmark9/blob/master/heart_monitor/main_app.py

import display
import sensor_readers
import prediction_engine
import notification_manager
import notifications_sender
import realtime_data_processor
from multiprocessing import Queue
from common_types import Contact
from database import InMemorySimpleDatabase


def main(cmd_args):
    '''
    Entry point of application; in here we spawn the sensor threads, AI thread and
    realtime data processing thread and then wait till we need to quit
    :param cmd_args: dictionary of expected command line arguments
    :return: 0 on success and non-zero on error
    '''
    data_proc_queue = Queue()
    tty = display.TextTerminalDisplay()
    notification_man = notification_manager.FlexibleNotificationManager(
        Contact('Nurse Suzy', None, None, None),
        notifications_sender.MockSMSSender(),
        notifications_sender.MockTelegramSender(),
        notifications_sender.MockEmailSender()
    )
    database = InMemorySimpleDatabase()
    ai_engine = prediction_engine.PredictionEngine(10, notification_man, database)
    pulse_reader = sensor_readers.BloodPulseSensorReader(1, data_proc_queue, tty, database)
    oxy_reader = sensor_readers.BloodOxygenSensorReader(4, data_proc_queue, tty, database)
    pressure_reader = sensor_readers.BloodPressureSensorReader(2, data_proc_queue, tty, database)
    real_time_proc = realtime_data_processor.RealTimeDataProcessor(data_proc_queue, notification_man)
    pulse_reader.start()
    oxy_reader.start()
    pressure_reader.start()
    real_time_proc.start()
    ai_engine.start()
    oxy_reader.join()
    pressure_reader.join()
    pulse_reader.join()
    real_time_proc.join()
    return 0


if __name__ == '__main__':
    main(None)
