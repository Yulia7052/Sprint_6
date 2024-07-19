import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPageHelper(BasePage):
    header_scooter_logo = [By.XPATH, '//div[contains(@class, "Header_Logo")]/a[contains(@class, "Header_LogoScooter")]']
    header_yandex_logo = [By.XPATH, '//div[contains(@class, "Header_Logo")]/a[contains(@class, "Header_LogoYandex")]']

    header_order_button = [By.XPATH, '//div[contains(@class, "Header_Nav")]/button[contains(@class, "Button_Button")]']
    middle_order_button = [By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button[contains(@class, '
                                     '"Button_Button")]']

    dict_questions = {
        1: [By.ID, 'accordion__heading-0'],
        2: [By.ID, 'accordion__heading-1'],
        3: [By.ID, 'accordion__heading-2'],
        4: [By.ID, 'accordion__heading-3'],
        5: [By.ID, 'accordion__heading-4'],
        6: [By.ID, 'accordion__heading-5'],
        7: [By.ID, 'accordion__heading-6'],
        8: [By.ID, 'accordion__heading-7']
    }

    dict_answers = {
        1: [By.XPATH, '//div[@id="accordion__panel-0"]/p'],
        2: [By.XPATH, '//div[@id="accordion__panel-1"]/p'],
        3: [By.XPATH, '//div[@id="accordion__panel-2"]/p'],
        4: [By.XPATH, '//div[@id="accordion__panel-3"]/p'],
        5: [By.XPATH, '//div[@id="accordion__panel-4"]/p'],
        6: [By.XPATH, '//div[@id="accordion__panel-5"]/p'],
        7: [By.XPATH, '//div[@id="accordion__panel-6"]/p'],
        8: [By.XPATH, '//div[@id="accordion__panel-7"]/p']
    }

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Кликаем на кнопку "Заказать" в верхней части страницы')
    def click_header_order_button(self):
        self.click_button(self.header_order_button)

    @allure.step('Кликаем на логотип "Самокат"')
    def click_header_scooter_logo(self):
        self.click_button(self.header_scooter_logo)

    @allure.step('Кликаем на логотип "Яндекс" для перехода в "Яндекс.Дзен"')
    def click_header_yandex_logo(self):
        self.click_button(self.header_yandex_logo)

    @allure.step('Кликаем на кнопку "Заказать" в средней части страницы')
    def click_middle_order_button(self):
        element = self.driver.find_element(*self.middle_order_button)
        self.driver.execute_script('arguments[0].scrollIntoView(true);', element)
        self.click_button(self.middle_order_button)

    @allure.step('Скролим до списка важных вопросов')
    def scroll_to_question(self, question_number):
        question = self.dict_questions[question_number]
        element = self.driver.find_element(*question)
        self.driver.execute_script('arguments[0].scrollIntoView(true);', element)

    @allure.step('Кликаем на вопросы')
    def click_question(self, question_number):
        question = self.dict_questions[question_number]
        self.click_button(question)

    @allure.step('Получаем текст ответов на вопросы')
    def get_answer_text(self, question_number):
        answer = self.dict_answers[question_number]
        return self.get_text(answer)
