from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class DriverManager:

    @staticmethod
    def get_driver(browser_name="chrome", headless=False):

        if browser_name.lower() == "chrome":
            options = ChromeOptions()

            if headless:
                options.add_argument("--headless=new")
            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")

            driver = webdriver.Chrome(options=options)
        elif browser_name.lower() == "firefox":
            options = FirefoxOptions()

            if headless:
                options.add_argument("--headless")
            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")

            driver = webdriver.Firefox(options=options)
        else:
            raise Exception(f"Unsupported browser: {browser_name}")

        return driver
