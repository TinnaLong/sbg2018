from selenium import webdriver
import sys
sys.path.append('../')
from models.verify import ECExample


driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.baidu.com")
ECExample.verify_title_is(driver, "https://www.baidu.com")
