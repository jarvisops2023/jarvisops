import os
from st2reactor.sensor.base import Sensor

class LogMonitorSensor(Sensor):
    def setup(self):
        self.log_file_path = '/var/log/my_app.log'

    def run(self, config):
        if os.path.exists(self.log_file_path):
            with open(self.log_file_path, 'r') as log_file:
                for line in log_file:
                    if 'ERROR' in line:
                        self._dispatch_trigger(line.strip())

    def _dispatch_trigger(self, error_message):
        self.sensor_service.dispatch(trigger='my_pack.log_error',
                                     payload={'error_message': error_message})

    def cleanup(self):
        pass
