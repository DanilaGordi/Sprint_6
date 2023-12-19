import allure
from locators.main_site_locators import MainSiteLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Нажать на лого яндекса')
    def click_logo_yandex(self):
        self.click_to_element(MainSiteLocators.YANDEX_LOGO)

    @allure.step('Нажать на лого самоката')
    def click_logo_scooter(self):
        self.click_to_element(MainSiteLocators.SCOOTER_LOGO)

    @allure.step('Нажать на кнопку согласия куки "да все привыкли"')
    def click_button_cookies(self):
        self.click_to_element(MainSiteLocators.COOKIE_BUTTON)

    @allure.step('Нажать на верхнюю кнопкку "Заказать"')
    def click_order_top(self):
        self.click_to_element(MainSiteLocators.TOP_ORDER_BUTTON)

    @allure.step('Нажать на нижнюю кнопкку "Заказать"')
    def click_order_down(self):
        self.click_to_element(MainSiteLocators.DOWN_ORDER_BUTTON)

    @allure.step('Проскроллить до блока с вопросами о важном')
    def find_questions(self):
        self.scroll_to_element(MainSiteLocators.EIGHTH_QUESTION)
