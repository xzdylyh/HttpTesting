import os
import unittest
import ddt
from HttpTesting.library.scripts import (load_case_data, get_run_flag)
from HttpTesting.library import HTMLTESTRunnerCN
from HttpTesting.library.http import HttpWebRequest
from HttpTesting.library.case import exec_test_case
from HttpTesting.globalVar import gl
from HttpTesting.library.emailstmp import EmailClass
from HttpTesting.library.case_queue import case_exec_queue

#########################################
#单个文件Debug时启用
# case_exec_queue.put("POS_INFO.yaml")
########################################3

'''
天子星－云财务接口场景
'''
@ddt.ddt
class TestCaseExec(unittest.TestCase):

    def setUp(self):
        pass


    @ddt.data(*load_case_data())
    def test_case(self, data):
        # 用例描述
        # self._testMethodName = "方法名"
        self._testMethodDoc = data[0]['Desc']
        #执行yaml测试用例数据
        exec_test_case(self, data)
        



if __name__=="__main__":


    suite = unittest.TestSuite()
    tests = [unittest.TestLoader().loadTestsFromTestCase(TestCaseExec)]
    suite.addTests(tests)

    #输出report.html路径
    print(gl.reportFile)

    with open(gl.reportFile, 'wb') as fp:
        runner = HTMLTESTRunnerCN.HTMLTestRunner(
            stream=fp,
            title= '接口自动化测试报告',
            description= '详细测试用例结果',  # 不传默认为空
            tester= "微生活－测试组"  # 测试人员名字，不传默认为小强
        )
        # 运行测试用例
        runner.run(suite)

    # email = EmailClass()
    # email.send(gl.reportFile)


