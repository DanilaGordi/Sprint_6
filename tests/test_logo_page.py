import allure
from conftest import driver
from pages.main_page import MainPage
from pages.base_page import BasePage
from data import Site


class TestLogoPage:

    @allure.title('Проверка перехода на страницу "Дзен"')
    @allure.description('Проверяем переход на странцу "Дзен" через логотип "ЯНДЕКС"')
    def test_transition_to_zen(self, driver):
        main_page = MainPage(driver)
        main_page.click_button_cookies()
        main_page.click_logo_yandex()
        main_page.switch_to_window()
        main_page.wait_for_site(Site.dzen_site)
        assert main_page.get_site() == Site.dzen_site

    @allure.title('Проверка перехода на главную страницу "Самокат"')
    @allure.description('Проверяем переход на главную странцу "Самокат" из оформления заказа')
    def test_transition_to_scooter(self, driver):
        main_page = MainPage(driver)
        main_page.click_button_cookies()
        main_page.click_order_top()
        main_page.click_logo_scooter()
        main_page.wait_for_site(Site.main_site)
        assert main_page.get_site() == Site.main_site
