from locators import Locators
from pages.page_base import BasePage


class PageQuestionsImportant(BasePage):

    def scroll(self, driver):
        element = driver.find_element(*Locators.QUESTIONS_IMPORTANT)
        driver.execute_script("arguments[0].scrollIntoView();", element)
