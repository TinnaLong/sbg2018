from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.smartbuyglasses.com")
WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, "//div[@id='EDM-popUp']/div[1]/div/a[1]")))
driver.find_element_by_xpath("//div[@id='EDM-popUp']/div[1]/div/a[1]").click()
WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, "//li[@id='signin_li']/a/span")))
login_loc = driver.find_element_by_xpath("//li[@id='signin_li']/a/span")
action = ActionChains(driver)
action.move_to_element(login_loc).perform()
sleep(1)
action.move_to_element(driver.find_element_by_xpath("//li[@id='signin_li']/div/div/span/a")).perform()
action.click()
action.perform()
# driver.find_element_by_xpath("//li[@id='signin_li']/div/div/span/a").click()
driver.find_element_by_id("username").send_keys("12345678@qq.com")
driver.find_element_by_id("password").send_keys("156756789")
driver.find_element_by_xpath("//form[@id='loginFormNew']/span").click()





if __name__ == '__main__':
    driver.quit()

