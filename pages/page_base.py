import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
    @allure.step('переход на сайт {url}')
    def go_to_site(self, url):
        return self.driver.get(url)

    def find_elements_located(self, locator, time=3):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f'notfind{locator}')

    def find_element_located(self, locator, time=3):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'notfind{locator}')

    def cook_ok(self, time=3):
        locator = Locators.COOKIE
        WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator)).click()

    def scooter_picture(self, time=3):
        WebDriverWait(self.driver, time).until(
            EC.text_to_be_present_in_element_attribute(Locators.SCOOTER_TEXT, 'src', "/assets/scooter.png"))

    # def scroll(self, driver):
    #     element =  driver.find_element(*Locators.QUESTIONS_IMPORTANT)
    #     driver.execute_script("arguments[0].scrollIntoView();", element)