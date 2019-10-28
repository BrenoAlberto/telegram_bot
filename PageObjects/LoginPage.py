import PageObjects.utils as utils
from selenium.webdriver.common.by import By


class LoginPage:
    __LOGIN_HEADER = (By.CLASS_NAME, 'login_form_head')
    __PHONE_COUNTRY_INPUT = (By.XPATH, '//input[@name="phone_country"]')
    __PHONE_NUMBER_INPUT = (By.XPATH, '//input[@name="phone_number"]')
    __NEXT_BUTTON = (By.CLASS_NAME, 'login_head_submit_btn') 
    __OK_BUTTON = (By.XPATH, '//*[@id="ng-app"]/body/div[5]/div[2]/div/div/div[2]/button[2]') 
    # __PHONE_CODE_INPUT = (By.XPATH, '//input[@name="phone_code"]')

    def __init__(self, browser):
        self.browser = browser

    def login(self, data):
        phone_country, phone_number = data.values()
        self._input_phone_country(phone_country)
        self._input_phone_number(phone_number)
        self._click_next_button()
        self._click_ok_button()
        # self._wait_for_phone_code()

    def check_if_is_not_logged_in(self):
        if utils.element_does_exists(self.browser, *self.__LOGIN_HEADER):
            return True
        return False

    def _input_phone_country(self, phone_country):
        phone_country_input = utils.return_web_element(self.browser, *self.__PHONE_COUNTRY_INPUT)
        phone_country_input.clear()
        phone_country_input.send_keys(phone_country)

    def _input_phone_number(self, phone_number):
        phone_number_input = utils.return_web_element(self.browser, *self.__PHONE_NUMBER_INPUT)
        phone_number_input.send_keys(phone_number)

    def _click_next_button(self):
        next_button = utils.return_web_element(self.browser, *self.__NEXT_BUTTON)
        next_button.click()

    def _click_ok_button(self):
        ok_button = utils.return_web_element(self.browser, *self.__OK_BUTTON)
        ok_button.click()

    # def _wait_for_phone_code(self):
    #     if utils.element_does_exists(self.browser, *self.__PHONE_CODE_INPUT):
    #         return 