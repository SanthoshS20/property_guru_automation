import time

class RetryHandler:

    @staticmethod
    def execute(action, retries=3, delay=2):
        for attempt in range(retries):
            try:
                return action()
            except Exception:
                if attempt == retries - 1:
                    raise
                time.sleep(delay)