from sbg.common import driver

chrome_driver = driver;
driver = chrome_driver.browser("Chrome")

driver.get("http://www.baidu.com")
