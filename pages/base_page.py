from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    """перейти"""

    def get_url(self, url):
        self.driver.get(url)

    """клик по кнопке"""

    def click_to_button(self, locator):
        element = self.driver.find_element(*locator)
        element.click()

    """скролит до элемента"""

    def scroll_to_down(self, locator):
        self.wait_an_element(locator)
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    """ожидание"""

    def wait_an_element(self, locator):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator))
        element = self.driver.find_element(*locator)
        return element

    """меняет локатор для вопроса
    добавляет уникальный номер"""

    @staticmethod
    def add_num_to_locator(locator, num):
        method, locator = locator
        return method, locator.format(num)

    """вернет текст элемента"""

    def get_text(self, locator):
        text = self.driver.find_element(*locator).text
        return text

    """вводит текст по локатору"""

    def set_input(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    def url(self):
        return self.driver.current_url

    """переход по вкладке"""
    def switch(self, logo, equals):
        self.click_to_button(logo)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 10).until(
            expected_conditions.url_to_be(equals))
        new_page = self.url()
        self.driver.close()
        return new_page
