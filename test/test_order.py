import allure
import pytest

from data import Credential
from locators import Locators
from pages.page_order import PageOrderFor


@pytest.mark.parametrize('numer', [0, 1])
@allure.description(
    'Проверяем заказ самоката, позитивный сценарий, кнопка "Заказать" - вверху страницы. Два набора данных')
def test_order_button_header(driver, numer):
    page_order = PageOrderFor(driver)

    ppage_order: PageOrderFor = PageOrderFor(driver)

    page_order.go_to_site('https://qa-scooter.praktikum-services.ru/')
    page_order.cook_ok()
    page_order.find_element_located(Locators.ORDER_BUTTON_MIDDLE).click()
    page_order.for_whom(driver, numer)

    page_order.find_element_located(Locators.NEXT_BUTTON).click()

    page_order.about_rent(driver, numer)
    page_order.find_element_located(Locators.ORDER_BUTTON).click()
    page_order.find_element_located(Locators.YES_BUTTON).click()
    page_order.find_element_located(Locators.STATUS_BUTTON).click()

    assert page_order.find_element_located(Locators.NAME_IN_STATUS).text == Credential.name[numer]


@allure.description('Проверяем заказ самоката, позитивный сценарий, кнопка "Заказать" - внизу страницы')
def test_order_button_middle(driver):
    page_order: PageOrderFor = PageOrderFor(driver)