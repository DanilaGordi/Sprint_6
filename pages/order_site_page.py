import allure
from locators.order_site_locators import OrderSiteLocators



class OrderPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажать на поле "Когда привезти самокат"')
    def click_when_to_bring(self):
        self.driver.find_element(*OrderSiteLocators.DATE_FIELD).click()

    @allure.step('Первый выбор даты')
    def choice_dec_20th(self):
        self.driver.find_element(*OrderSiteLocators.DATE_FIELD).click()
        self.driver.find_element(*OrderSiteLocators.DATE_1).click()

    @allure.step('Второй выбор даты')
    def choice_dec_25th(self):
        self.driver.find_element(*OrderSiteLocators.DATE_FIELD).click()
        self.driver.find_element(*OrderSiteLocators.DATE_2).click()
    @allure.step('Нажать на поле срока аренды')
    def click_rental_period(self):
        self.driver.find_element(*OrderSiteLocators.RENT_FIELD).click()

    @allure.step('Выбрать сутки')
    def choice_one_day(self):
        self.driver.find_element(*OrderSiteLocators.RENT_FIELD).click()
        self.driver.find_element(*OrderSiteLocators.RENT_FIELD_1).click()

    @allure.step('Выбрать трое суток')
    def choice_three_day(self):
        self.driver.find_element(*OrderSiteLocators.RENT_FIELD).click()
        self.driver.find_element(*OrderSiteLocators.RENT_FIELD_2).click()
    @allure.step('Выбор цвета жемчуг')
    def click_black_color(self):
        self.driver.find_element(*OrderSiteLocators.BLACK_COLOR).click()

    @allure.step('Выбор цвета безысходность')
    def click_grey_color(self):
        self.driver.find_element(*OrderSiteLocators.GREY_COLOR).click()

    @allure.step('Нажать кнопку "да"')
    def click_button_yes(self):
        self.driver.find_element(*OrderSiteLocators.YES_BUTTON).click()

    @allure.step('Нажать на кнопку "Заказать"')
    def click_order(self):
        self.driver.find_element(*OrderSiteLocators.ORDER_BUTTON).click()

    @allure.step('Получить всплывающее окно с номером заказа')
    def get_success_order_text(self):
        return self.driver.find_element(*OrderSiteLocators.STATUS_VIEW).text



