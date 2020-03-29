# 导包
import unittest

# 定义测试套件
from Test_IHRM.tool.HTMLTestReportCN import HTMLTestRunner

suite = unittest.defaultTestLoader.discover("./", pattern="test*.py")
# 获取报告存储文件流，并实例化HTMLTestRunner 调用run方法执行suite
with open("../report/report.html","wb")as f:
    HTMLTestRunner(stream=f).run(suite)