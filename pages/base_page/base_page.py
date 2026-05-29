from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from core.retry_handler import RetryHandler


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_url(self, url):
        self.driver.get(url)

    def get_element(self, locator):
        self.scroll_to_element(locator)
        return self.wait_until_element_should_be_visible(locator)

    def click_element(self, locator):
        try:
            self.wait_until_element_should_be_clickable(locator)
            RetryHandler.execute(lambda: self.get_element(locator).click())
        except NoSuchElementException:
            raise NoSuchElementException(f"Element with locator {locator} not found on the page.")

    def enter_text(self, locator, text):
        self.wait_until_element_should_be_visible(locator)
        self.get_element(locator).send_keys(text)

    def check_if_element_is_visible(self, locator):
        try:
            self.wait_until_element_should_be_visible(locator)
            return self.get_element(locator).is_displayed()
        except TimeoutException:
            raise TimeoutException(f"Element with locator {locator} is not visible within the specified timeout.")
    
    def wait_until_element_should_be_visible(self, locator):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located(locator))
        except TimeoutException:
            raise TimeoutException(f"Element with locator {locator} is not visible within the specified timeout.")

    def wait_until_element_should_be_clickable(self, locator):
        try:
            self.wait.until(expected_conditions.element_to_be_clickable(locator))
        except TimeoutException:
            raise TimeoutException(f"Element with locator {locator} is not clickable within the specified timeout.")

    def scroll_to_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", self.get_element(locator))
    
    def force_click_element(self, locator):
        self.driver.execute_script("arguments[0].click();", self.get_element(locator))

    def create_action_chains(self):
        return ActionChains(self.driver)

    def page_down(self):
        self.create_action_chains().send_keys(Keys.PAGE_DOWN).perform()