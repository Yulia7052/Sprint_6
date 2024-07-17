from pages.main_page_helper import MainPageHelper


class TestLogo:

    def test_check_scooter_logo_click(self, driver):
        helper = MainPageHelper(driver)

        helper.get_main_page()
        helper.click_header_scooter_logo()

        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"

    def test_check_yandex_logo_click(self, driver):
        helper = MainPageHelper(driver)

        helper.get_main_page()
        helper.click_header_yandex_logo()
        driver.switch_to.window(driver.window_handles[1])
        helper.wait_until_page_loaded("Дзен")

        assert driver.current_url == "https://dzen.ru/?yredirect=true"
