import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from pageObjects.IsThisHelpfulFirst import IsThisHelpful

class Test_004_IsThisHelpfulForOpenJob:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_helpful_functionality_first_Card(self, setup):
        self.logger.info("************** TC_004__verifying the module Name of First card********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***********Login successful... **************")
        self.logger.info("***********Starting is this helpful functionality validation *******")
        time.sleep(10)
        self.helpful_functionality_for_open_jobs_card = IsThisHelpful(self.driver)
        self.helpful_functionality_for_open_jobs_card.First_Recruit_Card_Click_On_Yes()
        time.sleep(5)

        self.helpful_functionality_for_open_jobs_card.First_Recruit_Card_IsThisHelpful_SendInput("Yeah! it is good")
        time.sleep(5)
        self.helpful_functionality_for_open_jobs_card.First_Recruit_Card_IsThisHelpful_Submit()
        time.sleep(2)

        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.TAG_NAME, "body"))
            )
            msg = element.text

            print(msg)

            if 'Thank You. Your response is saved successfully.' in msg:
                self.logger.info("********* Is this helpful functionality working fine **********")
            else:
                self.logger.error("**********Is this helpful functionality for Open jobs card Failed*********")
                assert False, "Is this helpful functionality for Open jobs card failed"

        except TimeoutException:
            self.logger.error("**********TimeoutException: Element not found within 20 seconds*********")
            assert False, "TimeoutException: Element not found within 20 seconds"

        finally:
            self.driver.close()
            self.logger.info("********** Ending is this helpful validation test *********")


