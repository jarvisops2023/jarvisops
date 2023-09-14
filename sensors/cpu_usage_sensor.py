import psutil
from st2reactor.sensor.base import Sensor

class CPUSensor(Sensor):
    def __init__(self, sensor_service, config):
        super(CPUSensor, self).__init__(sensor_service=sensor_service, config=config)
        self._sensor_name = "linux_vm.cpu_sensor"
        self._threshold = int(config.get("threshold", 80))
        
    def setup(self):
        pass

    def run(self):
        while True:
            cpu_usage = psutil.cpu_percent(interval=5)
            if cpu_usage > self._threshold:
                payload = {"cpu_usage": cpu_usage}
                self.sensor_service.dispatch(trigger=self._sensor_name, payload=payload)

