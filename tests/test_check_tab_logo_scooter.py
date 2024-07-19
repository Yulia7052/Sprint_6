import allure

from pages.main_page_helper import MainPageHelper


class TestLogo:

    @allure.title('Проверка нажатия на логотип "Самокат"')
    def test_check_scooter_logo_click(self, driver):
        helper = MainPageHelper(driver)

        helper.get_main_page()
        helper.click_header_scooter_logo()

        assert helper.driver.current_url == "https://qa-scooter.praktikum-services.ru/"

    @allure.title('Проверка нажатия на логотип "Яндекс" для перехода в "Яндекс.Дзен"')
    def test_check_yandex_logo_click(self, driver):
        helper = MainPageHelper(driver)

        helper.get_main_page()
        helper.click_header_yandex_logo()
        helper.driver.switch_to.window(helper.driver.window_handles[1])
        helper.wait_until_page_loaded("Дзен")

        assert helper.driver.current_url == "https://dzen.ru/?yredirect=true"
