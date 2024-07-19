from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    site_url = 'https://qa-scooter.praktikum-services.ru/'

    def __init__(self, driver):
        self._driver = driver

    @property
    def driver(self):
        return self._driver

    def get_main_page(self):
        self.driver.get(self.site_url)

    def find_element(self, element):
        return self.driver.find_element(*element)

    def wait_until_page_loaded(self, title):
        WebDriverWait(self.driver, 4).until(expected_conditions.title_is(title))

    def click_button(self, button):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((button[0], button[1])))
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((button[0], button[1])))
        self.find_element(button).click()

    def get_text(self, element):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((element[0], element[1])))
        return self.find_element(element).text

    def set_input_value(self, input, value):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((input[0], input[1])))
        self.find_element(input).send_keys(value)

    def set_select_value(self, select, value):
        self.click_button(select)
        self.click_button(value)

    def set_date_value(self, datepicker, day):
        self.click_button(datepicker)
        self.click_button(day)

    def set_dropdown_value(self, dropdown, value):
        self.click_button(dropdown)
        self.click_button(value)
