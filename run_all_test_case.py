# 这个python文件专门用来统一执行所有的测试用例
import unittest

# 胜多负少东方闪电是的防辐射服对方水电费哈哈哈 
# 如果这个文件不是最初的启动文件, 那么main代码块中的语句不能执行
if __name__ == '__main__':
    # 1.找到所有符合条件的测试用例
    # defaultTestLoader 默认的测试用例加载器
    # discover发现, 这句话的意思是把发现的所有测试用例加载到一起
    test_cases = unittest.defaultTestLoader.discover(".", pattern='*Test.py')
    # 2.执行这些测试用例
    # TextTestRunner 文本的测试用例运行器
    # run 执行, 这句话的意思是执行测试用例, 并且在控制台中显示文本的结果
    unittest.TextTestRunner().run(test_cases)