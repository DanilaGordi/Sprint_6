import allure
from locators.main_site_locators import MainSiteLocators



class MainPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажать на лого яндекса')
    def click_logo_yandex(self):
        self.driver.find_element(*MainSiteLocators.YANDEX_LOGO).click()

    @allure.step('Нажать на лого самоката')
    def click_logo_scooter(self):
        self.driver.find_element(*MainSiteLocators.SCOOTER_LOGO).click()

    @allure.step('Нажать на кнопку согласия куки "да все привыкли"')
    def click_button_cookies(self):
        self.driver.find_element(*MainSiteLocators.COOKIE_BUTTON).click()

    @allure.step('Нажать на верхнюю кнопкку "Заказать"')
    def click_order_top(self):
        self.driver.find_element(*MainSiteLocators.TOP_ORDER_BUTTON).click()

    @allure.step('Нажать на нижнюю кнопкку "Заказать"')
    def click_order_down(self):
        self.driver.find_element(*MainSiteLocators.DOWN_ORDER_BUTTON).click()

    @allure.step('Проскроллить до блока с вопросами о важном')
    def find_questions(self):
        element = self.driver.find_element(*MainSiteLocators.EIGHTH_QUESTION)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)