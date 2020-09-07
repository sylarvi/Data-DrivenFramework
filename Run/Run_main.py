import unittest
import os
import time
from Testreport import HTMLTestRunner
from PublicConfig.Path_var import project_dir

# 设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.')) + '/Testreport/'
print(report_path)
# 获取系统当前时间
now = time.strftime("%Y%m%d%H%M%S", time.localtime())

# 设置报告名称格式
HtmlFile = report_path + now + "testreport.html"
fp = open(HtmlFile, "wb")

# case路径
case_path = project_dir + '/UnittestCase'
print(case_path)
suite = unittest.TestLoader().discover(case_path, pattern="test*.py", top_level_dir=None)

if __name__ == '__main__':
    # 执行所有测试用例
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"接口自动化测试报告", description=u"用例测试情况")
    # 开始执行测试套件
    runner.run(suite)
    fp.close()