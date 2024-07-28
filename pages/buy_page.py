import allure
from locators.buy_page_locators import BuyPageLocators
from pages.base_page import BasePage


class BuyPage(BasePage):

    def click_to_buy_button_on_main(self, locator):
        self.wait_an_element(locator)
        self.click_to_button(locator)

    def set_data_buyer(self, inner_locator, value):
        self.click_to_button(inner_locator)
        self.set_input(inner_locator, value)

    """Локатор поля, текст"""
    @allure.step('проверка заполнения формы информации')
    def form_data_buyer(self, massive, massive_date):
        self.set_data_buyer(massive[0][0], massive[0][1])
        self.set_data_buyer(massive[1][0], massive[1][1])
        self.set_data_buyer(massive[2][0], massive[2][1])
        self.set_data_buyer(massive[3][0], massive[3][1])
        self.click_to_button(massive[4][0])
        self.set_data_buyer(massive[5][0], massive[5][1])
        self.click_to_button(massive[6][0])
        self.click_to_button(massive_date[0][0])
        self.set_input(massive_date[1][0], massive_date[1][1])
        self.click_to_button(massive_date[2][0])
        self.click_to_button(massive_date[3][0])
        self.click_to_button(massive_date[4][0])
        self.click_to_button(massive_date[5][0])
        self.click_to_button(massive_date[6][0])
        self.set_input(massive_date[7][0], massive_date[7][1])
        self.click_to_button(massive_date[8][0])

    """скролиться до кнопки заказать
    кликается по ней
    заполняются обе формы"""
    @allure.step('проверка заполнения формы заказа')
    def filling_out_the_lease(self, rent_button, massive_data, massive_date):
        self.scroll_to_down(rent_button)
        self.click_to_button(rent_button)
        self.form_data_buyer(massive_data, massive_date)
        self.click_to_button(BuyPageLocators.ALLOW_BUTTON_RENT)
