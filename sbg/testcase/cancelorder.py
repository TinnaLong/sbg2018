from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('http://om.motionglobal.com')
action = ActionChains(driver)

def login():
    username = driver.find_element_by_id('username')
    pwd = driver.find_element_by_id('password')
    #verify_code = driver.find_element_by_xpath('//html/body/div/form/div/div/div[3]/input')
    login_button = driver.find_element_by_id('sub')
    username.clear()
    username.send_keys('sharly')
    pwd.clear()
    pwd.send_keys('1qaz!QAZ')
    sleep(10)
    login_button.click()


def open_order_menu():
    order_menu = driver.find_element_by_xpath('//html/body/div[1]/div[4]/ul/li[2]/a')
    WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, "//html/body/div[1]/div[4]/ul/li[2]/a")))
    action.move_to_element(order_menu).perform()
    action.click()
    action.perform()


login()
open_order_menu()

order_id_input_box = driver.find_element_by_id('order_id')
order_id_input_box.clear()
order_id_input_box.send_keys("US0442278401G")
go_button = driver.find_element_by_id('button')
go_button.click()


edit_button = driver.find_element_by_xpath('//html/body/div[2]/div[3]/div/div/div[4]/div[2]/form/table/tbody/tr[1]/td[8]/div/a[1]')
WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH,'//html/body/div[2]/div[3]/div/div/div[4]/div[2]/form/table/tbody/tr[1]/td[8]/div/a[1]')))
action.move_to_element(edit_button).perform()
action.click()
action.perform()
