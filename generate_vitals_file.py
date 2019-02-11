import random

# moved this to a function so its easier to use


def create_vitals_file(filename):
    afile = open(filename, 'w')
    for x in range(1000):
        # first column: blood pressure (systolic)
        # second column: blood pressure (diastolic)
        # third column: heartbeat per min
        # fourth column: oxygen level (in percentage)
        line = str(random.randint(70, 140)) + "	" + str(random.randint(40, 90)) + "	" + str(
            random.randint(60, 100)) + "	" + str(random.randint(0, 100))
        afile.write(line + "\n")
        afile.close()
