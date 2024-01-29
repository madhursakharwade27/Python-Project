import pytest
import time
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.ModuleNameAndTitleOfFirstCard import ModuleNameAndCardQuestion
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen


class Test_TC_003_ModuleNameOfFirstCard:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_verifyModuleNameOfFirstCard(self, setup):
        self.logger.info("************** TC_003__verifying the module Name of First card********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**************Login Successfully....*************")
        time.sleep(4)
        self.logger.info("*********Starting verifying your test********* ")

        # Create an instance of the page object
        page_object_instance = ModuleNameAndCardQuestion(self.driver)

        actual_text = page_object_instance.capture_the_text_from_first_card_header()
        expected_text = "Recruitment"
        assert actual_text == expected_text, f"Text mismatch. Expected: {expected_text}, Actual: {actual_text}"



    def test_verifyTitleOfFirstCard(self, setup):
        self.logger.info("************** TC_003A__verifying Title Of First card********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**************Login Successfully....*************")
        time.sleep(4)
        self.logger.info("*********Starting verifying your test********* ")

        # Create an instance of the page object
        page_object_instance = ModuleNameAndCardQuestion(self.driver)

        actual_text = page_object_instance.capture_the_text_from_first_card_question()
        expected_text = "How many open jobs are there in the company?"
        assert actual_text == expected_text, f"Text mismatch. Expected: {expected_text}, Actual: {actual_text}"
