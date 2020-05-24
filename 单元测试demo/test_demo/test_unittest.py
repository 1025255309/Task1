import unittest  # 导入unittest库


class demo(unittest.TestCase):  # 创建一个类继承于unittest.TestCase
    @classmethod
    def setUpClass(cls) -> None:  # setupclass和teardownclass是cls的方法，所以前面要加一个@classmethod
        print("setup class")

    @classmethod
    def tearDownClass(cls) -> None:
        print("teardown class")

    def setUp(self) -> None:  # 创建一个setup方法，准备测试资源
        print("setup")

    def tearDown(self) -> None:  # 创建一个teardown方法，回收资源,如清空缓存，断开数据库连接，清除资源文件的操作
        print("teardown")

    def testcase01(self):  # 创建一个testcase01
        print("testcase01")
        self.assertEqual(2, 2, "判断相等")  # unittest提供了多种断言方法供测试使用
        self.assertIn('h',"this")

    @unittest.skip  # 跳过执行这个用例
    # @unittest.skipIf(1+1==2)     # 如果满足if条件则跳过执行这个用例
    def testcase02(self):  # 创建一个testcase01
        print("testcase02")
        self.assertEqual(1, 1, "判断相等")  # unittest提供了多种断言方法供测试使用
        # self.assertIn('h',"this")

    def testcase03(self):  # 创建一个testcase01
        print("testcase03")
        self.assertEqual(3, 3, "判断相等")  # unittest提供了多种断言方法供测试使用
        # self.assertIn('h',"this")

class demo1(unittest.TestCase):
    def test_demo1_case0(self):
        print("test demo1 case0")

    def test_demo1_case1(self):
        print("test demo1 case1")

class demo2(unittest.TestCase):
    def test_demo2_case0(self):
        print("test demo2 case0")

    def test_demo2_case1(self):
        print("test demo2 case1")

if __name__ == '__main__':  # 创建一个入口函数main
    """
    #unittest.main()  # 通过unittest.main()方法可以将当前页面中所有以test开头的测试用例都加载出来，并且执行一遍
    suite=unittest.TestSuite()
    suite.addTest(demo("testcase01"))
    #suite.addTest(demo1("test_demo1_case0"))
    #suite.addTests(demo1("test_demo1_case0","test_demo1_case1"))？？？？？？
    unittest.TextTestRunner().run(suite)  # unittest有测试套件（管理一条或多条测试用例）的概念，我们可以使用test runner方法来执行这个套件中的测试用例
    """
    # suite1=unittest.TestLoader().loadTestsFromTestCase("demo1")
    # suite2=unittest.TestLoader().loadTestsFromTestCase("demo2")
    # suiteall=unittest.TestCase([suite1,suite2])
    # unittest.TextTestRunner().run(suiteall)

    discover = unittest.defaultTestLoader.discover("../", pattern ="test*.py")
    unittest.TextTestRunner().run(discover)