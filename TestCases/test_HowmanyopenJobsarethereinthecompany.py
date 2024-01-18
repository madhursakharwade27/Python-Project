#
# import pytest
# import time
# from selenium import webdriver
# from pageObjects.LoginPage import LoginPage
# from Utilities.readProperties import ReadConfig
# from Utilities.customLogger import LogGen
# from pageObjects.HowManyOpenJobsAreThereInCompany import HowManyOpenJobsAreThereInTheCompany
#
# class Tc_003_ModuleNameofFirstCard:
#     baseURL = ReadConfig.getApplicationURL()
#     username = ReadConfig.getUseremail()
#     password = ReadConfig.getPassword()
#
#     logger = LogGen.loggen()
#
#     def verifyModuleNameOfFirstCard(self, setup):
#         self.logger.info("************** TC_003__verifying the module Name of First card********************")
#         self.driver = setup
#         self.driver.get(self.baseURL)
#         self.driver.maximize_window()
#
#         self.lp =LoginPage(self.driver)
#         self.lp.setUserName(self.username)
#         self.lp.setPassword(self.password)
#         self.lp.clickLogin()
#         self.logger.info("**************Login Successfully....*************")
#         time.sleep(4)
#         self.logger.info("*********Starting verifying your test********* ")
#
#
#         self.verifyModuleNameOfFirstCard = HowManyOpenJobsAreThereInTheCompany(self.driver)
#
#         actual_text = HowManyOpenJobsAreThereInTheCompany.firstrecruitcardheader()
#         expected_text = "Recruitment"
#         assert actual_text == expected_text, f"Text mismatch. Expected: {expected_text}, Actual: {actual_text}"
#
#
#



import pytest
import time
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from pageObjects.HowManyOpenJobsAreThereInCompany import HowManyOpenJobsAreThereInTheCompany

class Tc_003_ModuleNameofFirstCard:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def verifyModuleNameOfFirstCard(self, setup):
        try:
            self.logger.info("************** TC_003__verifying the module Name of First card********************")
            self.driver = setup
            self.driver.get(self.baseURL)
            self.driver.maximize_window()

            self.lp = LoginPage(self.driver)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            self.logger.info("************** Login Successfully....*************")
            time.sleep(4)
            self.logger.info("*********Starting verifying your test********* ")

            # Instantiate the page object
            self.how_many_jobs_page = HowManyOpenJobsAreThereInTheCompany(self.driver)

            # Call the function to get the actual text
            actual_text = self.how_many_jobs_page.firstrecruitcardheader()

            expected_text = "Recruitment"
            assert actual_text == expected_text, f"Text mismatch. Expected: {expected_text}, Actual: {actual_text}"

        except Exception as e:
            print(f"An error occurred: {e}")

# # Create an instance of the class to call the method
# test_instance = Tc_003_ModuleNameofFirstCard()
# test_instance.verifyModuleNameOfFirstCard("pass_the_setup_parameter_here")
