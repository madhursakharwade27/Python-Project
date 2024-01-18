import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait


class ViewTable:
    First_RecruitCardHeaderClickOnThreeDot = "//app-card-v2[@id='chart-3515']//mat-icon[@role='img']"
    First_RecruitCardClickViewAsTable = "//span[normalize-space()='View As Table']"
    First_RecruitCardClickViewAsChart = "//span[normalize-space()='View As Chart']"

    def __init__(self, driver):
        self.driver = driver

    def click_on_three_dot(self):
        self.driver.find_element_by_xpath(self.First_RecruitCardHeaderClickOnThreeDot).click()

    def click_on_View_Table(self):
        self.driver.find_element_by_xpath(self.First_RecruitCardClickViewAsTable).click()

    def click_on_view_chart(self):
        self.driver.find_element_by_xpath(self.First_RecruitCardClickViewAsChart).click()

