from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_LOCATOR = By.ID, 'accordion__heading-{}'
    ANSWER_LOCATOR = By.ID, 'accordion__panel-{}'

    COOKIE = By.XPATH, ".//*[@id='rcc-confirm-button']"
    QUESTION_LOCATOR_8 = By.ID, 'accordion__heading-7'

    MAIN_PAGE_TITLE = By.XPATH, ".//*[@class='Home_Header__iJKdX']"
