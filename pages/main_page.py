import allure
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Клик куки')
    def click_to_cookie(self, locator):
        self.click_to_button(locator)

    @allure.step('Клик по вопросу')
    def click_to_question(self, locator, num):
        element = self.add_num_to_locator(locator, num)
        self.click_to_button(element)
        return element

    @allure.step('Текст из ответа')
    def get_answer_from_question(self, locator, num):
        element = self.add_num_to_locator(locator, num)
        text = self.get_text(element)
        return text

    @staticmethod
    def comparison_answer(result, expected_result):
        return result == expected_result
