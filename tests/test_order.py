import pytest
import allure

from data import TestData

@allure.feature("Заказ самоката и навигация")
@allure.story("Позитивные сценарии заказа")
class TestOrder:

    @allure.title("Успешный заказ через верхнюю кнопку")
    @pytest.mark.parametrize("order_data", TestData.order_data())
    def test_order_through_top_button_success(self, main_page, order_page, order_data):
        main_page.click_accept_cookie()
        with allure.step("Кликнуть на верхнюю кнопку 'Заказать'"):
            main_page.click_order_button_top()
        
        with allure.step("Заполнить информацию о заказе"):
            order_page.fill_order_data(order_data)

        with allure.step("Подтвердить заказ"):
            order_page.click_order_button()
            order_page.confirm_order()
        
        with allure.step("Проверить сообщение об успешном заказе"):
            assert order_page.is_success_message_displayed(), "Сообщение об успешном заказе не отображается"

    @allure.title("Успешный заказ через нижнюю кнопку")
    @pytest.mark.parametrize("order_data", TestData.order_data())
    def test_order_through_bottom_button_success(self, main_page, order_page, order_data):
        main_page.click_accept_cookie()
        with allure.step("Прокрутить к нижней кнопке 'Заказать'"):
            main_page.scroll_to_bottom_order_button()
        
        with allure.step("Кликнуть на нижнюю кнопку 'Заказать'"):
            main_page.click_order_button_bottom()
        
        with allure.step("Заполнить информацию о заказе"):
            order_page.fill_order_data(order_data)

        with allure.step("Подтвердить заказ"):
            order_page.click_order_button()
            order_page.confirm_order()
        
        with allure.step("Проверить сообщение об успешном заказе"):
            assert order_page.is_success_message_displayed(), "Сообщение об успешном заказе не отображается"
    
    @allure.title("Переход на главную страницу через логотип Самоката")
    def test_scooter_logo_navigation(self, main_page):
        with allure.step("Кликнуть на логотип Самоката"):
            main_page.click_scooter_logo()
        
        with allure.step("Проверить URL текущей страницы"):
            assert main_page.is_main_page_loaded(), \
                f"Ожидался переход на главную страницу, но текущий URL: {main_page.get_current_url()}"
    
    @allure.title("Переход на Дзен через логотип Яндекса")
    def test_yandex_logo_navigation(self, main_page):
        with allure.step("Запомнить текущее окно"):
            main_window = main_page.get_current_window()
        
        with allure.step("Кликнуть на логотип Яндекса"):
            main_page.click_yandex_logo()
        
        with allure.step("Переключиться на новое окно"):
            main_page.switch_to_new_window()
        
        with allure.step("Проверить, что открылась страница Дзен"):
            assert main_page.is_dzen_page_loaded(), \
                f"Ожидался переход на Дзен, но текущий URL: {main_page.get_current_url()}"
        
        with allure.step("Закрыть новое окно и вернуться к основному"):
            main_page.close_and_switch_window(main_window)