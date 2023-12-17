import allure
from data import SiteOrderDaniil
from data import SiteOrderElse
from locators.order_site_locators import OrderSiteLocators



class OwnerPage:

    def __init__(self, driver):
        self.driver = driver


    @allure.step('Ввести первое имя')
    def set_name_1(self):
        self.driver.find_element(*OrderSiteLocators.NAME_FIELD).send_keys(SiteOrderDaniil.name)

    @allure.step('Ввести второе имя')
    def set_name_2(self):
        self.driver.find_element(*OrderSiteLocators.NAME_FIELD).send_keys(SiteOrderElse.name)

    @allure.step('Ввести первую фамилию')
    def set_surname_1(self):
        self.driver.find_element(*OrderSiteLocators.SURNAME_FIELD).send_keys(SiteOrderDaniil.surname)

    @allure.step('Ввести вторую фамилию')
    def set_surname_2(self):
        self.driver.find_element(*OrderSiteLocators.SURNAME_FIELD).send_keys(SiteOrderElse.surname)

    @allure.step('Ввести первый адрес')
    def set_address_1(self):
        self.driver.find_element(*OrderSiteLocators.ADDRESS_FIELD).send_keys(SiteOrderDaniil.address)

    @allure.step('Ввести второй адрес')
    def set_address_2(self):
        self.driver.find_element(*OrderSiteLocators.ADDRESS_FIELD).send_keys(SiteOrderElse.address)

    @allure.step('Выбрать первое метро')
    def set_station_university(self):
        self.driver.find_element(*OrderSiteLocators.METRO_FIELD).click()
        self.driver.find_element(*OrderSiteLocators.METRO_UNIVERSITY).click()

    @allure.step('Выбрать второе метро')
    def set_station_dinamo(self):
        self.driver.find_element(*OrderSiteLocators.METRO_FIELD).click()
        self.driver.find_element(*OrderSiteLocators.METRO_DINAMO).click()

    @allure.step('Выбрать первый телефон')
    def set_phone_1(self):
        self.driver.find_element(*OrderSiteLocators.PHONE_FIELD).send_keys(SiteOrderDaniil.phone)

    @allure.step('Выбрать второй телефон')
    def set_phone_2(self):
        self.driver.find_element(*OrderSiteLocators.PHONE_FIELD).send_keys(SiteOrderElse.phone)


    @allure.step('Выбрать первый комментарий')
    def set_comment_1(self):
        self.driver.find_element(*OrderSiteLocators.COMMENTS).send_keys(SiteOrderDaniil.comment)

    @allure.step('Выбрать второй комментарий')
    def set_comment_2(self):
        self.driver.find_element(*OrderSiteLocators.COMMENTS).send_keys(SiteOrderElse.comment)


    @allure.step('Нажать на кнопкку "Далее"')
    def click_next_button(self):
        self.driver.find_element(*OrderSiteLocators.NEXT_BUTTON).click()

