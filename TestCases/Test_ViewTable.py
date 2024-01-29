import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from pageObjects.viewAsTable import ViewTable

class Test_005_viewTableChart:
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
        time.sleep(10)
        # assert "dashboard" in self.driver.current_url.lower(), "Login not successful"

        self.logger.info("***********Login successfully......... **************")
        self.logger.info("*********** Starting view as table and view as chart validation *******")

        self.ViewAsTableChart = ViewTable(self.driver)
        self.ViewAsTableChart.click_on_three_dot()
        assert self.ViewAsTableChart.is_three_dot_visible(), "Three dots not visible"

        self.ViewAsTableChart.click_on_view_table()
        self.ViewAsTableChart.is_view_table_visible()

        self.ViewAsTableChart.click_on_three_dot_again()
        assert self.ViewAsTableChart.is_three_dot_visible(), "Three dots not visible"

        self.ViewAsTableChart.click_on_view_chart()
        self.ViewAsTableChart.is_view_chart_visible()

        self.logger.info("********* your view as table and view as chart test case run successfully...******")
        self.logger.info("***********test cases Execution End*********")
