import PageObjects.utils as utils
from selenium.webdriver.common.by import By

class MainPage:
    __TELEGRAM_HEADER = (By.CLASS_NAME, 'tg_head_btn')
    __MESSAGE_LIST = (By.XPATH, '//*[@id="ng-app"]/body/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div')

    def __init__(self, browser):
        self.browser = browser
        utils.wait_element_to_be_visible(self.browser, *self.__TELEGRAM_HEADER)

    def watch_channel(self, channel_at):
        self.browser.get(f'https://web.telegram.org/#/im?p=@{channel_at}')
        message_list = self.__get_message_list()
        last_message_sended = message_list[-1]
        self.__get_message_data(last_message_sended)
        While(True):
            last_message_sended = self.__get_last_message_sended_after_message(last_message_sended)
            __get_message_data

    
    def __get_message_list(self):
        utils.wait_elements_to_be_visible(self.browser, *self.__MESSAGE_LIST)
        message_list = utils.return_web_elements(self.browser, *self.__MESSAGE_LIST)

    def __get_last_message_sended_after_message(self, message):


    def __get_message_data(self, message):
        __MESSAGE_AUTHOR = (By.CLASS_NAME, 'im_message_author')
        __MESSAGE_DATE = (By.CLASS_NAME, 'im_message_date_text')
        __MESSAGE_TEXT = (By.CLASS_NAME, 'im_message_text')

        message_author = utils.return_web_element(message, *__MESSAGE_AUTHOR)
        message_date = utils.return_web_element(message, *__MESSAGE_DATE)
        message_text = utils.return_web_element(message, *__MESSAGE_TEXT)

        author = message_author.get_attribute('innerHTML')
        date = message_date.get_attribute('data-content')
        text = message_text.get_attribute('innerHTML')