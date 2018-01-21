# 这个类的作用: 把setup方法和teardown方法,从测试用例类中分离分来
# 以后创建测试用例类时,就不需要重新写setUp和tearDown方法
# 13681477136
# 如何实现这样一个类?
# 原来的测试用例类继承了unittest.TestCase类, 所以它需要重写setUp和teardown方法
# 现在我们写一个myTestCase类也继承了unittest.TestCase类, 并且重写setUp和teardown方法,
# 以后所有的测试用例类只需要继承这个类, 是不是会自动继承父类中的setUp()和tearDown()
import unittest
import time
from selenium import webdriver
# 导包的快捷键是alt + enter

class MyTestCase(unittest.TestCase):
    # 重写父类的setUp和tearDown方法
    # setUp==beforeMethod, tearDown=afterMethod
    # setup方法和setupClass方法的区别
    # setup是每次测试用例都要重新执行一遍
    # setup--->登录--->teardown--->setUp---->修改会员信息--->teardown
    # setupclass是在类中所有测试用例之前只执行一遍
    # setUPClass--->登录--->修改会员信息---->tearDownClass
    # 测试用例之间的执行顺序是按照字母的顺序执行的,denglu是d开头,那么就比member_update是m开头的先执行
    @classmethod
    def setUpClass(self):
        print("这个方法类似于java中的beforeMethod")
        self.driver = webdriver.Chrome()
        # 隐式等待的
        # 优点: 会自动判断网页是否加载好, 一旦网页加载好, 就会执行下面的语句
        self.driver.implicitly_wait(30)
        # driver.maximize_window()

    @classmethod
    def tearDownClass(self):
        print("这个方法类似于java中的afterMethod")
        time.sleep(15)
        self.driver.quit()