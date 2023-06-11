from selenium.webdriver.common.by import By

from data import Credential
from locators import Locators
from pages.page_base import BasePage


class PageOrderFor(BasePage):

    def select_metro(self, driver, metro):
        driver.find_element(*Locators.METRO_DRIVER).send_keys(metro)
        driver.find_element(By.XPATH, f"//div[contains(text(),'{metro}')]").click()

    def select_data(self, driver, data):
        driver.find_element(*Locators.WHEN_DRIVER).send_keys(data)
        driver.find_element(*Locators.WHEN_DRIVER).click()

    def select_rental_period(self, driver, period):
        driver.find_element(*Locators.RENTAL_PERIOD_DRIVER).click()
        driver.find_element(By.XPATH, f"//div[contains(text(),'{period}')]").click()

    def select_color(self, driver, color):
        driver.find_element(By.XPATH, f"// input[ @ id = '{color}']").click()

    def for_whom(self, driver, num):
        ''' Заполняем страницу - для кого самокат'''
        self.num = num
        driver.find_element(*Locators.NAME_DRIVER).send_keys(Credential.name[num])
        driver.find_element(*Locators.SURNAME_DRIVER).send_keys(Credential.surname[num])
        driver.find_element(*Locators.ADDRESS_DRIVER).send_keys(Credential.address[num])
        driver.find_element(*Locators.TELEPHONE_DRIVER).send_keys(Credential.telephone[num])
        self.select_metro(driver,Credential.metro[num])

    def about_rent(self, driver, num):
        '''Заполняем страницу - про аренду'''
        self.num = num
        self.select_data(driver, Credential.data[num])
        self.select_rental_period(driver, Credential.period[num])
        self.select_color(driver, Credential.color[num])
