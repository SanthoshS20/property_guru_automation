import os, constants
from datetime import datetime

class ScreenshotUtils:

    @staticmethod
    def capture(driver):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        screenshot_path = os.path.join(
            constants.SCREENSHOTS_DIR,
            f"screenshot_{timestamp}.png"
        )
        driver.save_screenshot(screenshot_path)

        return screenshot_path