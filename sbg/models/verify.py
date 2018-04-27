from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import unittest


driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.maximize_window()


class ECExample(unittest.TestCase):

    """Verify the title is accord with expect"""
    def verify_title_is(self, title_name):
        title_is = EC.title_is(title_name)
        self.assertTrue(title_is(driver))

    """Verify the title contains stt"""
    def verify_title_contains(self, contain_str):
        title_should_contains = EC.title_contains(contain_str)
        self.assertTrue(title_should_contains(driver))
