import pytest
import allure

from data import TestData


@allure.feature("Вопросы о важном")
class TestQuestions:
    
    @allure.title("Проверка раскрытия ответов на вопросы")
    @pytest.mark.parametrize("question_index,expected_answer", 
                            [(i, answer) for i, (question, answer) in enumerate(TestData.questions_data())])
    def test_question_expands_correct_answer(self, main_page, question_index, expected_answer):
        with allure.step(f"Прокрутить к вопросам"):
            main_page.scroll_to_questions()
            main_page.click_accept_cookie()
            main_page.wait_until_scooter_image_disapears()
        
        with allure.step(f"Кликнуть на вопрос №{question_index + 1}"):
            main_page.click_question(question_index)
        
        with allure.step("Проверить, что отображается правильный ответ"):
            actual_answer = main_page.get_answer_text(question_index)
            assert actual_answer == expected_answer, \
                f"Ожидался ответ: '{expected_answer}', но получен: '{actual_answer}'"
        
        with allure.step("Проверить, что ответ виден"):
            assert main_page.is_answer_displayed(question_index), "Ответ не отображается"