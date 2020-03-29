import unittest

import Test_IHRM.api
from parameterized import parameterized
from Test_IHRM.api.api_login import ApiLogin
from Test_IHRM.tool.ge_log import GetLog
# 获取数据
from Test_IHRM.tool.assert_common import assert_common
from Test_IHRM.tool.read_json import ReadJson

# log = GetLog.get_log()


def get_data():
    datas = ReadJson("login.json").read_json()

    arrs = []
    for data in datas.values():
        arrs.append((
            data.get("url"),
            data.get("mobile"),
            data.get("password"),
            data.get("code"),
            data.get("message")))
    return arrs


class TestLogin(unittest.TestCase):
    def setUp(self):
        # 获取api_login对象
        self.login = ApiLogin()
        # log.info("正在初始化 ApiLogin对象：{}".format(self.login))

    # 登录测试方法
    @parameterized.expand(get_data())
    def test_login(self, url,mobile, password, code, message):
        # 调用登录方法
        result = self.login.api_login(url,mobile, password)
        print(result)
        # 断言状态码
        self.assertEqual(code,result.json().get("code"))
        # 断言 登录状态
        # self.assertTrue(result.json().get("status_code"))
        # 断言 message
        self.assertEqual(message, result.json().get("message"))

        # 提取data
        Test_IHRM.api.headers['Authorization'] = "Bearer " + result.json().get('data')  # 提取 data值，并追加到headers

        # 查看此时header信息：
        print("追加data后,headers信息内容为：", Test_IHRM.api.headers)

        # 调用公共断言
        # assert_common(self, result)


if __name__ == '__main__':
    unittest.main()
