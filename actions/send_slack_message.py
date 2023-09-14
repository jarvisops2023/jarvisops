from st2common.runners.base_action import Action
import requests
import json

class SendSlackMessageAction(Action):
    def run(self, webhook_url, message):
        payload = {"text": message}
        headers = {"Content-Type": "application/json"}
        
        response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
        
        if response.status_code == 200:
            return True, "Message sent successfully"
        else:
            return False, f"Failed to send message: {response.status_code} - {response.text}"

