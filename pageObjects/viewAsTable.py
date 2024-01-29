from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ViewTable:
    First_RecruitCardHeaderClickOnThreeDot = "//app-card-v2[@id='chart-3515']//mat-icon[@role='img']"
    First_RecruitCardClickViewAsTable = "//span[normalize-space()='View As Table']"
    First_RecruitCardClickViewAsChart = "//span[normalize-space()='View As Chart']"

    def __init__(self, driver):
        self.driver = driver

    def click_on_three_dot(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.First_RecruitCardHeaderClickOnThreeDot))
        )
        element.click()

    def click_on_three_dot_again(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.First_RecruitCardHeaderClickOnThreeDot))
        )
        element.click()

    def click_on_view_table(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.First_RecruitCardClickViewAsTable))
        )
        element.click()

    def click_on_view_chart(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.First_RecruitCardClickViewAsChart))
        )
        element.click()

    def is_three_dot_visible(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.First_RecruitCardHeaderClickOnThreeDot))
            )
            return True
        except:
            return False

    def is_view_table_visible(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.First_RecruitCardClickViewAsTable))
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            return element.is_displayed()
        except:
            return False

    def is_view_chart_visible(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.First_RecruitCardClickViewAsChart))
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            return element.is_displayed()
        except:
            return False
