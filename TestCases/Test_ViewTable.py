import pytest
import time
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from pageObjects.viewAsTable import ViewTable

class Tc_005_viewTableChart:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_ViewTable(self, setup):
        self.logger.info("************** TC_005__verifying view as table and chart functionality********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***********Login successfully......... **************")
        self.logger.info("*********** Starting view as table and view as chart validation *******")

        self.ViewAsTableChart = ViewTable(self.driver)
        self.ViewAsTableChart.First_RecruitCardHeaderClickOnThreeDot()
        time.sleep(10)
        self.ViewAsTableChart.First_RecruitCardClickViewAsTable()
        time.sleep(10)
        self.ViewAsTableChart.First_RecruitCardClickViewAsChart()
        time.sleep(10)
        self.logger.info("********* your view as table and view as chart test case run successfully...******")
        self.logger.info("***********test cases Execution End*********8")

