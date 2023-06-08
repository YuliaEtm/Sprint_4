from selenium.webdriver.common.by import By

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
