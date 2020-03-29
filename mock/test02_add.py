"""
    目标：mock对象使用
    需求：测试加法函数
"""
# 定义一个加法函数（未实现）
import unittest
from unittest.mock import Mock

def add(a,b):
    """该功能未实现"""
    pass


# 定义测试类
class TestAdd(unittest.TestCase):

    # 定义测试方法
    def test_add(self):
        # 获取mock对象 并设置行为 替换要替换的对象
        # 重点：return_value 设置行为
        add=Mock(return_value=10, side_effect=NameError)

        result = add(1,1)
        self.assertEqual(result, 2)
        # 调用进行测试
