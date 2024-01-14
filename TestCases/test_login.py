####### final code use this do not lost
#
# import pytest
# from selenium import webdriver
# from pageObjects.LoginPage import LoginPage
# from Utilities.readProperties import ReadConfig
# from Utilities.customLogger import LogGen
#
#
# class TestLogin:
#     baseURL = ReadConfig.getApplicationURL()
#     username = ReadConfig.getUseremail()
#     password = ReadConfig.getPassword()
#
#     logger = LogGen.loggen()
#
#     def test_homePageTitle(self, setup):
#         self.logger.info("**************TC_001*********************")
#         self.logger.info("************** verifying Home page title ********************")
#         self.driver = setup
#         self.driver.get(self.baseURL)
#         act_title = self.driver.title
#         # assert act_title == "Log in to 3", "Title does not match expected"
#         if act_title == "Log in to 3":
#             assert True
#             self.driver.close()
#             self.logger.info("************** Home page title test is passed ********************")
#         else:
#             self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
#             self.driver.close()
#             self.logger.info("************** Home page title test is Failed ********************")
#             assert False
#
#     def test_Login(self, setup):
#         self.logger.info("************** verifying login test ********************")
#         self.driver = setup
#         self.driver.get(self.baseURL)
#         self.lp = LoginPage(self.driver)
#         self.lp.setUserName(self.username)
#         self.lp.setPassword(self.password)
#         self.lp.clickLogin()
#
#         act_title = self.driver.title
#         # assert act_title == "Analytics", "Login unsuccessful"
#         if act_title == "Analytics":
#             assert True
#             self.driver.close()
#             self.logger.error("************** login test is passed ********************")
#         else:
#             self.driver.save_screenshot(".\\Screenshots\\" + "test_Login.png")
#             self.driver.close()
#             self.logger.error("************** login test is Failed ********************")
#             assert False
#

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# TestCases/test_login.py

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

class TestLogin:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("**************TC_001*********************")
        self.logger.info("************** verifying Home page title ********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Log in to 3":
            assert True
            self.driver.close()
            self.logger.info("************** Home page title test is passed ********************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.info("************** Home page title test is Failed ********************")
            assert False

    def test_Login(self, setup):
        self.logger.info("************** verifying login test ********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        act_title = self.driver.title
        if act_title == "Analytics":
            assert True
            self.driver.close()
            self.logger.info("************** login test is passed ********************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Login.png")
            self.driver.close()
            self.logger.error("************** login test is Failed ********************")
            assert False

