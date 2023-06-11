import allure

from locators import Locators
from pages.page_base import BasePage
from pages.page_order import PageOrderFor
from data import Credential


class PageTransit(BasePage):

    @allure.step('оформляем заказ')
    def ordering_scooter (self,driver):
        ''' оформляем заказ самоката'''

        page_order = PageOrderFor(driver)
        # base_page = BasePage(driver)
        self.go_to_site('https://qa-scooter.praktikum-services.ru/')
        self.cook_ok()
        self.find_element_located(Locators.ORDER_BUTTON_HEDER).click()
        self.find_element_located(Locators.NAME_DRIVER).send_keys(Credential.name[0])
        self.find_element_located(Locators.SURNAME_DRIVER).send_keys(Credential.surname[0])
        self.find_element_located(Locators.ADDRESS_DRIVER).send_keys(Credential.address[0])
        page_order.select_metro(driver, Credential.metro[0])
        self.find_element_located(Locators.TELEPHONE_DRIVER).send_keys(Credential.telephone[0])

        self.find_element_located(Locators.NEXT_BUTTON).click()
        page_order.select_data(driver, Credential.data[0])
        page_order.select_rental_period(driver, Credential.period[0])
        page_order.select_color(driver, Credential.color[0])
        self.find_element_located(Locators.ORDER_BUTTON).click()

        self.find_element_located(Locators.YES_BUTTON).click()

        self.find_element_located(Locators.STATUS_BUTTON).click()

