from selenium.webdriver.common.by import By
from .base_page import BasePage

class OrderPage(BasePage):
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION_OPTION = (By.XPATH, "//div[@class='select-search__select']//li")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[contains(text(), 'Далее')]")
    
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-arrow")
    RENTAL_PERIOD_OPTION = (By.XPATH, "//div[@class='Dropdown-option']")
    COLOR_CHECKBOX = (By.ID, "black")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Заказать')]")
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[2][contains(text(), 'Заказать')]")
    
    SUCCESS_MESSAGE = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def fill_personal_info(self, name, surname, address, metro_station, phone):
        self.input_text(self.NAME_INPUT, name)
        self.input_text(self.SURNAME_INPUT, surname)
        self.input_text(self.ADDRESS_INPUT, address)
        
        self.click_element(self.METRO_STATION_INPUT)
        metro_options = self.find_elements(self.METRO_STATION_OPTION)
        for option in metro_options:
            if metro_station in option.text:
                option.click()
                break
        
        self.input_text(self.PHONE_INPUT, phone)
    
    def click_next_button(self):
        self.click_element(self.NEXT_BUTTON)
    
    def fill_rental_info(self, date, rental_period, color, comment):
        self.input_text(self.DATE_INPUT, date)
        
        self.click_element(self.RENTAL_PERIOD_DROPDOWN)
        period_options = self.find_elements(self.RENTAL_PERIOD_OPTION)
        for option in period_options:
            if rental_period in option.text:
                option.click()
                break
        
        if color:
            color_locator = (By.ID, color)
            self.click_element(color_locator)
        
        if comment:
            self.input_text(self.COMMENT_INPUT, comment)
    
    def click_order_button(self):
        self.click_element(self.ORDER_BUTTON)
    
    def confirm_order(self):
        self.click_element(self.CONFIRM_ORDER_BUTTON)
    
    def is_success_message_displayed(self):
        try:
            return self.find_element(self.SUCCESS_MESSAGE, time=5).is_displayed()
        except:
            return False
    
    def get_success_message_text(self):
        return self.find_element(self.SUCCESS_MESSAGE).text