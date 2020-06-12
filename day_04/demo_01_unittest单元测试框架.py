# coding=utf-8

import unittest
from HTMLTestRunner import HTMLTestRunner
from time import strftime

def jia(x: int, y: int) -> int:
    print("jia")
    return x + y


def jian(x, y):
    print("jian")
    return x - y


def cheng(x, y):
    print("cheng")
    return x * y


def chu(x, y):
    print("chu")
    return x / y


class TestMath(unittest.TestCase):

    def setUp(self) -> None:
        print("我是setup 在每一条用例执行前执行")

    def tearDown(self) -> None:
        print("我是teardown")

    @classmethod
    def setUpClass(cls) -> None:
        print("我是setUp class 在整个用例执行前执行")

    @classmethod
    def tearDownClass(cls) -> None:
        print("我是tearDown Class 在整个用例执行完执行")


    def test_jia(self):
        assert jia(10, 10) == 20

    # @unittest.skip
    def test_jian(self):
        assert jian(10, 10) == 1

    def test_cheng(self):
        assert cheng(10, 10) == 100

    def test_chu(self):
        assert chu(10, 10) == 1


if __name__ == "__main__":
    # unittest.main() # 自动寻找以test_开头的测试函数并添加到测试用例集合

    suite = unittest.TestSuite()
    suite.addTest(TestMath('test_jia'))
    suite.addTest(TestMath('test_jian'))
    suite.addTest(TestMath('test_cheng'))
    suite.addTest(TestMath('test_chu'))

    # runner = unittest.TextTestRunner()
    f = open(f'{strftime("%Y-%m-%d %H-%M-%S")}.html', mode='wb')
    h = HTMLTestRunner(stream=f, verbosity=2, title="自动化测试", description="20200612_zero_自动化测试")
    h.run(suite)
