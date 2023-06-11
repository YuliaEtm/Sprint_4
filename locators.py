from selenium.webdriver.common.by import By


class Locators:
    # Кнопка заказать вверху главной
    ORDER_BUTTON_HEDER = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    # Кнопка заказать внизу главной
    ORDER_BUTTON_MIDDLE = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    # Логотип "Яндекс"
    LOGO_YA = (By.XPATH, "//img[@alt='Yandex']")
    # Логотип "Самокат"
    LOGO_SCOOTER = (By.XPATH, '//img[@ alt="Scooter"]')
    # КУКУ
    COOKIE = (By.XPATH, "// button[ @ id = 'rcc-confirm-button']")
    # Проверка главной страницы
    SCOOTER_TEXT = (By.XPATH, "//div[@class='Header_Disclaimer__3VEni']")

    # Блок вопросы о важном
    QUESTIONS_IMPORTANT = (By.XPATH, "//div[contains(text(),'Вопросы о важном')]")
    # Вопросы
    QUESTIONS_ALL = (By.XPATH, '//div[@class="accordion__item" ]')
    # Ответы
    ANSWER_ALL = (By.XPATH, '//div[@class="accordion__panel" ]/p')

    # форма Заказать часть1 Для кого самокат
    # Заголовок для кого самокат
    FOR_WHOM = (By.XPATH, '//div[@class="Order_Header__BZXOb"]')
    # Поле имя
    NAME_DRIVER = (By.XPATH, '//input[@placeholder="* Имя"]')
    # Поле Фамилия
    SURNAME_DRIVER = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    # Поле Адрес
    ADDRESS_DRIVER = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    # Поле станция метро
    METRO_DRIVER = (By.CLASS_NAME, 'select-search__input')
    # Поле Телефон
    TELEPHONE_DRIVER = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    # Далее кнопка из заказать часть1
    NEXT_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")

    # форма Заказать часть2 Про аренду
    # Поле когда привезти самокат
    WHEN_DRIVER = (By.XPATH, "//div[@class='react-datepicker__input-container']//input[@type='text']")
    # Поле срок аренды
    RENTAL_PERIOD_DRIVER = (By.XPATH, "//span[@class='Dropdown-arrow']")
    # поле комментарий для курьера
    COMMENT_DRIVER = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')

    # Кнопка заказать
    ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    # Кнопка хотите оформить заказ ДА
    YES_BUTTON = (By.XPATH, "// button[contains(text(), 'Да')]")
    # кнопка посмитреть статус
    STATUS_BUTTON = (By.XPATH, "// button[contains(text(), 'Посмотреть статус')]")
    # Имя заказчика в статусе заказа
    NAME_IN_STATUS = (By.XPATH, "//div[@class='Track_Value__15eEX']")
