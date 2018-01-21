from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    # 通过成员变量, 保存页面元素的定位信息
    url = "http://localhost/index.php?m=user&c=public&a=login"
    username_input_loc = (By.ID, "username")
    password_input_loc = (By.ID, "password")
    login_button_loc = (By.CLASS_NAME, "login_btn")


    # __init__表示构造方法
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)

    # 输入用户名的方法
    def input_username(self, username):
        self.driver.find_element(*self.username_input_loc).send_keys(username)

    def input_password(self, password):
        self.driver.find_element(*self.password_input_loc).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button_loc).click()

    def login(self, username, password):
        self.open()
        self.input_username(username)
        self.input_password(password)
        self.click_login_button()



#   封装思路
#     def input_username2(self):
#         driver = webdriver.Chrome()
# #         .... 最早的版本
#         driver.find_element_by_id("username").send_keys("changcheng")
#         # 第一次优化
#         driver.find_element(By.ID, "username").send_keys("changcheng")
# #        # 第二次优化
#         username_input_loc = (By.ID, "username")
#         driver.find_element(*username_input_loc).send_keys("changcheng")
#           如果不加星号, 传进来的是一个元组,
#           星号的作用就是把外面的括号去掉, 比如(By.ID, "username")变成 By.ID, "username"





