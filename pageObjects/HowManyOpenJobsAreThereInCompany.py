import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait


class HowManyOpenJobsAreThereInTheCompany:
    #How many open jobs are there in the company
    drp_ClickOnDashboarddropdown = "//mat-select[@id='mat-select-0']//div[@class='mat-select-arrow-wrapper']"
    First_RecruitCardHeader = "//app-card-v2[@id='chart-3515']//h2[contains(text(),'Recruitment')]"
    First_RecruitCardHeaderClickOnThreeDot = "//app-card-v2[@id='chart-3515']//mat-icon[@role='img']"
    First_RecruitCardClickViewAsTable = "//span[normalize-space()='View As Table']"
    First_RecruitCardClickViewAsChart = "//span[normalize-space()='View As Chart']"
    First_RecruitCardIsThisHelpfulYes = "//app-card-v2[@id='chart-3515']//strong[contains(text(),'Yes')]"
    First_RecruitCardIsThisHelpfulYes_radio = "//label[@for='mat-radio-2-input']//div[@class='mat-radio-inner-circle']"
    First_RecruitCardIsThisHelpfulNo = "//app-card-v2[@id='chart-3515']//strong[contains(text(),'No')]"
    First_RecruitCardIsThisHelpfulNo_radio = "//label[@for='mat-radio-3-input']//div[@class='mat-radio-inner-circle']"
    First_RecruitCardIsThisHelpfulMSG = "//textarea[@id='mat-input-0']"
    First_RecruitCardIsThisHelpfulSubmit = "//button[normalize-space()='SUBMIT']"
    First_RecruitCardIsThisHelpfulCancel = "//button[normalize-space()='CANCEL']"
    First_RecruitCardQuestion = "//h2[normalize-space()='How many open jobs are there in the company?']"
    First_RecruitCardInfoIcon = "//*[@id='chart-3515']/div/div/div[2]/div[1]/h2/span/i"
    First_RecruitCard_Jobs = "//span[normalize-space()='Jobs']"
    First_RecruitCardBaseMetric = "//p[contains(text(),'are open across the company which were approved in') or contains(text(),'are open across the company which were approved as per applied filter')]"
    First_RecruitCardBaseMetricInsight = "//app-card-v2[@id='chart-3515']//span[contains(text(),'Historic Data Not Present For Insights') or contains(text(),'than last to last year')]"
    First_RecruitCardClickShowMeMoreInsight = "//*[@id='chart-3515']/div/div/div[3]/div/button"
    # After clicking on Show me more insight
    First_RecruitCardShowMeMoreInsightCardQuestionOnTopOfChildchart = "//*[@id='raphael-paper-2350']/g/text"
    First_RecruitCardShowMeMoreInsightClosed = "//div[@class='mat-drawer-title']//i[@class='mdi mdi-close']"
    # first child chart : No of open jobs by grade and band
    First_RC_SMMI_NoOfOPenJobsByGradeAndBand = "//div[@class='homestroryboard ng-star-inserted']//div[1]//div[1]//div[1]//label[1]"
    First_RC_SMMI_NoOfOPenJobsByGradeAndBand_TimeSpan = "//div[@class='section-card']//div[1]//div[1]//div[1]//label[1]//span[1]"
    First_RC_SMMI_NoOfOPenJobsByGradeAndBand_DrillIcon = "//div[contains(@class,'section-card')]//div[1]//div[1]//div[1]//div[1]//span[1]//img[1]"
    First_RC_SMMI_NoOfOPenJobsByGradeAndBand_HedThreedot = "//div[contains(@class,'section-card')]//div[1]//div[1]//div[1]//div[1]//div[1]//button[1]//span[1]//mat-icon[1]"
    First_RC_SMMI_NoOfOPenJobsByGradeAndBand_HedViewAsTable = "//span[normalize-space()='View As Table']"
    First_RC_SMMI_NoOfOPenJobsByGradeAndBand_HedViewAsChart = "//span[normalize-space()='View As Chart']"
    #2nd child chart: Opening by hiring manager
    First_RC_SMMI_OpeningByHireManager = "//div[@class='homestroryboard ng-star-inserted']//div[2]//div[1]//div[1]//label[1]"
    First_RC_SMMI_OpeningByHireManager_TimeSpan = "//div[@class='homestroryboard ng-star-inserted']//div[2]//div[1]//div[1]//label[1]//span[1]"
    # 3rd child chart: Opening by recruiter
    First_RC_SMMI_OpeningByRecruiter = "//div[3]//div[1]//div[1]//label[1]"
    First_RC_SMMI_OpeningByRecruiter_TimeSpan = "//div[3]//div[1]//div[1]//label[1]//span[1]"
    #4th Child chart: Number of open job by worklocation
    First_RC_SMMI_NoOfOpenJobsByWorklocation = "//div[4]//div[1]//div[1]//label[1]"
    First_RC_SMMI_NoOfOpenJobsByWorklocation_TimeSpan = "//div[4]//div[1]//div[1]//label[1]//span[1]"
    First_RC_SMMI_NoOfOpenJobsByWorklocation_DrillIcon = "//div[4]//div[1]//div[1]//div[1]//span[1]//img[1]"
    First_RC_SMMI_NoOfOpenJobsByWorklocation_ThreeDot = "//*[@id='topContainer']/mat-drawer-container/mat-drawer-content/div[2]/app-dashboard-v2/mat-drawer-container/mat-drawer/div/app-more-insights/div/div/div/div/div[4]/div/div[1]/div/div/button/span/mat-icon"
    First_RC_SMMI_NoOfOpenJobsByWorklocation_ViewAsTable = "//span[normalize-space()='View As Table']"
    First_RC_SMMI_NoOfOpenJobsByWorklocation_ViewAsChart = "//span[normalize-space()='View As Chart']"
    #Applicant by stage for open jobs
    First_RC_SMMI_ApplicantByStageForOpenJobs = "//div[5]//div[1]//div[1]//label[1]"
    First_RC_SMMI_ApplicantByStageForOpenJobs_TimeSpan = "//div[5]//div[1]//div[1]//label[1]//span[1]"
    First_RC_SMMI_ApplicantByStageForOpenJobs_DrillIcon = "//div[5]//div[1]//div[1]//div[1]//span[1]//img[1]"
    First_RC_SMMI_ApplicantByStageForOpenJobs_ThreeDot = "//*[@id='topContainer']/mat-drawer-container/mat-drawer-content/div[2]/app-dashboard-v2/mat-drawer-container/mat-drawer/div/app-more-insights/div/div/div/div/div[5]/div/div[1]/div/div/button/span/mat-icon"
    First_RC_SMMI_ApplicantByStageForOpenJobs_ViewAsTable = "//span[normalize-space()='View As Table']"
    First_RC_SMMI_ApplicantByStageForOpenJobs_ViewAsChart = "//span[normalize-space()='View As Chart']"


    def __init__(self, driver):
        self.driver = driver

    def clickondashboarddropdown(self):
        self.driver.find_element_by_xpath(self.drp_ClickOnDashboarddropdown).click()

    def firstrecruitcardheader(self):
        header_element = self.driver.find_element_by_xpath(self.First_RecruitCardHeader)
        return header_element.text

    def firstrecruitcardheaderclickonthreedot(self):
        self.driver.find_element_by_xpath(self.First_RecruitCardHeaderClickOnThreeDot).click()

    def firstrecruitcardviewastable(self):
        self.driver.find_element_by_xpath(self.First_RecruitCardClickViewAsTable).click()

    def firstrecruitcardclickviewaschart(self):
        self.driver.find_element_by_xpath(self.First_RecruitCardClickViewAsChart).click()

    def firstrecruitcardisthishelpfulyes(self):
        self.driver.find_element_by_xpath(self.First_RecruitCardIsThisHelpfulYes).click()

    def firstrecruitcardisthishelpfulyesradio(self):
        self.driver.find_element_by_xpath(self.First_RecruitCardIsThisHelpfulYes_radio).click()

    def firstrecruitcardisthishelpfulno(self):
        self.driver.find_element_by_xpath(self.First_RecruitCardIsThisHelpfulNo).click()

    def firstrecruitcardisthishelpfulnoradio(self):
        self.driver.find_element_by_xpath(self.First_RecruitCardIsThisHelpfulNo_radio).click()

    def firstrecruitcardisthishelpfulmsg(self, MSG):
        self.driver.find_element_by_xpath(self.First_RecruitCardIsThisHelpfulMSG).send_keys(MSG)

    def firstrecruitcardisthishelpfulsubmit(self):
        self.driver.find_element_by_xpath(self.First_RecruitCardIsThisHelpfulSubmit).click()

    def firstrecruitcardisthishelpfulcancel(self):
        self.driver.find_element_by_xpath(self.First_RecruitCardIsThisHelpfulCancel).click()

    def firstrecruitcardquestion(self):
        self.driver.find_element_by_xpath(self.First_RecruitCardQuestion).text

    def firstrecruitcardinfoicon(self, First_RecruitCardInfoIcon):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,First_RecruitCardInfoIcon)))
        action = ActionChains(self.driver)
        action.move_to_element(element).click().perform()

    def firstrecruitcardjobs(self):
        self.driver.find_element_by_xpath(self.First_RecruitCard_Jobs).text()

    def firstrecruitcardbasemetric(self):
        self.driver.find_element_by_xpath(self.First_RecruitCardBaseMetric).text()

    def firstrecruitcardbasemetricinsight(self):
        self.driver.find_element_by_xpath(self.First_RecruitCardBaseMetricInsight).text()

    def firstrecruitcardclickshowmemoreinsight(self):
        self.driver.find_element_by_xpath(self.First_RecruitCardClickShowMeMoreInsight).click()

    def firstrecruitcardshowmemoreinsightcardquestionontopofchildchart(self):
        self.driver.find_element_by_xpath(self.First_RecruitCardShowMeMoreInsightCardQuestionOnTopOfChildchart).text()

    def firstrecruitcardshowmemoreinsightclosed(self):
        self.driver.find_element_by_xpath(self.First_RecruitCardShowMeMoreInsightClosed).click()

    def firstRCSMMInoofopenjobsbygradeandband(self):
        self.driver.find_element_by_xpath(self.First_RC_SMMI_NoOfOPenJobsByGradeAndBand).text()

    def firstRCSMMInoofopenjobsbygradeandbandtimeSpan(self):
        self.driver.find_element_by_xpath(self.First_RC_SMMI_NoOfOPenJobsByGradeAndBand_TimeSpan).text()


    def firstRCSMMInoofopenjobsbygradeandbanddrillicon(self, First_RC_SMMI_NoOfOPenJobsByGradeAndBand_DrillIcon):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,First_RC_SMMI_NoOfOPenJobsByGradeAndBand_DrillIcon)))
        action = ActionChains(self.driver)
        action.move_to_element(element).click().perform()

    def firstRCSMMInoOfopenjobsbygradeandbandhedhtreedot(self):
        self.driver.find_element_by_xpath(self.First_RC_SMMI_NoOfOPenJobsByGradeAndBand_HedThreedot).click()

    def firstRCSMMInoofopenjobsbygradeandbandhedviewastable(self):
        self.driver.find_element_by_xpath(self.First_RC_SMMI_NoOfOPenJobsByGradeAndBand_HedViewAsTable).click()

    def firstRCSMMInoofopenjobsbygradeandbandhedviewaschart(self):
        self.driver.find_element_by_xpath(self.First_RC_SMMI_NoOfOPenJobsByGradeAndBand_HedViewAsChart).click()

    def first_recruit_card_is_this_helpful_yes(self):
        self.driver.find_element_by_xpath(self.First_RecruitCardIsThisHelpfulYes).click()

    def first_recruit_card_is_this_helpful_msg(self, msg):
        self.driver.find_element_by_xpath(self.First_RecruitCardIsThisHelpfulMSG).send_keys(msg)

    def first_recruit_card_is_this_helpful_submit(self):
        self.driver.find_element_by_xpath(self.First_RecruitCardIsThisHelpfulSubmit).click()





