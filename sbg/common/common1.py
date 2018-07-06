from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class PySele():
    def __init__(self, brower):  # 初始化浏览器
        if brower == 'firefox' or brower == 'Firefox' or brower == 'f' or brower == 'F':
            driver = webdriver.Firefox()
        elif brower == 'Ie' or brower == 'ie' or brower == 'i' or brower == 'I':
            driver = webdriver.Ie()
        elif brower == 'Chrome' or brower == 'chrome' or brower == 'Ch' or brower == 'ch':
            driver = webdriver.Chrome()
        elif brower == 'PhantomJS' or brower == 'phantomjs' or brower == 'ph' or brower == 'phjs':
            driver = webdriver.PhantomJS()
        elif brower == 'Edge' or brower == 'edge' or brower == 'Ed' or brower == 'ed':
            driver = webdriver.Edge()
        elif brower == 'Opera' or brower == 'opera' or brower == 'op' or brower == 'OP':
            driver = webdriver.Opera()
        elif brower == 'Safari' or brower == 'safari' or brower == 'sa' or brower == 'saf':
            driver = webdriver.Safari()
        else:
            raise NameError('只能输入firefox,Ie,Chrome,PhantomJS,Edge,Opera,Safari')
        self.driver = driver

    def element_find(self, locator_type, locator):  # 定位
        if locator_type == 'id':
            element = self.driver.find_element_by_id(locator)
        elif locator_type == "name":
            element = self.driver.find_element_by_name(locator)
        elif locator_type == "class":
            element = self.driver.find_element_by_class_name(locator)
        elif locator_type == "link_text":
            element = self.driver.find_element_by_link_text(locator)
        elif locator_type == "xpath":
            element = self.driver.find_element_by_xpath(locator)
        elif locator_type == "tag":
            element = self.driver.find_element_by_tag_name(locator)
        elif locator_type == "css":
            element = self.driver.find_element_by_css_selector(locator)
        else:
            raise NameError("Please enter the  elements,'id','name','class','link_text','xpath','css','tag'.")
        return element

    def elements_find(self, locator_type, locator):  # 组定位
        if locator_type == 'id':
            element = self.driver.find_elements_by_id(locator)
        elif locator_type == "name":
            element = self.driver.find_elements_by_name(locator)
        elif locator_type == "class":
            element = self.driver.find_elements_by_class_name(locator)
        elif locator_type == "link_text":
            element = self.driver.find_elements_by_link_text(locator)
        elif locator_type == "xpath":
            element = self.driver.find_elements_by_xpath(locator)
        elif locator_type == "tag":
            element = self.driver.find_elements_by_tag_name(locator)
        elif locator_type == "css":
            element = self.driver.find_elements_by_css_selector(locator)
        else:
            raise NameError("Please enter the  elements,'id','name','class','link_text','xpath','css','tag'.")
        return element

    def element_wait(self, locator_type, locator, waittime=6):  # 等待
        if locator_type == "id":
            WebDriverWait(self.driver, waittime, 1).until(EC.presence_of_element_located((By.ID, locator)))
        elif locator_type == "name":
            WebDriverWait(self.driver, waittime, 1).until(EC.presence_of_element_located((By.NAME, locator)))
        elif locator_type == "class":
            WebDriverWait(self.driver, waittime, 1).until(EC.presence_of_element_located((By.CLASS_NAME, locator)))
        elif locator_type == "link_text":
            WebDriverWait(self.driver, waittime, 1).until(EC.presence_of_element_located((By.LINK_TEXT, locator)))
        elif locator_type == "xpath":
            WebDriverWait(self.driver, waittime, 1).until(EC.presence_of_element_located((By.XPATH, locator)))
        elif locator_type == "css":
            WebDriverWait(self.driver, waittime, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
        else:
            raise NameError("Please enter the  elements,'id','name','class','link_text','xpath','css'.")

    # 打开网页
    def open(self, url):
        self.driver.get(url)

    # 最大化浏览器
    def make_maxwindow(self):
        self.driver.maximize_window()

    # 设置窗口大小
    def set_windowsize(self, wide, hight):
        self.driver.set_window_size(wide, hight)

    # 发送内容
    def send_key(self, locator_type, locator, text):
        self.element(locator_type, locator)
        element = self.element(locator_type, locator)
        element.clear()
        element.send_keys(text)

    def clear(self, locator_type, locator):  # 清空
        self.element_wait(locator_type, locator)
        element = self.element(locator_type, locator)
        element.clear()

    def clic(self, locator_type, locator):  # 单击
        self.element_wait(locator_type, locator)
        element = self.element(locator_type, locator)
        element.click()

    def right_click(self, locator_type, locator):  # 右击
        self.element_wait(locator_type, locator)
        element = self.element(locator_type, locator)
        ActionChains(self.driver).context_click(element).perform()

    def move_element(self, locator_type, locator):  # 移动到
        self.element_wait(locator_type, locator)
        element = self.element(locator_type, locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def double_click(self, locator, locator_type):  # 双击
        self.element_wait(locator_type, locator)
        element = self.element(locator_type, locator)
        ActionChains(self.driver).double_click(element).perform()

    def drag_and_drop(self, locator_typelement, element, locator_type2, e2):  # 从element到e2
        self.element_wait(locator_typelement, element)
        emelement = self.element(locator_typelement, element)
        self.element_wait(locator_type2, e2)
        eme2 = self.element(locator_type2, e2)
        ActionChains(self.driver).drag_and_drop(emelement, eme2).perform()

    def click_text(self, text):  # 点击文字
        self.driver.find_element_by_link_text(text).click()

    def driver_close(self):  # 关闭
        self.driver.close()

    def dirver_kill(self):  # 退出
        self.driver.quit()

    def sublimit(self, locator_type, locator):  # 提交
        self.element_wait(locator_type, locator)
        element = self.element(locator_type, locator)
        element.sublimit()

    def driver_refresh(self):  # 刷新
        self.driver.refresh()

    def execute_script(self, sprit):  # 执行js
        self.driver.execute_script(sprit)

    def get_attribute(self, locator_type, locator, attribute):
        element = self.element(locator_type, locator)
        return element.get_attribute(attribute)

    def get_text(self, locator_type, locator):
        self.element_wait(locator_type, locator)
        element = self.element(locator_type, locator)
        return element.text

    def get_is_dis(self, locator_type, locator):
        self.element_wait(locator_type, locator)
        element = self.element(locator_type, locator)
        return element.is_displayed()

    def get_title(self, locator_type, locator):  # 获取title
        return self.driver.title

    def get_screen(self, file_path):  # 截屏
        self.driver.get_screenshot_as_file(file_path)

    def implicitly_wait(self, locator_type, locator):  # 等待
        self.driver.implicitly_wait((locator_type, locator))

    def alter_accpet(self):  # 允许
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        self.driver.switch_to.alert.dismiss()

    def switch_to_frame(self, locator_type, locator):  # 切换
        self.element_wait(locator_type, locator)
        if1 = self.element(locator_type, locator)
        self.driver.switch_to.frame(if1)
