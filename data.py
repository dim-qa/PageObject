from locators.buy_page_locators import BuyPageLocators

answer = {
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

data_buyer = {
    'name': 'Фродо',
    'surname': 'Беггинс',
    'adress': 'Изенгард',
    'station': 'Комсомольская',
    'phone': '+71233211221'
}

data_renter = {
    'name': 'Бильбо',
    'surname': 'Беггинс',
    'adress': 'Эсгарот',
    'station': 'Бульвар Рокоссовского',
    'phone': '11111111111'
}

massive_buyer = [
    [BuyPageLocators.SET_NAME, data_buyer['name']],
    [BuyPageLocators.SET_SURNAME, data_buyer['surname']],
    [BuyPageLocators.SET_ADRESS, data_buyer['adress']],
    [BuyPageLocators.SET_STATION, data_buyer['station']],
    [BuyPageLocators.KOMSOMOLSKAYA_STATION],
    [BuyPageLocators.SET_PHONE, data_buyer['phone']],
    [BuyPageLocators.BUTTON_NEXT]
]

massive_renter = [
    [BuyPageLocators.SET_NAME, data_renter['name']],
    [BuyPageLocators.SET_SURNAME, data_renter['surname']],
    [BuyPageLocators.SET_ADRESS, data_renter['adress']],
    [BuyPageLocators.SET_STATION, data_renter['station']],
    [BuyPageLocators.BOULEVARD_ROKOSSOVSKOGO],
    [BuyPageLocators.SET_PHONE, data_buyer['phone']],
    [BuyPageLocators.BUTTON_NEXT]
]

massive_date_1 = [
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

massive_date_2 = [
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

title_main_page = ('Самокат'
                   '\nна пару дней'
                   '\nПривезём его прямо к вашей двери,'
                   '\nа когда накатаетесь — заберём')

find = 'Найти'
