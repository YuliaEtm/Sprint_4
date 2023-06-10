import time

import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait

from data import Credential
from locators import Locators
from pages.page_questions_important import PageQuestionsImportant


@pytest.mark.parametrize('num', [0, 1, 2, 3, 4, 5, 6, 7])
@allure.description('Проверка списка из восьми вопросов и ответов, в разделе "Вопросы о важном"')
@allure.step('проверка вопроса №{num}')
def test_questions_important(driver, num):
    page_questions = PageQuestionsImportant(driver)
    page_questions.go_to_site('https://qa-scooter.praktikum-services.ru/')
    page_questions.scroll(driver)
    accordion_quest = page_questions.find_elements_located(Locators.QUESTIONS_ALL)
    accordion_quest[num].click()
    accordion_ansver = page_questions.find_elements_located(Locators.ANSWER_ALL)

    time.sleep(3)
    #здесь я не знаю как задать ожидание, это не элемент страницы, а создаваемый список, неявное ожидание не работает.
    assert accordion_ansver[num].text == Credential.ansver[num]
