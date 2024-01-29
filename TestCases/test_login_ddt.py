
# TestCases/test_login.py

import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import XLUtils

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/loginData.xlsx"

    logger = LogGen.loggen()


    def test_Login_ddt(self, setup):
        self.logger.info("************** Test_002_DDT_Login ********************")
        self.logger.info("************** verifying login DDT test ********************")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of rows in a Excel: ", self.rows)

        list_status=[]  # Emppty list variable

        for r in range(2,self.rows+1):
            self.username = XLUtils.readData(self.path,'Sheet1',r,1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 2)


            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            self.driver.implicitly_wait(10)


            act_tile = self.driver.title
            exp_title = "Analytics"

            # if act_tile == exp_title:
            #     print("label as per expected")
            #
            # self.driver.quit()

            if act_tile == exp_title:
                if self.exp == "pass":
                    self.logger.info("***Test is passed ***")
                    self.lp.usericon()
                    self.lp.userlogout()
                    self.lp.userlogoutconfirmation()
                    list_status.append("pass")
                elif self.exp == "Fail":
                    self.logger.info("*** Test is Failed ***")
                    self.lp.usericon()
                    self.lp.userlogout()
                    self.lp.userlogoutconfirmation()
                    list_status.append("Fail")

            elif act_tile != exp_title:
                if self.exp == "Pass":
                    self.logger.info("*** Failed ****")
                    list_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("**** Passed ****")
                    list_status.append("Pass")

        if "Fail" not in list_status:
            self.logger.info("****Login DDT test Passed....****")
            self.driver.close()
            assert True
        else:
            self.logger.info("**** login DDT test failed")
            self.driver.close()
            assert False

        self.logger.info("**********End of login DDT Test*************")
        self.logger.info("********** Completed TC_LoginDDT_002 **********");





















