from selenium.webdriver.common.by import By


class BuyPageLocators:
    BUTTON_BUY_FOOTER = By.CLASS_NAME, 'Button_Button__ra12g'
    BUTTON_BUY_MAIN_PAGE = By.XPATH, ".//*[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']"

    SET_NAME = By.XPATH, ".//*[@placeholder='* Имя']"
    SET_SURNAME = By.XPATH, ".//*[@placeholder='* Фамилия']"
    SET_ADRESS = By.XPATH, ".//*[@placeholder='* Адрес: куда привезти заказ']"
    SET_STATION = By.XPATH, ".//*[@placeholder='* Станция метро']"
    SET_PHONE = By.XPATH, ".//*[@placeholder='* Телефон: на него позвонит курьер']"
    BUTTON_NEXT = By.XPATH, ".//*[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Далее']"
    KOMSOMOLSKAYA_STATION = By.XPATH, ".//*[@class='select-search__row' and @data-value='6']"
    BOULEVARD_ROKOSSOVSKOGO = By.XPATH, ".//*[@class='select-search__row' and @data-value='1']"

    DELIVERY_DATE = By.XPATH, ".//*[@class='react-datepicker__input-container']/input"
    DELIVERY_DATE_29_07_2024 = By.XPATH, (".//*[@class='react-datepicker__day react-datepicker__day--029 "
                                          "react-datepicker__day--selected']")
    DELIVERY_DATE_30_07_2024 = By.XPATH, (".//*[@class='react-datepicker__day react-datepicker__day--030 "
                                          "react-datepicker__day--selected']")
    RENTAL_PERIOD = By.XPATH, ".//*[@class='Dropdown-placeholder' and text() = '* Срок аренды']"
    RENTAL_PERIOD_SIX_DAYS = By.XPATH, ".//*[@class='Dropdown-option' and text() = 'шестеро суток']"
    RENTAL_PERIOD_FIVE_DAYS = By.XPATH, ".//*[@class='Dropdown-option' and text() = 'пятеро суток']"
    COLOUR_1 = By.XPATH, ".//*[text()='чёрный жемчуг']"
    COLOUR_2 = By.XPATH, ".//*[text()='серая безысходность']"
    COMMENT = By.XPATH, (".//*[@class='Input_Input__1iN_Z Input_Responsible__1jDKN' and @placeholder = 'Комментарий "
                         "для курьера']")
    ALLOW_BUTTON_DATE_FORM = By.XPATH, ".//*[@class='Button_Button__ra12g Button_Middle__1CSJM']"
    ALLOW_BUTTON_RENT = By.XPATH, ".//*[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']"
    TEXT_GOOD_RENT = By.XPATH, ".//*[@class='Order_ModalHeader__3FDaJ' and text()='Заказ оформлен']"

    GOOD_TEST = By.CLASS_NAME, 'Order_ModalHeader__3FDaJ'

    FORM_STATUS = By.CLASS_NAME, 'Order_Modal__YZ-d3'

    BUTTON_STATUS = By.XPATH, ".//*[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Посмотреть статус']"
