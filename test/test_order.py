import time

import allure
import pytest

from locators import Locators
from pages.page_order import PageOrderFor

metro = ('Сокольники', 'Университет')
data = ('15.06.2023', '20.06.2023')
period = ('двое суток', 'сутки')
color = ('black', 'grey')
name = ('Васяня', 'Масяня')
surname = ('Иванов', 'Петрова')
address = ('Смоленск', 'Красная площадь')
telephone = ('89997776655', '+79992223344')


@pytest.mark.parametrize('num', [0, 1])
@allure.description(
    'Проверяем заказ самоката, позитивный сценарий, кнопка "Заказать" - вверху страницы. Два набора данных')
def test_order_button_header(driver, num):
    page_order = PageOrderFor(driver)

    page_order.go_to_site('https://qa-scooter.praktikum-services.ru/')
    page_order.cook_ok()
    page_order.find_element_located(Locators.ORDER_BUTTON_HEDER).click()
    page_order.find_element_located(Locators.NAME_DRIVER).send_keys(name[num])
    page_order.find_element_located(Locators.SURNAME_DRIVER).send_keys(surname[num])
    page_order.find_element_located(Locators.ADDRESS_DRIVER).send_keys(address[num])
    page_order.select_metro(driver, metro[num])
    page_order.find_element_located(Locators.TELEPHONE_DRIVER).send_keys(telephone[num])

    page_order.find_element_located(Locators.NEXT_BUTTON).click()
    page_order.select_data(driver, data[num])
    page_order.select_rental_period(driver, period[num])
    page_order.select_color(driver, color[num])
    page_order.find_element_located(Locators.ORDER_BUTTON).click()

    page_order.find_element_located(Locators.YES_BUTTON).click()

    page_order.find_element_located(Locators.STATUS_BUTTON).click()

    assert page_order.find_element_located(Locators.NAME_IN_STATUS).text == name[num]


@allure.description('Проверяем заказ самоката, позитивный сценарий, кнопка "Заказать" - внизу страницы')
def test_order_button_middle(driver):
    page_order = PageOrderFor(driver)

    page_order.go_to_site('https://qa-scooter.praktikum-services.ru/')
    page_order.cook_ok()
    page_order.find_element_located(Locators.ORDER_BUTTON_MIDDLE).click()
    page_order.find_element_located(Locators.NAME_DRIVER).send_keys(name[0])
    page_order.find_element_located(Locators.SURNAME_DRIVER).send_keys(surname[0])
    page_order.find_element_located(Locators.ADDRESS_DRIVER).send_keys(address[0])
    page_order.select_metro(driver, metro[0])
    page_order.find_element_located(Locators.TELEPHONE_DRIVER).send_keys(telephone[0])

    page_order.find_element_located(Locators.NEXT_BUTTON).click()
    page_order.select_data(driver, data[0])
    page_order.select_rental_period(driver, period[0])
    page_order.select_color(driver, color[0])
    page_order.find_element_located(Locators.ORDER_BUTTON).click()

    page_order.find_element_located(Locators.YES_BUTTON).click()

    page_order.find_element_located(Locators.STATUS_BUTTON).click()

    assert page_order.find_element_located(Locators.NAME_IN_STATUS).text == name[0]

