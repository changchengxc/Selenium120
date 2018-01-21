# 0. 打开浏览器
import time
from selenium import webdriver
# 导入代码库, 就是我发给你的selenium.zip,这里是selenium源码
# 从 selenium这个项目中, 导入 webdriver这个模块
# webdriver的意思是网络驱动, 是用来操作浏览器的
# 不管想打开什么浏览器,都要把相应的驱动文件放到python home路径下面
# 驱动文件在selenium官网下载, 版本号要求和浏览器的版本好匹配
driver = webdriver.Chrome()

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

# selenium首先在登录成功页面找是存在按钮,如果不存在,那么程序直接保存,后面语句就不会执行了
# 所以我们需要让我们的程序,休息一点时间,等页面加载到个人中心时,在执行
# 贯标放在红色波浪线上, 按alt+enter, 选择import,选择time

time.sleep(5)
# driver.find_element_by_link_text("进入商城购物").click()
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
