import allure
from conftest import driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators.order_site_locators import OrderSiteLocators
from pages.main_site_page import MainPage
from pages.owner_site_page import OwnerPage
from pages.order_site_page import OrderPage


class TestOrderScooter:

    @allure.title('Проверка заказа через верхнюю кнопку "Заказать"')
    @allure.description('Заказываем самокат через верхнюю кнопку "Заказать" при помощи данных из первого набора, и проверяем, что заказ сформирован')
    def test_order_one(self, driver):
        MainPage(driver).click_button_cookies()
        MainPage(driver).click_order_top()
        OwnerPage(driver).set_name_1()
        OwnerPage(driver).set_surname_1()
        OwnerPage(driver).set_address_1()
        OwnerPage(driver).set_station_university()
        OwnerPage(driver).set_phone_1()
        OwnerPage(driver).click_next_button()
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(OrderSiteLocators.ORDER_BUTTON))
        OrderPage(driver).click_when_to_bring()
        OrderPage(driver).choice_dec_20th()
        OrderPage(driver).choice_one_day()
        OrderPage(driver).click_black_color()
        OwnerPage(driver).set_comment_1()
        OrderPage(driver).click_order()
        OrderPage(driver).click_button_yes()
        assert 'Заказ оформлен' in OrderPage(driver).get_success_order_text()

    @allure.title('Проверка заказа через нижнюю кнопку "Заказать"')
    @allure.description('Заказываем самокат через нижнюю кнопку "Заказать" при помощи данных из второго набора, и проверяем, что заказ сформирован')
    def test_order_two(self, driver):
        MainPage(driver).click_button_cookies()
        MainPage(driver).click_order_down()
        OwnerPage(driver).set_name_2()
        OwnerPage(driver).set_surname_2()
        OwnerPage(driver).set_address_2()
        OwnerPage(driver).set_station_dinamo()
        OwnerPage(driver).set_phone_2()
        OwnerPage(driver).click_next_button()
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(OrderSiteLocators.ORDER_BUTTON))
        OrderPage(driver).click_when_to_bring()
        OrderPage(driver).choice_dec_25th()
        OrderPage(driver).choice_three_day()
        OrderPage(driver).click_grey_color()
        OwnerPage(driver).set_comment_2()
        OrderPage(driver).click_order()
        OrderPage(driver).click_button_yes()
        assert 'Заказ оформлен' in OrderPage(driver).get_success_order_text()