import os
import eventlet
from slack_sdk import WebClient
from st2reactor.sensor.base import Sensor

eventlet.monkey_patch(os=True, select=True, socket=True, thread=True, time=True)

class SlackMessageSensor(Sensor):
    def __init__(self, sensor_service, config=None):
        super(SlackMessageSensor, self).__init__(sensor_service=sensor_service, config=config)
        self._token = self._config.get('xoxb-5789901142679-5817091293057-JTxpNcwf1glsWe1DtOSFEe1d')
        self._client = WebClient(token=self._token)
        self._your_name = self._config.get('Anudeep')  # Your name (e.g., 'John Doe')

    def setup(self):
        self._logger.info('SlackMessageSensor initialized.')

    def poll(self):
        try:
            result = self._client.conversations_history(channel='st2', limit=10)
            messages = result.get('messages', [])

            for message in messages:
                user = message.get('user', 'Unknown')
                text = message.get('text', '')

                # Check if your name is mentioned in the message
                if self._your_name.lower() in text.lower():
                    # Respond to the thread where the message was posted
                    self._respond_to_thread(user, text, message)

        except Exception as e:
            self._logger.error(f'Error polling Slack: {str(e)}')

    def cleanup(self):
        self._logger.info('SlackMessageSensor cleanup.')

    def add_trigger(self, trigger):
        pass

    def update_trigger(self, trigger):
        pass

    def remove_trigger(self, trigger):
        pass

    def _respond_to_thread(self, user, text, message):
        # Extract the thread timestamp
        thread_ts = message.get('thread_ts')

        # Prepare a response message
        response_text = f"Hi {user}! I noticed you mentioned my name in the thread. How can I assist you?"

        # Post the response to the thread
        self._client.chat_postMessage(channel='YOUR_CHANNEL_ID', text=response_text, thread_ts=thread_ts)

    def _dispatch_message_event(self, user, text):
        payload = {
            'user': user,
            'text': text
        }
        self._sensor_service.dispatch(trigger='slack.message', payload=payload)

