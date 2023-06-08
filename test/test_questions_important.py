import time

import allure
import pytest

from locators import Locators
from pages.page_questions_important import PageQuestionsImportant

ansver = ['Сутки — 400 рублей. Оплата курьеру — наличными или картой.',
          'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.',
          'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.',
          'Только начиная с завтрашнего дня. Но скоро станем расторопнее.',
          'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.',
          'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.',
          'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.',
          'Да, обязательно. Всем самокатов! И Москве, и Московской области.']


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
    assert accordion_ansver[num].text == ansver[num]
