# import pytest
# import time
# from selenium import webdriver
# from pageObjects.LoginPage import LoginPage
# from Utilities.readProperties import ReadConfig
# from Utilities.customLogger import LogGen
# from pageObjects.HowManyOpenJobsAreThereInCompany import HowManyOpenJobsAreThereInTheCompany
#
# class Tc_004_IsThisHelpfulFor1stCard:
#     baseURL = ReadConfig.getApplicationURL()
#     username = ReadConfig.getUseremail()
#     password = ReadConfig.getPassword()
#
#     logger = LogGen.loggen()
#
#     def verifyIsThisHelpfulFuctionalityForFirstCard(self, setup):
#         self.logger.info("************** TC_004__verifying the module Name of First card********************")
#         self.driver = setup
#         self.driver.get(self.baseURL)
#         self.driver.maximize_window()
#
#         self.lp = LoginPage(self.driver)
#         self.lp.setUserName(self.username)
#         self.lp.setPassword(self.password)
#         self.lp.clickLogin()
#         self.logger.info("***********Login successfully......... **************")
#         self.logger.info("***********Starting is this helpuf fuctionality validation *******")
#
#         self.verifyIsThisHelpfulFuctionalityforopenjobscard = HowManyOpenJobsAreThereInTheCompany(self.driver)
#         self.verifyIsThisHelpfulFuctionalityforopenjobscard.firstrecruitcardisthishelpfulyes()
#
#         self.verifyIsThisHelpfulFuctionalityforopenjobscard.firstrecruitcardisthishelpfulmsg("Yeah! it is good")
#         self.verifyIsThisHelpfulFuctionalityforopenjobscard.firstrecruitcardisthishelpfulsubmit()
#
#         self.msg = self.driver.find_element_by_tag_Name("body").text
#
#         print(self.msg)
#
#         if 'Thank You. Your response is saved successfully.' in self.msg:
#             assert True == True
#             self.logger.info("********* Is this helpful fuctionality working fine **********")
#         else:
#             self.logger.save_screenshot(".\\Screenshots\\"+"test_IsThisHelpful_forOpenJobs.scr.png")
#             self.logger.error("**********Is this helpful functionality for Open jobs card Failed*********")
#             assert True == False
#
#         self.driver.close()
#         self.logger.info("********** ending is this helpful validation test *********")
#
#
#
#
#


####+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from pageObjects.HowManyOpenJobsAreThereInCompany import HowManyOpenJobsAreThereInTheCompany
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class Tc_004_IsThisHelpfulFor1stCard:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_verify_is_this_helpful_functionality_for_first_card(self, setup):
        self.logger.info("************** TC_004__verifying the module Name of First card********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***********Login successful... **************")
        self.logger.info("***********Starting is this helpful functionality validation *******")

        self.verify_is_this_helpful_functionality_for_open_jobs_card = HowManyOpenJobsAreThereInTheCompany(self.driver)
        self.verify_is_this_helpful_functionality_for_open_jobs_card.first_recruit_card_is_this_helpful_yes()

        self.verify_is_this_helpful_functionality_for_open_jobs_card.first_recruit_card_is_this_helpful_msg("Yeah! it is good")
        self.verify_is_this_helpful_functionality_for_open_jobs_card.first_recruit_card_is_this_helpful_submit()

        msg = self.driver.find_element_by_tag_name("body").text

        print(msg)

        if 'Thank You. Your response is saved successfully.' in msg:
            self.logger.info("********* Is this helpful functionality working fine **********")
        else:
            self.logger.save_screenshot(".\\Screenshots\\"+"test_IsThisHelpful_forOpenJobs.scr.png")
            self.logger.error("**********Is this helpful functionality for Open jobs card Failed*********")
            assert False, "Is this helpful functionality for Open jobs card failed"

        self.driver.close()
        self.logger.info("********** Ending is this helpful validation test *********")




