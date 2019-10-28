from PageObjects.BasePage import BasePage
from PageObjects.LoginPage import LoginPage
from PageObjects.MainPage import MainPage
import time

def start_watcher():
    base_page = BasePage()
    browser = base_page.browser

    login_page = LoginPage(browser)

    if login_page.check_if_is_not_logged_in():
        login_page.login({ 'phone_country': 55, 'phone_number': 31975325480 })

    main_page = MainPage(browser)
    main_page.watch_channel('testedotelegra')

try:
    start_watcher()
    time.sleep(520)
except KeyboardInterrupt:
    print('Watcher interrompido pelo usuario')