from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(locator)

    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    def click_to_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def get_text(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator)).text

    def set_text(self, locator, text):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).send_keys(text)

    def scroll_to_element(self, locator):
        element = self.wait_for_element(locator)
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_for_site(self, url):
        WebDriverWait(self.driver, 5).until(expected_conditions.url_to_be(url))

    def get_site(self):
        return self.driver.current_url

    def switch_to_window(self):
        return self.driver.switch_to.window(self.driver.window_handles[-1])

