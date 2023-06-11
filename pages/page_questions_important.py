from locators import Locators
from pages.page_base import BasePage


class PageQuestionsImportant(BasePage):
# если убрать метод scroll В page_base , то в этот клас (и файл) становятся не нужными. Их тоже убирать?
    def scroll(self, driver):
        element = driver.find_element(*Locators.QUESTIONS_IMPORTANT)
        driver.execute_script("arguments[0].scrollIntoView();", element)


