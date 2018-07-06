from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC


def driver_path():
    return r"C:\Users\xua\Downloads\chromedriver_win32\chromedriver.exe"


def base_url():
    return "https://www.smartbuyglasses.com"


def get_current_time():
    format_time = "%a %b %d %H:%M:%S %Y"
    return datetime.now().strftime(format_time)


def time_different(start_time, end_time):
    format_time = "%a %b %d %H:%M:%S %Y"
    return datetime.strptime(end_time, format_time) - datetime.strptime(start_time, format_time)


def is_element_visible(self, element):
    driver = self.driver
    try:
        the_element = EC.visibility_of_element_located(element)
        assert the_element(driver)
        flag = True
    except IOError:
        flag = False
    return flag


def is_presence_of_element(self, element):
    driver = self.driver
    try:
        the_element = EC.presence_of_element_located(element)
        assert the_element(driver)
        flag = True
    except IOError:
        flag = False
    return flag


def is_element_exist(self, element):
    flag = True
    driver = self.driver
    try:
        driver.find_element_by_css_selector(element)
        return flag
    except IOError:
        flag = False
        return flag
