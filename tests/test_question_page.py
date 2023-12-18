import allure
import pytest
from conftest import driver
from pages.main_page import MainPage
from locators.main_site_locators import MainSiteLocators
from data import AnswersText


class TestQuestionsPage:
    @allure.title('Проверка выпадающих ответов на вопросы о важном')
    @allure.description('Проверяем, что при клике на вопросы о важном 1-8 будут развёрнуты ответы')
    @pytest.mark.parametrize('question, answer, right_answer',
                             [
                                 (MainSiteLocators.FIRST_QUESTION, MainSiteLocators.FIRST_ANSWER, AnswersText.text_answer_1),
                                 (MainSiteLocators.SECOND_QUESTION, MainSiteLocators.SECOND_ANSWER, AnswersText.text_answer_2),
                                 (MainSiteLocators.THIRD_QUESTION, MainSiteLocators.THIRD_ANSWER, AnswersText.text_answer_3),
                                 (MainSiteLocators.FOURTH_QUESTION, MainSiteLocators.FOURTH_ANSWER, AnswersText.text_answer_4),
                                 (MainSiteLocators.FIFTH_QUESTION, MainSiteLocators.FIFTH_ANSWER, AnswersText.text_answer_5),
                                 (MainSiteLocators.SIXTH_QUESTION, MainSiteLocators.SIXTH_ANSWER, AnswersText.text_answer_6),
                                 (MainSiteLocators.SEVENTH_QUESTION, MainSiteLocators.SEVENTH_ANSWER, AnswersText.text_answer_7),
                                 (MainSiteLocators.EIGHTH_QUESTION, MainSiteLocators.EIGHTH_ANSWER, AnswersText.text_answer_8)
                             ])
    def test_answers_to_questions(self, question, answer, right_answer, driver):
            MainPage(driver).click_button_cookies()
            MainPage(driver).find_questions()
            MainPage(driver).click_to_element(question)
            MainPage(driver).wait_for_element(answer)
            right_text = driver.find_element(*answer).text
            assert right_text == right_answer
