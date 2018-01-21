# 自动化测试框架unittest
# 框架的优点: 1.组织和执行测试用例
# 2.封装了一些底层常用的方法,使测试用例更简洁

# 如何使用unittest
# 1.导包
import unittest

import time
from selenium import webdriver

# 2.我们自己写的测试用例类,需要集成unittest中的父类TestCase
from myTestCase import MyTestCase


class UpdateMemberInfoTest(MyTestCase):
    # 3.重写父类的setUp和tearDown方法

    # 4.声明一个测试用例方法, 需要以test作为方法名的开头
    def test_member_updating(self):
        print("这是一个测试用例方法, 这个方法用于修改会员信息的测试")
        driver = self.driver
        # 1.账号设置
        driver.find_element_by_link_text("账号设置").click()
        # 2.个人资料
        driver.find_element_by_partial_link_text("个人资料").click()
        # 3.修改具体信息
        # xpath中//表示相对路径
        # * 表示任意元素
        # []表示属性
        # @id id属性
        # driver.find_element_by_xpath("//*[@id=\"true_name\"]")
        # xpath的缺点: 定位速度很慢
        #  cssSelector优点: 快, 定位简单,准确
        driver.find_element_by_css_selector("#true_name").clear()
        driver.find_element_by_css_selector("#true_name").send_keys("张三")
        # 在css selector的定位方式中, 想用什么属性定位都可以, 只需要在两边加上一对中括号
        driver.find_element_by_css_selector("[value=\"2\"]").click()
        # selenium不能删除页面元素的属性, 只能通过javascript来实现
        # document.getElementById("date").removeAttribute("readonly")
        driver.execute_script('document.getElementById("date").removeAttribute("readonly")')
        driver.find_element_by_id("date").clear()
        driver.find_element_by_id("date").send_keys("1970-11-12")
        driver.find_element_by_id("qq").clear()
        driver.find_element_by_id("qq").send_keys("24325346")
        # 4.保存
        # css 中id属性前面加井号#
        # class 属性前面加小数点
        # 其他属性就加一对中括号
        driver.find_element_by_css_selector(".btn4").click()
        # 对弹出窗的操作
        # 在处理弹出框操作前,一定要加一个固定锝时间等待
        time.sleep(3)
        driver.switch_to.alert.accept()

        # driver.switch_to.alert.dismiss()

    def test_denglu(self):
        print("这是登录的测试用例")
        driver = self.driver
        # 1. 打开登录页面
        # http://localhost/index.php?m=user&c=public&a=login
        # 接口测试: 请求最重要的一个请求方式get, url地址, 有了这两部分,就可以构造请求,接收响应了
        driver.get("http://localhost/index.php?m=user&c=public&a=login")
        # 2. 输入用户名
        # 分为两部分, 找到用户名输入框, 对输入框输入文字
        # 元素的定位顺序: id---> name----> class
        driver.find_element_by_id("username").send_keys("changcheng")
        # 接下来手工主测一个账号, 写代码实现输入用户名和密码,点击登录按钮
        # 3.输入密码
        driver.find_element_by_name("password").send_keys("123654")
        # 4.点击登录
        driver.find_element_by_class_name("login_btn").click()

if __name__ == '__main__':
    unittest.main()