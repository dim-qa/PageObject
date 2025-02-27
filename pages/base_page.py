import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("переход по ссылке")
    def get_url(self, url):
        self.driver.get(url)

    @allure.step("клик по кнопке")
    def click_to_button(self, locator):
        element = self.driver.find_element(*locator)
        element.click()

    @allure.step("скролит до элемента")
    def scroll_to_down(self, locator):
        self.wait_an_element(locator)
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("ожидание")
    def wait_an_element(self, locator):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator))
        element = self.driver.find_element(*locator)
        return element

    @staticmethod
    def add_num_to_locator(locator, num):
        method, locator = locator
        return method, locator.format(num)

    @allure.step("вернет текст элемента")
    def get_text(self, locator):
        text = self.driver.find_element(*locator).text
        return text

    @allure.step("вводит текст по локатору")
    def set_input(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    def url(self):
        return self.driver.current_url

    @allure.step("переход по вкладке")
    def switch(self, logo, equals):
        self.click_to_button(logo)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 10).until(
            expected_conditions.url_to_be(equals))
        new_page = self.url()
        self.driver.close()
        return new_page
