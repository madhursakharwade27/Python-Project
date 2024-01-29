import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from pageObjects.ShowMeMoreInsight import ShowMeMore

class Test_006_clickonshowmemore:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_show_me_more(self, setup):
        self.logger.info("************** Tc_006_verifying show me more insight tab ********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()


        time.sleep(20)

        self.logger.info("******** Now validation start on show me more insight ********")

        # Using a more consistent name for the instance
        show_me_more_instance = ShowMeMore(self.driver)
        show_me_more_instance.click_on_show_me_more()  # Corrected method name
        self.logger.info("********Clicked on Show me more insight successfully********")





        show_me_more_instance.click_on_cross_to_exit_from_show_more()  # Corrected method name
        self.logger.info("*************** Quited successfully from show me more insight********")
