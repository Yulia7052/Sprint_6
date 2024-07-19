import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrderPageHelper(BasePage):
    name_field = [By.XPATH, '//div/input[@placeholder="* Имя"]']
    last_name_field = [By.XPATH, '//div/input[@placeholder="* Фамилия"]']
    address_field = [By.XPATH, '//div/input[@placeholder="* Адрес: куда привезти заказ"]']
    metro_station_select = [By.XPATH, '//div/input[@placeholder="* Станция метро"]']
    metro_station = [By.XPATH, '//div[@class="select-search__select"]/ul/li[1]/button']
    telephone_number_field = [By.XPATH, '//div/input[@placeholder="* Телефон: на него позвонит курьер"]']
    date_datepicker = [By.XPATH, '//div[contains(@class, "Order_MixedDatePicker")]']
    day_div = [By.CLASS_NAME, 'react-datepicker__day--today']
    period_dropdown = [By.XPATH, '//div[contains(@class, "Dropdown-root")]']
    period_div = [By.XPATH, '//div[contains(@class, "Dropdown-root")]/div[contains(@class, "Dropdown-menu")]/div[1]']
    color_black_button = [By.XPATH, '//div[contains(@class, "Order_Checkboxes")]/label[@for="black"]/input']
    color_grey_button = [By.XPATH, '//div[contains(@class, "Order_Checkboxes")]/label[@for="grey"]/input']
    comment_field = [By.XPATH, '//div/input[@placeholder="Комментарий для курьера"]']
    next_button = [By.XPATH, '//div[contains(@class, "Order_NextButton")]/button[contains(@class, "Button_Button")]']
    order_button = [By.XPATH, '//div[contains(@class, "Order_Buttons")]/button[2]']
    cookie_button = [By.XPATH, '//*[@id="rcc-confirm-button"]']
    modal_order_button = [By.XPATH, '//div[contains(@class, "Order_Modal")]/div[contains(@class, '
                                    '"Order_Buttons")]/button[2]']
    modal_success_text = [By.XPATH, '//div[contains(@class, "Order_Modal")]/div[contains(@class, "Order_ModalHeader")]']

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Получаем нужный текст')
    def get_success_text(self):
        return self.get_text(self.modal_success_text)

    @allure.step('Кликаем на кнопку "Далее"')
    def click_next_button(self):
        self.click_button(self.next_button)

    @allure.step('Кликаем на кнопку "Заказать"')
    def click_order_button(self):
        self.click_button(self.order_button)

    @allure.step('Кликаем на кнопку "Да"')
    def click_modal_order_button(self):
        self.click_button(self.modal_order_button)

    @allure.step('Кликаем на кнопку с куки')
    def click_cookie_button(self):
        self.click_button(self.cookie_button)

    @allure.step('Вводим имя в поле с именем')
    def set_name(self, value):
        self.set_input_value(self.name_field, value)

    @allure.step('Вводим фамилию в поле с фамилией')
    def set_last_name(self, value):
        self.set_input_value(self.last_name_field, value)

    @allure.step('Вводим адрес в поле с адресом')
    def set_address(self, value):
        self.set_input_value(self.address_field, value)

    @allure.step('Выбираем станцию метро')
    def set_metro_station(self):
        self.set_select_value(self.metro_station_select, self.metro_station)

    @allure.step('Вводим номер телефона')
    def set_telephone_number(self, value):
        self.set_input_value(self.telephone_number_field, value)

    @allure.step('Выбираем дату')
    def set_date(self):
        self.set_date_value(self.date_datepicker, self.day_div)

    @allure.step('Выбираем период аренды')
    def set_period(self):
        self.set_date_value(self.period_dropdown, self.period_div)

    @allure.step('Выбираем черный цвет самоката')
    def set_color_black(self):
        self.click_button(self.color_black_button)

    @allure.step('Выбираем серый цвет самоката')
    def set_color_grey(self):
        self.click_button(self.color_grey_button)

    @allure.step('Заполняем поле с комментарием')
    def set_comment(self, value):
        self.set_input_value(self.comment_field, value)
