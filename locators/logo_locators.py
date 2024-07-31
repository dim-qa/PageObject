from selenium.webdriver.common.by import By


class LogoLocators:
    LOGO_SCOOTERS = By.CLASS_NAME, 'Header_LogoScooter__3lsAR'
    LOGO_YANDEX = By.CLASS_NAME, 'Header_LogoYandex__3TSOI'
    BUTTON_FIND_YANDEX = By.XPATH, ".//*[@class='arrow__button' and text()='Найти']"
