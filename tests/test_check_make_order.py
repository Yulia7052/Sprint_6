import allure

from pages.main_page_helper import MainPageHelper
from pages.order_page_helper import OrderPageHelper


class TestOrder:

    @allure.title('Проверка оформления заказа по кнопке в верхней части страницы')
    def test_check_make_order_from_header(self, driver):
        main_helper = MainPageHelper(driver)
        order_helper = OrderPageHelper(driver)

        main_helper.get_main_page()

        main_helper.click_header_order_button()

        order_helper.set_name("Вупсень")
        order_helper.set_last_name("Вупсень")
        order_helper.set_address("г.Москва, ул.Садовая, дом.35")
        order_helper.set_metro_station()
        order_helper.set_telephone_number("66686668666")

        order_helper.click_cookie_button()
        order_helper.click_next_button()

        order_helper.set_date()
        order_helper.set_period()
        order_helper.set_color_black()
        order_helper.set_color_grey()
        order_helper.set_comment("Спасибо!!!")

        order_helper.click_order_button()
        order_helper.click_modal_order_button()

        success_text = order_helper.get_success_text()

        assert "Заказ оформлен" in success_text

    @allure.title('Проверка оформления заказа по кнопке в средней части страницы')
    def test_check_make_order_from_middle(self, driver):
        main_helper = MainPageHelper(driver)
        order_helper = OrderPageHelper(driver)

        main_helper.get_main_page()

        main_helper.click_middle_order_button()

        order_helper.set_name("Пупсень")
        order_helper.set_last_name("Пупсень")
        order_helper.set_address("г.Москва,ул.Садовая,д.36")
        order_helper.set_metro_station()
        order_helper.set_telephone_number("12345678987")

        order_helper.click_cookie_button()
        order_helper.click_next_button()

        order_helper.set_date()
        order_helper.set_period()
        order_helper.set_color_black()
        order_helper.set_comment("Большое спасибо!!!")

        order_helper.click_order_button()
        order_helper.click_modal_order_button()

        success_text = order_helper.get_success_text()

        assert "Заказ оформлен" in success_text
