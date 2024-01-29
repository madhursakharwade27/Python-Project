from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ModuleNameAndCardQuestion:
    First_RecruitCardHeader = "//app-card-v2[@id='chart-3515']//h2[contains(text(),'Recruitment')]"
    First_RecruitCardQuestion = "//h2[normalize-space()='How many open jobs are there in the company?']"


    def __init__(self, driver):
        self.driver = driver

    def capture_the_text_from_first_card_header(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.First_RecruitCardHeader))
        )
        return element.text

    def capture_the_text_from_first_card_question(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.First_RecruitCardQuestion))
        )
        return element.text
