# https://github.com/ec500-software-engineering/exercise-1-modularity-mmark9/blob/master/heart_monitor/display.py #

class DisplayHandler(object):

    '''
    :developer: Byoungsui Lee && Seunghee Lee
    This class receives numerical data from sensor readers and
    encodes the data for a display technology
    The displayhandler obejct will take in a object containing the vital data.
    Then it will parse the data into three catagories ( blood oxygen, blood pressure, pulse)
    Each of these parsed data will be the input for the three display methods.
    :param oxy: uint32_t value of blood oxygen level;
    returns: void function ( displays blood oxygen level )
    :raises keyError: raises an exception
    :param systolic: uint32_t value of blood pressure;
    :param diatolic: uint32_t value of blood pressure;
    returns: void function ( displays blood pressure level )
    :raises keyError: raises an exception
    :param pulse: uint32_t value of blood pulse;
    returns: void function ( displays pulselevel )
    :raises keyError: raises an exception
    '''

    def display_blood_oxygen(self, oxy):
        pass

    def display_blood_pressure(self, systolic, diastolic):
        pass

    def display_blood_pulse(self, pulse):
        pass


class TextTerminalDisplay(DisplayHandler):
    '''
    :developer: N/A
    A simple derived class which will print data to the terminal (stdout)
    '''

    def __init__(self):
        self._cur_oxygen = 0
        self._cur_systolic = 0
        self._cur_diastolic = 0
        self._cur_pulse = 0

    def display_blood_oxygen(self, oxy):
        self._cur_oxygen = oxy
        self.display_data()

    def display_blood_pressure(self, systolic, diastolic):
        self._cur_diastolic = diastolic
        self._cur_systolic = systolic
        self.display_data()

    def display_blood_pulse(self, pulse):
        self._cur_pulse = pulse
        self.display_data()

    def display_data(self):
        print(
            (
                '< {} bps HEART RATE > | '
                '< {}/{} SYS/DIA mmHg kPa > | '
                '< {}% Oxygen Saturation >'
            ).format(
                self._cur_pulse,
                self._cur_systolic,
                self._cur_diastolic,
                self._cur_oxygen
            )
        )
