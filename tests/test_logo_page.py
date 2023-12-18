import allure
from conftest import driver
from pages.main_page import MainPage
from pages.base_page import BasePage
from data import Site


class TestLogoPage:

    @allure.title('Проверка перехода на страницу "Дзен"')
    @allure.description('Проверяем переход на странцу "Дзен" через логотип "ЯНДЕКС"')
    def test_transition_to_zen(self, driver):
        MainPage(driver).click_button_cookies()
        MainPage(driver).click_logo_yandex()
        driver.switch_to.window(driver.window_handles[1])
        MainPage(driver).wait_for_site(Site.dzen_site)
        assert BasePage(driver).get_site() == Site.dzen_site

    @allure.title('Проверка перехода на главную страницу "Самокат"')
    @allure.description('Проверяем переход на главную странцу "Самокат" из оформления заказа')
    def test_transition_to_scooter(self, driver):
        MainPage(driver).click_button_cookies()
        MainPage(driver).click_order_top()
        MainPage(driver).click_logo_scooter()
        MainPage(driver).wait_for_site(Site.main_site)
        assert BasePage(driver).get_site() == Site.main_site
