from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class IsThisHelpful:
    First_RecruitCardIsThisHelpfulYes = "//app-card-v2[@id='chart-3515']//strong[contains(text(),'Yes')]"
    First_RecruitCardIsThisHelpfulYes_radio = "//label[@for='mat-radio-2-input']//div[@class='mat-radio-inner-circle']"
    First_RecruitCardIsThisHelpfulNo = "//app-card-v2[@id='chart-3515']//strong[contains(text(),'No')]"
    First_RecruitCardIsThisHelpfulNo_radio = "//label[@for='mat-radio-3-input']//div[@class='mat-radio-inner-circle']"
    First_RecruitCardIsThisHelpfulMSG = "//textarea[@id='mat-input-0']"
    First_RecruitCardIsThisHelpfulSubmit = "//button[normalize-space()='SUBMIT']"
    First_RecruitCardIsThisHelpfulCancel = "//button[normalize-space()='CANCEL']"

    def __init__(self,driver):
        self.driver = driver

    def First_Recruit_Card_Click_On_Yes(self):
        element = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,self.First_RecruitCardIsThisHelpfulYes))
        )
        element.click()

    def First_Recruit_Card_Click_On_No(self):
        element = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,self.First_RecruitCardIsThisHelpfulNo))
        )
        element.click()

    def First_Recruit_Card_Click_Radio_Button_Yes(self):
        element = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,self.First_RecruitCardIsThisHelpfulYes_radio))
        )
        element.click()

    def First_Recruit_Card_Click_Radio_Button_No(self):
        element = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,self.First_RecruitCardIsThisHelpfulNo_radio))
        )
        element.click()

    def First_Recruit_Card_IsThisHelpful_SendInput(self, input_text):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.First_RecruitCardIsThisHelpfulMSG))
        )
        element.send_keys(input_text)

    def First_Recruit_Card_IsThisHelpful_Submit(self):
        element = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,self.First_RecruitCardIsThisHelpfulSubmit))
        )
        element.click()

    def First_Recruit_Card_IsThisHelpful_Cancel(self):
        element = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,self.First_RecruitCardIsThisHelpfulCancel))
        )
        element.click()



