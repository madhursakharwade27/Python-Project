from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class ShowMeMore:
    First_RecruitCardShowMeMore_tab = "//*[@id='chart-3515']/div/div/div[3]/div/button/strong"
    First_RecruitCardShowMeMoreInsightClosed = "//div[@class='mat-drawer-title']//i[@class='mdi mdi-close']"
    First_RecruitCardShowMeMoreInsightCardQuestionOnTopOfChildChart = "//*[@id='topContainer']/mat-drawer-container/mat-drawer-content/div[2]/app-dashboard-v2/mat-drawer-container/mat-drawer/div/div/div/span"
    # first child chart : No of open jobs by grade and band
    First_RC_SMMI_NoOfOPenJobsByGradeAndBand = "//*[@id='topContainer']/mat-drawer-container/mat-drawer-content/div[2]/app-dashboard-v2/mat-drawer-container/mat-drawer/div/app-more-insights/div/div/div/div/div[1]/div/div[1]/label"
    First_RC_SMMI_NoOfOPenJobsByGradeAndBand_TimeSpan = "//div[@class='section-card']//div[1]//div[1]//div[1]//label[1]//span[1]"
    First_RC_SMMI_NoOfOPenJobsByGradeAndBand_DrillIcon = "//div[contains(@class,'section-card')]//div[1]//div[1]//div[1]//div[1]//span[1]//img[1]"
    First_RC_SMMI_NoOfOPenJobsByGradeAndBand_HedThreeDot = "//div[contains(@class,'section-card')]//div[1]//div[1]//div[1]//div[1]//div[1]//button[1]//span[1]//mat-icon[1]"
    First_RC_SMMI_NoOfOPenJobsByGradeAndBand_HedViewAsTable = "//span[normalize-space()='View As Table']"
    First_RC_SMMI_NoOfOPenJobsByGradeAndBand_HedViewAsChart = "//span[normalize-space()='View As Chart']"
    # 2nd child chart: Opening by hiring manager
    First_RC_SMMI_OpeningByHireManager = "//div[@class='homestroryboard ng-star-inserted']//div[2]//div[1]//div[1]//label[1]"
    First_RC_SMMI_OpeningByHireManager_TimeSpan = "//div[@class='homestroryboard ng-star-inserted']//div[2]//div[1]//div[1]//label[1]//span[1]"
    # 3rd child chart: Opening by recruiter
    First_RC_SMMI_OpeningByRecruiter = "//div[3]//div[1]//div[1]//label[1]"
    First_RC_SMMI_OpeningByRecruiter_TimeSpan = "//div[3]//div[1]//div[1]//label[1]//span[1]"
    # 4th Child chart: Number of open job by worklocation
    First_RC_SMMI_NoOfOpenJobsByWorklocation = "//div[4]//div[1]//div[1]//label[1]"
    First_RC_SMMI_NoOfOpenJobsByWorklocation_TimeSpan = "//div[4]//div[1]//div[1]//label[1]//span[1]"
    First_RC_SMMI_NoOfOpenJobsByWorklocation_DrillIcon = "//div[4]//div[1]//div[1]//div[1]//span[1]//img[1]"
    First_RC_SMMI_NoOfOpenJobsByWorklocation_ThreeDot = "//*[@id='topContainer']/mat-drawer-container/mat-drawer-content/div[2]/app-dashboard-v2/mat-drawer-container/mat-drawer/div/app-more-insights/div/div/div/div/div[4]/div/div[1]/div/div/button/span/mat-icon"
    First_RC_SMMI_NoOfOpenJobsByWorklocation_ViewAsTable = "//span[normalize-space()='View As Table']"
    First_RC_SMMI_NoOfOpenJobsByWorklocation_ViewAsChart = "//span[normalize-space()='View As Chart']"
    # 5th Child chart Applicant by stage for open jobs
    First_RC_SMMI_ApplicantByStageForOpenJobs = "//div[5]//div[1]//div[1]//label[1]"
    First_RC_SMMI_ApplicantByStageForOpenJobs_TimeSpan = "//div[5]//div[1]//div[1]//label[1]//span[1]"
    First_RC_SMMI_ApplicantByStageForOpenJobs_DrillIcon = "//div[5]//div[1]//div[1]//div[1]//span[1]//img[1]"
    First_RC_SMMI_ApplicantByStageForOpenJobs_ThreeDot = "//*[@id='topContainer']/mat-drawer-container/mat-drawer-content/div[2]/app-dashboard-v2/mat-drawer-container/mat-drawer/div/app-more-insights/div/div/div/div/div[5]/div/div[1]/div/div/button/span/mat-icon"
    First_RC_SMMI_ApplicantByStageForOpenJobs_ViewAsTable = "//span[normalize-space()='View As Table']"
    First_RC_SMMI_ApplicantByStageForOpenJobs_ViewAsChart = "//span[normalize-space()='View As Chart']"


    def __init__(self, driver):
        self.driver = driver

    def click_on_show_me_more(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.First_RecruitCardShowMeMore_tab))
        )
        element.click()

    def click_on_cross_to_exit_from_show_more(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.First_RecruitCardShowMeMoreInsightClosed))
        )
        element.click()

    def First_RC_SMMI_CQ_OnTopOfChildChart(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.First_RecruitCardShowMeMoreInsightCardQuestionOnTopOfChildChart))
        )
        return element.text

    def First_RC_SMMI_OJ_ByGradeAndBand(self):
        element = WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located((By.XPATH,self.First_RC_SMMI_NoOfOPenJobsByGradeAndBand))
        )
        return element.text

    def First_RC_SMMI_OJ_ByGradeAndBand_TS(self):
        element = WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located((By.XPATH,self.First_RC_SMMI_NoOfOPenJobsByGradeAndBand_TimeSpan))
        )
        return element.text


    def capture_text_after_hovering(self):
        # Locate the drill icon element
        drill_icon = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.First_RC_SMMI_NoOfOPenJobsByGradeAndBand_DrillIcon))
        )
        ActionChains(self.driver).move_to_element(drill_icon).perform()

        try:
            # Wait for the popup to appear
            popup = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH,self.First_RC_SMMI_NoOfOPenJobsByGradeAndBand_DrillIcon))
            )
            popup_text = popup.text

            return popup_text

        except TimeoutException:
            print("Popup did not appear within 10 seconds")
            return None


    def First_RC_SMMI_OJ_ByGradeAndBand_ThreeDot(self):
        Three_dot = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,self.First_RC_SMMI_NoOfOPenJobsByGradeAndBand_HedThreeDot))
        )
        Three_dot.click()

    def First_RC_SMMI_OJ_ByGradeAndBand_ViewAsTable(self):
        View_Table = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,self.First_RC_SMMI_NoOfOPenJobsByGradeAndBand_HedViewAsTable))
        )
        View_Table.click()


    def First_RC_SMMI_OJ_ByGradeAndBand_ViewAsChart(self):
        View_Chart = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,self.First_RC_SMMI_NoOfOPenJobsByGradeAndBand_HedViewAsChart))
        )
        View_Chart.click()

    def First_RC_SMMI_Opening_By_Hiring_mngr_scroll_to_element(self):
        opening_by_hiring_manager = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.First_RC_SMMI_OpeningByHireManager))
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", opening_by_hiring_manager)


    def First_RC_SMMI_Opening_By_Hiring_mngr_chartTitle(self):
        opening_by_hiring_manager = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.First_RC_SMMI_OpeningByHireManager))
        )
        return opening_by_hiring_manager.text

    def First_RC_SMMI_Opening_By_Recruiter_scroll_to_element(self):
        opening_by_Recruiter = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.First_RC_SMMI_OpeningByRecruiter))
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", opening_by_Recruiter)


    def First_RC_SMMI_Opening_By_Recruiter_chartTitle(self):
        opening_by_Recruiter = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.First_RC_SMMI_OpeningByRecruiter))
        )
        return opening_by_Recruiter.text


    def First_RC_SMMI_OpenJobsByWorklocation_scroll_to_element(self):
        Open_Jobs_By_Worklocation = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.First_RC_SMMI_NoOfOpenJobsByWorklocation))
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", Open_Jobs_By_Worklocation)


    def First_RC_SMMI_OpenJobsByWorklocation_chartTitle(self):
        Open_Jobs_By_Worklocation_Title = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.First_RC_SMMI_NoOfOpenJobsByWorklocation))
        )
        return Open_Jobs_By_Worklocation_Title.text


    def First_RC_SMMI_OpenJobsByWorklocation_DrillIcon(self):
        Open_Jobs_By_Worklocation_DrillIcon = WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located((By.XPATH,self.First_RC_SMMI_NoOfOpenJobsByWorklocation_DrillIcon))
        )
        ActionChains(self.driver).move_to_element(Open_Jobs_By_Worklocation_DrillIcon).perform()

        try:
            Open_Jobs_By_Worklocation_DrillIcon_Popup = WebDriverWait(self.driver,10).until(
                EC.visibility_of_element_located((By.XPATH,self.First_RC_SMMI_NoOfOpenJobsByWorklocation_DrillIcon))
            )
            Open_Jobs_By_Worklocation_DrillIcon_Popup_text = Open_Jobs_By_Worklocation_DrillIcon_Popup.text

            return Open_Jobs_By_Worklocation_DrillIcon_Popup_text

        except TimeoutException:
            print("Pop up did not appear within 10 sec ")
            return None

    def First_RC_SMMI_OpenJobsByWorklocation_ThreeDot(self):
        Open_Jobs_By_Worklocation_ThreeDot = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,self.First_RC_SMMI_NoOfOpenJobsByWorklocation_ThreeDot))
        )
        Open_Jobs_By_Worklocation_ThreeDot.click()

    def First_RC_SMMI_OpenJobsByWorklocation_ViewTable(self):
        Open_Jobs_By_Worklocation_ViewTable = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,self.First_RC_SMMI_NoOfOpenJobsByWorklocation_ViewAsTable))
        )
        Open_Jobs_By_Worklocation_ViewTable.click()

    def First_RC_SMMI_OpenJobsByWorklocation_ViewChart(self):
        Open_Jobs_By_Worklocation_ViewChart = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,self.First_RC_SMMI_NoOfOpenJobsByWorklocation_ViewAsChart))
        )
        Open_Jobs_By_Worklocation_ViewChart.click()


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


    def First_RC_SMMI_ApplicantByStageForOpenJobs_scroll_to_element(self):
        Applicant_By_Stage_For_OpenJob = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.First_RC_SMMI_ApplicantByStageForOpenJobs))
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", Applicant_By_Stage_For_OpenJob)


    def First_RC_SMMI_ApplicantByStageForOpenJobs_chartTitle(self):
        Applicant_By_Stage_For_OpenJob_Title = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.First_RC_SMMI_ApplicantByStageForOpenJobs))
        )
        return Applicant_By_Stage_For_OpenJob_Title.text


    def First_RC_SMMI_Applicant_By_Stage_For_OpenJobs_DrillIcon(self):
        ApplicantByStageForOpenJobs_DrillIcon = WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located((By.XPATH,self.First_RC_SMMI_ApplicantByStageForOpenJobs_DrillIcon))
        )
        ActionChains(self.driver).move_to_element(ApplicantByStageForOpenJobs_DrillIcon).perform()

        try:
            ApplicantByStageForOpenJobs_DrillIcon_popup = WebDriverWait(self.driver,10).until(
                EC.visibility_of_element_located((By.XPATH,self.First_RC_SMMI_NoOfOpenJobsByWorklocation_DrillIcon))
            )
            ApplicantByStageForOpenJobs_DrillIcon_popup_Popup_text = ApplicantByStageForOpenJobs_DrillIcon_popup.text

            return ApplicantByStageForOpenJobs_DrillIcon_popup_Popup_text

        except TimeoutException:
            print("Pop up did not appear within 10 sec ")
            return None


    def First_RC_SMMI_Applicant_By_Stage_For_Open_Jobs_ThreeDot(self):
        Applicant_By_Stage_For_OpenJobs_ThreeDot = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,self.First_RC_SMMI_ApplicantByStageForOpenJobs_ThreeDot))
        )
        Applicant_By_Stage_For_OpenJobs_ThreeDot.click()


    def First_RC_SMMI_Applicant_By_Stage_For_Open_Jobs_ViewTable(self):
        Applicant_By_Stage_For_OpenJobs_ViewTable = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,self.First_RC_SMMI_ApplicantByStageForOpenJobs_ViewAsTable))
        )
        Applicant_By_Stage_For_OpenJobs_ViewTable.click()


    def First_RC_SMMI_Applicant_By_Stage_For_Open_Jobs_ViewChart(self):
        Applicant_By_Stage_For_OpenJobs_ViewChart = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,self.First_RC_SMMI_ApplicantByStageForOpenJobs_ViewAsChart))
        )
        Applicant_By_Stage_For_OpenJobs_ViewChart.click()




