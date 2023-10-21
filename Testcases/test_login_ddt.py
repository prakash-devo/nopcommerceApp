import time

import pytest
from selenium import webdriver
from PageObject.Loginpage import LoginPage
from Testcases.confitest import setup
from Utility.readproperty import ReadConfig
from Utility.customlogger import LogGen
from Utility import xlutils

class Test_002_DDT_login:
    baseUrl = ReadConfig.getApplicationURL()
    path=".//TestData/Testdata.xlsx"
    username = ReadConfig.getUseremail()
    password = ReadConfig.getpassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_login_ddt(self, setup):
        self.logger.info("**********test_login_ddt ***************")
        self.logger.info("**********Verifying _login_ddt ***************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)

        self.rows=xlutils.getrowCount(self.path,'Sheet1')
        print('number of rows:',self.rows)

        lst_status=[]
        for r in range(2,self.rows+1):
            self.user=xlutils.readdata(self.path,'Sheet1',r,1)
            self.password=xlutils.readdata(self.path,'Sheet1',r,2)
            self.exp=xlutils.readdata(self.path,'Sheet1',r,3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clicklogin()
            time.sleep(6)
            act_title = self.driver.title
            exp_title="Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.exp=="Pass":
                    self.logger.info("***passed**")
                    self.lp.cliccklogout()
                    lst_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("*****fail*******")
                    self.lp.cliccklogout()
                    lst_status.append("fail")
            elif act_title != exp_title:
                if self.exp=="Pass":
                    self.logger.info("***failed***")
                    lst_status.append("fail")
                elif self.exp=="Fail":
                    self.logger.info("**passed***")
                    lst_status.append("pass")
        if "Fail" not in lst_status:
            self.logger.info("login DDT test passed")
            self.driver.close()
            assert True
        else:
            self.logger.info('login DDT test is failed')
            self.driver.close()
            assert False

        self.logger.info("end of the DDT test")
        self.logger.info("*************complted**")
