import time

import allure

from locators import Locators
from pages.page_base import BasePage
from pages.page_transit import PageTransit


@allure.description(
    'Заказ создан, проверяем переход со страницы статус заказа по логотипу "Яндекс" на главную страницу Яндекса')
def test_trasit_to_yandex_logo(driver):
    page_transit = PageTransit(driver)
    base_page = BasePage(driver)

    page_transit.ordering_scooter(driver)
    base_page.find_element_located(Locators.LOGO_YA).click()

    current_url = driver.current_url

    assert current_url == "https://ya.ru/"


@allure.description(
    'Заказ создан, проверяем переход со страницы статус заказа по логотипу "Самокат" на главную страницу')
def test_transit_to_scooter_logo(driver):
    page_transit = PageTransit(driver)
    base_page = BasePage(driver)

    page_transit.ordering_scooter(driver)
    base_page.find_element_located(Locators.LOGO_SCOOTER).click()

    assert base_page.find_element_located(Locators.SCOOTER_TEXT).text == 'УЧЕБНЫЙ ТРЕНАЖЕР'
