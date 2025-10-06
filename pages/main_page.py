from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage


class MainPage(BasePage):
    QUESTION_LOCATORS = [
        (By.ID, "accordion__heading-0"),
        (By.ID, "accordion__heading-1"),
        (By.ID, "accordion__heading-2"),
        (By.ID, "accordion__heading-3"),
        (By.ID, "accordion__heading-4"),
        (By.ID, "accordion__heading-5"),
        (By.ID, "accordion__heading-6"),
        (By.ID, "accordion__heading-7")
    ]
    
    ANSWER_LOCATORS = [
        (By.ID, "accordion__panel-0"),
        (By.ID, "accordion__panel-1"),
        (By.ID, "accordion__panel-2"),
        (By.ID, "accordion__panel-3"),
        (By.ID, "accordion__panel-4"),
        (By.ID, "accordion__panel-5"),
        (By.ID, "accordion__panel-6"),
        (By.ID, "accordion__panel-7")
    ]

    SCOOTER_IMAGE = (By.XPATH, "//img[contains(@src, 'scooter.png')]")
    ORDER_BUTTON_TOP = (By.XPATH, "//button[contains(text(), 'Заказать') and parent::div[@class='Header_Nav__AGCXC']]")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[contains(text(), 'Заказать') and parent::div[@class='Home_FinishButton__1_cWm']]")

    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

    ACCEPT_COOKIE = (By.ID, "rcc-confirm-button")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(self.base_url)

    def wait_until_scooter_image_disapears(self):
        self.wait_for_element_hidden(self.SCOOTER_IMAGE)

    def click_accept_cookie(self):
        self.click_element(self.ACCEPT_COOKIE)

    def click_question(self, question_index):
        locator = self.QUESTION_LOCATORS[question_index]
        self.click_element(locator)
    
    def get_answer_text(self, answer_index):
        locator = self.ANSWER_LOCATORS[answer_index]
        return self.find_element(locator).text
    
    def is_answer_displayed(self, answer_index):
        locator = self.ANSWER_LOCATORS[answer_index]
        try:
            return self.find_element(locator).is_displayed()
        except:
            return False
    
    def click_order_button_top(self):
        self.click_element(self.ORDER_BUTTON_TOP)
    
    def click_order_button_bottom(self):
        self.click_element(self.ORDER_BUTTON_BOTTOM)
    
    def click_scooter_logo(self):
        self.click_element(self.SCOOTER_LOGO)
    
    def click_yandex_logo(self):
        self.click_element(self.YANDEX_LOGO)
    
    def scroll_to_questions(self):
        questions_section = (By.ID, "accordion__heading-7")
        self.scroll_to_bottom_of_element(questions_section)
        
    def scroll_to_bottom_order_button(self):
        self.scroll_to_element(self.ORDER_BUTTON_BOTTOM)
    
    def is_main_page_loaded(self):
        return self.wait_for_page_loaded(self.base_url)
    
    def is_dzen_page_loaded(self):
        return self.wait_for_page_loaded("dzen.ru")

    def get_current_window(self):
        return self.current_window_handle()
    
    def close_and_switch_window(self, window):
        return self.close_and_switch_to_selected_window(window)
    