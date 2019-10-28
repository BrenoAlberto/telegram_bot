from selenium import webdriver
from utils import get_path_from_root_dir

class BasePage:

    def __init__(self):
        self.browserProfile = webdriver.ChromeOptions()
        chrome_driver = get_path_from_root_dir('bin/chromedriver.exe')

        user_data_dir = get_path_from_root_dir('data/User_Data')
        self.browserProfile.add_argument(f"--user-data-dir={user_data_dir}")

        self.browserProfile.add_argument("user-agent=[user-agent string]")
        self.browserProfile.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")

        self.browser = webdriver.Chrome(chrome_driver, chrome_options=self.browserProfile)
        self.browser.get('https://web.telegram.org/')        

    def exit_browser(self):
        self.browser.quit()
