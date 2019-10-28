from selenium.common.exceptions import NoSuchElementException
import time


def return_web_element(driver, *element):
    return driver.find_element(*element)

def return_web_elements(driver, *element):
    return driver.find_elements(*element)

def element_does_exists(driver, *element):
    try:
        driver.find_element(*element)
        return True
    except NoSuchElementException:
        return False


def wait_element_to_be_visible(driver, *element):
    try:
        time.sleep(3)
        driver.find_element(*element)
    except NoSuchElementException:
        wait_element_to_be_visible(driver, *element)

def wait_elements_to_be_visible(driver, *element):
    try:
        time.sleep(3)
        driver.find_elements(*element)
    except NoSuchElementException:
        wait_elements_to_be_visible(driver, *element)
