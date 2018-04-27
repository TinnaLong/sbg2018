import unittest
from sbg.common.browser import BrowserEngine


class BaiduSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    def tearDownClass(cls):
        cls.driver.quit()


