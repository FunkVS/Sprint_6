import pytest
import allure
from selenium.webdriver.common.by import By

class TestQuestions:
    QUESTIONS_AND_ANSWERS = [
        (
            "Сколько это стоит? И как оплатить?",
            "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
        ),
        (
            "Хочу сразу несколько самокатов! Так можно?",
            "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
        ),
        (
            "Как рассчитывается время аренды?",
            "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
        ),
        (
            "Можно ли заказать самокат прямо на сегодня?",
            "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
        ),
        (
            "Можно ли продлить заказ или вернуть самокат раньше?",
            "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
        ),
        (
            "Вы привозите зарядку вместе с самокатом?",
            "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
        ),
        (
            "Можно ли отменить заказ?",
            "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
        ),
        (
            "Я жизу за МКАДом, привезёте?",
            "Да, обязательно. Всем самокатов! И Москве, и Московской области."
        )
    ]
    
    @allure.feature("Вопросы о важном")
    @allure.story("Проверка раскрытия ответов на вопросы")
    @pytest.mark.parametrize("question_index,expected_answer", 
                            [(i, answer) for i, (question, answer) in enumerate(QUESTIONS_AND_ANSWERS)])
    def test_question_expands_correct_answer(self, main_page, question_index, expected_answer):
        with allure.step(f"Прокрутить к вопросам"):
            main_page.scroll_to_questions()
            main_page.wait_until_scooter_image_disapears()
        
        with allure.step(f"Кликнуть на вопрос №{question_index + 1}"):
            main_page.click_question(question_index)
        
        with allure.step("Проверить, что отображается правильный ответ"):
            actual_answer = main_page.get_answer_text(question_index)
            assert actual_answer == expected_answer, \
                f"Ожидался ответ: '{expected_answer}', но получен: '{actual_answer}'"
        
        with allure.step("Проверить, что ответ виден"):
            assert main_page.is_answer_displayed(question_index), "Ответ не отображается"