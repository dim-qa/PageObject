import allure
import pytest
import data
import links
from locators.buy_page_locators import BuyPageLocators
from locators.logo_locators import LogoLocators
from locators.main_page_locators import MainPageLocators


class TestMainPage:
    """фикстуры откроют главную страницу
    прокрутит до низа страницы
    кликает по вопросу и сравнивает ответ с текстом из data"""
    @allure.step('Клик на вопрос и получение текста ответа')
    @pytest.mark.parametrize(
        "q_num, expected_result", [
            (0, data.ANSWER[0]),
            (1, data.ANSWER[1]),
            (2, data.ANSWER[2]),
            (3, data.ANSWER[3]),
            (4, data.ANSWER[4]),
            (5, data.ANSWER[5]),
            (6, data.ANSWER[6]),
            (7, data.ANSWER[7])
        ]
    )
    def test_questions(self, main_page, main_page_click_cookie, q_num, expected_result):
        main_page.scroll_to_down(MainPageLocators.QUESTION_LOCATOR_8)
        main_page.click_to_question(MainPageLocators.QUESTION_LOCATOR, q_num)
        result = main_page.get_answer_from_question(MainPageLocators.ANSWER_LOCATOR, q_num)
        assert main_page.comparison_answer(result, expected_result)

    """Фикстуры откроют главную страницу
    параметризация передает кнопку заказать, список из данных для первой и второй формы
    формы заполняются сравнивается текст в окне"""
    @allure.step('Клик по кнопке заказать, заполнение форм и заказ, переход по логотипу')
    @pytest.mark.parametrize(
        "rent_button, profile, date_rent", [
            (BuyPageLocators.BUTTON_BUY_FOOTER, data.MASSIVE_BUYER, data.MASSIVE_DATE_1),
            (BuyPageLocators.BUTTON_BUY_MAIN_PAGE, data.MASSIVE_RENTER, data.MASSIVE_DATE_2)
        ]
    )
    def test_buy_scooter(self, buy_page, main_page_click_cookie, rent_button, profile, date_rent):
        buy_page.filling_out_the_lease(rent_button, profile, date_rent)
        result = buy_page.get_text(BuyPageLocators.TEXT_GOOD_RENT)
        assert data.RENT_COMPLETE in result, f'Нет Заказ оформлен'

    """фикстуры открывают главную страницу
    производиться заполнение формы заказа
    кликается посмотреть статус
    кликается по логотипу из параметризации по очереди
    сравнивается url"""
    @allure.step('формы, клик по лого')
    @pytest.mark.parametrize(
        "rent_button, profile, date_rent, logo, equals", [
            (BuyPageLocators.BUTTON_BUY_FOOTER, data.MASSIVE_BUYER, data.MASSIVE_DATE_1,
             LogoLocators.LOGO_SCOOTERS, links.link_main_page),
            (
                    BuyPageLocators.BUTTON_BUY_MAIN_PAGE, data.MASSIVE_RENTER, data.MASSIVE_DATE_2,
                    LogoLocators.LOGO_YANDEX, links.link_yandex)
        ]
    )
    def test_click_to_logo(self, buy_page, main_page_click_cookie,
                           rent_button, profile, date_rent, logo, equals):
        buy_page.filling_out_the_lease(rent_button, profile, date_rent)
        buy_page.click_to_button(BuyPageLocators.BUTTON_STATUS)
        url = buy_page.switch(logo, equals)
        assert url == equals
