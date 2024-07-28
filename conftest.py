from selenium import webdriver
import pytest
import links
from locators.main_page_locators import MainPageLocators
from pages.buy_page import BuyPage
from pages.main_page import MainPage

from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService


@pytest.fixture()
def driver():
    driver = webdriver.Firefox(service=FirefoxService(executable_path=GeckoDriverManager().install()))
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def main_page(driver):
    page = MainPage(driver)
    page.get_url(links.link_main_page)
    return page


@pytest.fixture(scope='function')
def main_page_click_cookie(main_page):
    main_page.click_to_cookie(MainPageLocators.COOKIE)
    return main_page


@pytest.fixture(scope='function')
def buy_page(driver):
    page = BuyPage(driver)
    page.get_url(links.link_main_page)
    return page
