import allure

from locators import Locators
from pages.page_base import BasePage
from pages.page_order import PageOrderFor


metro = 'Сокольники'
data = '15.06.2023'
period = 'двое суток'
color = 'black'
name = 'Васяня'
surname = 'Иванов'
address = 'Смоленск'
telephone = '89997776655'


class PageTransit(BasePage):

    @allure.step('оформляем заказ')
    def ordering_scooter (sels,driver):
        page_order = PageOrderFor(driver)
        base_page = BasePage(driver)
        base_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        base_page.cook_ok()
        base_page.find_element_located(Locators.ORDER_BUTTON_HEDER).click()
        base_page.find_element_located(Locators.NAME_DRIVER).send_keys(name)
        base_page.find_element_located(Locators.SURNAME_DRIVER).send_keys(surname)
        base_page.find_element_located(Locators.ADDRESS_DRIVER).send_keys(address)
        page_order.select_metro(driver, metro)
        base_page.find_element_located(Locators.TELEPHONE_DRIVER).send_keys(telephone)

        base_page.find_element_located(Locators.NEXT_BUTTON).click()
        page_order.select_data(driver, data)
        page_order.select_rental_period(driver, period)
        page_order.select_color(driver, color)
        base_page.find_element_located(Locators.ORDER_BUTTON).click()

        base_page.find_element_located(Locators.YES_BUTTON).click()

        base_page.find_element_located(Locators.STATUS_BUTTON).click()

