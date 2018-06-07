import time

from testcases.ranzhitest.admin_log_logout import RanZhiAdminLogin
import unittest
import HTMLTestRunner_PY3
if __name__=="__main__":
    suite=unittest.TestSuite()
    load=unittest.TestLoader()
    suite.addTests(load.loadTestsFromTestCase(RanZhiAdminLogin))
    #unittest.TextTestRunner().run(suite)
    fp = open('reports/my_report_%s.html'%time.strftime("%Y-%m-%d %H-%M-%S"), 'wb')
    runner = HTMLTestRunner_PY3.HTMLTestRunner(
        stream=fp,
        title='然之系统 test',
        description='登录然之.'
        )
    runner.run(suite)