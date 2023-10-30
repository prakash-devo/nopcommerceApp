import pytest
from selenium import webdriver
from PageObject.Loginpage import LoginPage
from Testcases.confitest import setup
from Utility.readproperty import ReadConfig
from Utility.customlogger import LogGen


class Test_001_login:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getpassword()

    logger = LogGen.loggen()
    @pytest.mark.regression
    def test_homepageTitle(self, setup):
        self.logger.info("**********Test_001_login***************")
        self.logger.info("**********Verifying Home page Title***************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("**********Home page Title Test pass***************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepageTitle.png")
            self.driver.close()
            self.logger.error("**********Home page Title Test fail ***************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("**********verifying login test ***************")

        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("**********Login test is passed ***************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("**********Login test is failed ***************")
            assert False
