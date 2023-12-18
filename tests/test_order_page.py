import allure
from conftest import driver
from locators.order_site_locators import OrderSiteLocators
from data import SiteOrderDaniil
from data import SiteOrderElse
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderScooter:

    @allure.title('Проверка заказа через верхнюю кнопку "Заказать"')
    @allure.description('Заказываем самокат через верхнюю кнопку "Заказать" при помощи данных из первого набора, и проверяем, что заказ сформирован')
    def test_order_one(self, driver):
        MainPage(driver).click_button_cookies()
        MainPage(driver).click_order_top()
        OrderPage(driver).fill_rent_form(SiteOrderDaniil.name,
                                       SiteOrderDaniil.surname,
                                       SiteOrderDaniil.address,
                                       OrderSiteLocators.METRO_UNIVERSITY,
                                       SiteOrderDaniil.phone,
                                       OrderSiteLocators.DATE_1,
                                       OrderSiteLocators.RENT_FIELD_1,
                                       OrderSiteLocators.BLACK_COLOR,
                                       SiteOrderDaniil.comment)
        assert 'Заказ оформлен' in OrderPage(driver).get_success_order_text()

    @allure.title('Проверка заказа через нижнюю кнопку "Заказать"')
    @allure.description('Заказываем самокат через нижнюю кнопку "Заказать" при помощи данных из второго набора, и проверяем, что заказ сформирован')
    def test_order_two(self, driver):
        MainPage(driver).click_button_cookies()
        MainPage(driver).click_order_top()
        OrderPage(driver).fill_rent_form(SiteOrderElse.name,
                                       SiteOrderElse.surname,
                                       SiteOrderElse.address,
                                       OrderSiteLocators.METRO_DINAMO,
                                       SiteOrderElse.phone,
                                       OrderSiteLocators.DATE_2,
                                       OrderSiteLocators.RENT_FIELD_2,
                                       OrderSiteLocators.GREY_COLOR,
                                       SiteOrderElse.comment)
        assert 'Заказ оформлен' in OrderPage(driver).get_success_order_text()
