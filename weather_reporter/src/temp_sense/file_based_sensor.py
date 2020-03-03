class FileBasedSensor():
    """Class to read and record the value of a digital sensor such as the DS18B20.

        Reads from a filepath to return the contents of a file on disk that contains the data from the sensor.
    """
    def __init__(self, name, s_type, f_path):
        self.name = name
        self.s_type = s_type
        self.f_path = f_path

    def set_path(self, f_path):
        self.f_path = f_path

    def read_raw_value(self):
        """Reads the raw value of the sensor and returns the lines from the file"""
        with open(self.f_path, 'r') as sensor:
            return sensor.readlines()

    def read_value(self):
        """Reads the value of the sensor
        """
        return ret_val

    def format_data(self, unformatted_data):
        """Formats the data so that it can be saved as a tuple
        """
        # formatted_data = unformatted_data.strftime('%Y-%M-%d %H-%M-%s+0000')
        pass

