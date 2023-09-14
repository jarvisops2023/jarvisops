import time
from st2reactor.sensor.base import Sensor

class MyFileSensor(Sensor):
    def __init__(self, sensor_service, config):
        super(MyFileSensor, self).__init__(sensor_service=sensor_service, config=config)

    def setup(self):
        pass

    def run(self):
        while True:
            with open("/tmp/sensor_input.txt", "r") as file:
                content = file.read()
                if "keyword" in content:
                    self._trigger_keyword_alert(content)
            time.sleep(5)

    def cleanup(self):
        pass

    def _trigger_keyword_alert(self, content):
        payload = {
            "content": content
        }
        self.sensor_service.trigger(trigger="my_trigger.keyword_alert", payload=payload)

def main():
    MyFileSensor().run()

if __name__ == "__main__":
    main()

