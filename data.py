from locators.buy_page_locators import BuyPageLocators

ANSWER = {
    0: 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.',
    1: 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, '
       'можете просто сделать несколько заказов — один за другим.',
    2: 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. '
       'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли '
       'самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.',
    3: 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.',
    4: 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по '
       'красивому номеру 1010.',
    5: 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если '
       'будете кататься без передышек и во сне. Зарядка не понадобится.',
    6: 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не '
       'попросим. Все же свои.',
    7: 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
}

DATA_BUYER = {
    'name': 'Фродо',
    'surname': 'Беггинс',
    'adress': 'Изенгард',
    'station': 'Комсомольская',
    'phone': '+71233211221'
}

DATA_RENTER = {
    'name': 'Бильбо',
    'surname': 'Беггинс',
    'adress': 'Эсгарот',
    'station': 'Бульвар Рокоссовского',
    'phone': '11111111111'
}

MASSIVE_BUYER = [
    [BuyPageLocators.SET_NAME, DATA_BUYER['name']],
    [BuyPageLocators.SET_SURNAME, DATA_BUYER['surname']],
    [BuyPageLocators.SET_ADRESS, DATA_BUYER['adress']],
    [BuyPageLocators.SET_STATION, DATA_BUYER['station']],
    [BuyPageLocators.KOMSOMOLSKAYA_STATION],
    [BuyPageLocators.SET_PHONE, DATA_BUYER['phone']],
    [BuyPageLocators.BUTTON_NEXT]
]

MASSIVE_RENTER = [
    [BuyPageLocators.SET_NAME, DATA_RENTER['name']],
    [BuyPageLocators.SET_SURNAME, DATA_RENTER['surname']],
    [BuyPageLocators.SET_ADRESS, DATA_RENTER['adress']],
    [BuyPageLocators.SET_STATION, DATA_RENTER['station']],
    [BuyPageLocators.BOULEVARD_ROKOSSOVSKOGO],
    [BuyPageLocators.SET_PHONE, DATA_BUYER['phone']],
    [BuyPageLocators.BUTTON_NEXT]
]

MASSIVE_DATE_1 = [
    [BuyPageLocators.DELIVERY_DATE],
    [BuyPageLocators.DELIVERY_DATE, '29.07.2024'],
    [BuyPageLocators.DELIVERY_DATE_29_07_2024],
    [BuyPageLocators.RENTAL_PERIOD],
    [BuyPageLocators.RENTAL_PERIOD_SIX_DAYS],
    [BuyPageLocators.COLOUR_1],
    [BuyPageLocators.COMMENT],
    [BuyPageLocators.COMMENT, 'Звоните вечером'],
    [BuyPageLocators.ALLOW_BUTTON_DATE_FORM]
]

MASSIVE_DATE_2 = [
    [BuyPageLocators.DELIVERY_DATE],
    [BuyPageLocators.DELIVERY_DATE, '30.07.2024'],
    [BuyPageLocators.DELIVERY_DATE_30_07_2024],
    [BuyPageLocators.RENTAL_PERIOD],
    [BuyPageLocators.RENTAL_PERIOD_FIVE_DAYS],
    [BuyPageLocators.COLOUR_2],
    [BuyPageLocators.COMMENT],
    [BuyPageLocators.COMMENT, 'Звоните днем'],
    [BuyPageLocators.ALLOW_BUTTON_DATE_FORM]
]

RENT_COMPLETE = 'Заказ оформлен'
