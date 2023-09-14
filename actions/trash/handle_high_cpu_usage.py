from st2common.runners.base_action import Action

class HandleHighCPUUsageAction(Action):
    def run(self, cpu_usage):
        message = f"High CPU usage detected: {cpu_usage}%"
        self.logger.info(message)
        # You can add more logic here, such as sending notifications or taking remediation actions
        return message

