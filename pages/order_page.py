import allure
from locators.order_site_locators import OrderSiteLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Ввести имя')
    def set_name(self, name):
        self.set_text(OrderSiteLocators.NAME_FIELD, name)


    @allure.step('Ввести фамилию')
    def set_surname(self, surname):
        self.set_text(OrderSiteLocators.SURNAME_FIELD, surname)


    @allure.step('Ввести адрес')
    def set_address(self, address):
        self.set_text(OrderSiteLocators.ADDRESS_FIELD, address)


    @allure.step('Выбрать метро')
    def set_station(self, station):
        self.click_to_element(OrderSiteLocators.METRO_FIELD)
        self.click_to_element(station)


    @allure.step('Выбрать телефон')
    def set_phone(self, phone):
        self.set_text(OrderSiteLocators.PHONE_FIELD, phone)


    @allure.step('Выбрать комментарий')
    def set_comment(self, comment):
        self.set_text(OrderSiteLocators.COMMENTS, comment)


    @allure.step('Нажать на кнопкку "Далее"')
    def click_next_button(self):
        self.click_to_element(OrderSiteLocators.NEXT_BUTTON)


    @allure.step('Выбор даты "Когда привезти самокат"')
    def choice_date(self, date):
        self.click_to_element(OrderSiteLocators.DATE_FIELD)
        self.wait_for_element(date)
        self.click_to_element(date)

    @allure.step('Выбрать количество суток')
    def choice_day(self, day):
        self.click_to_element(OrderSiteLocators.RENT_FIELD)
        self.wait_for_element(day)
        self.click_to_element(day)

    @allure.step('Выбрать цвет')
    def click_colour(self, colour):
        self.click_to_element(colour)

    @allure.step('Нажать кнопку "да"')
    def click_button_yes(self):
        self.click_to_element(OrderSiteLocators.YES_BUTTON)

    @allure.step('Нажать на кнопку "Заказать"')
    def click_order(self):
        self.click_to_element(OrderSiteLocators.ORDER_BUTTON)

    @allure.step('Получить всплывающее окно с номером заказа')
    def get_success_order_text(self):
        return self.get_text(OrderSiteLocators.STATUS_VIEW)

    @allure.step('Заполнить форму с данными пользователя')
    def fill_rent_form(self, name, surname, address, station, phone, date, day, colour, comment):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_station(station)
        self.set_phone(phone)
        self.click_next_button()
        self.choice_date(date)
        self.choice_day(day)
        self.click_colour(colour)
        self.set_comment(comment)
        self.click_order()
        self.click_button_yes()



