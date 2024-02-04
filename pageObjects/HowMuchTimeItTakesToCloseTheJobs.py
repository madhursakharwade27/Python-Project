from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Utilities.customLogger import LogGen
import logging
import time
from Utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage

class TimeTakesToCloseTheJob:

    ClickOn_DashboardDropdown = "//mat-select[@id='mat-select-0']//div[@class='mat-select-arrow-wrapper']"
    Dashboards_dropdown_AllDashboard_text = "//*[starts-with(@id,'mat-option-')]"

    Second_RecruitCardHeader = "//app-card-v2[@id='chart-3501']//h2[contains(text(),'Recruitment')]"
    Second_RecruitCardQuestion = "//h2[normalize-space()='How much time it takes to close the jobs?']"
    Second_RC_CardQuestion_Info_Icon = "//*[@id='chart-3501']/div/div/div[2]/div[1]/h2/span/i"

    ### Base Chart RC second Card
    Second_RecruitCardHeaderClickOnThreeDot = "//app-card-v2[@id='chart-3501']//mat-icon[@role='img']"
    Second_RecruitCardClickViewAsTable = "//span[normalize-space()='View As Table']"
    Second_RecruitCardClickViewAsChart = "//span[normalize-space()='View As Chart']"

    Second_RecruitCard_Helpful_Functionality_Yes = "//app-card-v2[@id='chart-3501']//strong[contains(text(),'Yes')]"
    Second_RecruitCard_Helpful_Functionality_No = "//app-card-v2[@id='chart-3501']//strong[contains(text(),'No')]"
    Second_RC_Helpful_Functionality_Yes_Radio = "//label[@for='mat-radio-2-input']//div[@class='mat-radio-inner-circle']"
    Second_RC_Helpful_Functionality_No_Radio = "//label[@for='mat-radio-3-input']//div[@class='mat-radio-inner-circle']"
    Second_RC_Helpful_Functionality_MSG = "//textarea[@id='mat-input-0']"
    Second_RC_Helpful_Functionality_Submit = "//button[normalize-space()='SUBMIT']"
    Second_RC_Helpful_Functionality_Cancel = "//button[normalize-space()='CANCEL']"
    Second_RC_Helpful_Functionality_No_Submit_warnings = "//div[@class='error-msg ng-star-inserted']"

    ##### SHOW ME MORE INSIGHT
    Second_RC_Click_On_ShowMeMoreInsight = "//*[@id='chart-3501']/div/div/div[3]/div/button"
    Second_RC_Click_Exit_From_ShowMeMoreInsight = "//div[@class='mat-drawer-title']//i[@class='mdi mdi-close']"
    Second_RC_SMMI_CQ_TopOfChildChart = "//*[@id='topContainer']/mat-drawer-container/mat-drawer-content/div[2]/app-dashboard-v2/mat-drawer-container/mat-drawer/div/div/div/span"

    ###First Child Chart: Average Days It Takes To Close A Job By Organization Unit (Current Year) (ADITTCJB_by)
    Second_RC_SMMI_ADITTCJB_ByOrgUnit_Title = "//div[@class='section-card']//div[1]//div[1]//div[1]//label[1]"
    Second_RC_SMMI_ADITTCJB_ByOrgUnit_ThreeDot = "//div[@class='section-card']//div[1]//div[1]//div[1]//div[1]//div[1]//button[1]//span[1]//mat-icon[1]"
    Second_RC_SMMI_ADITTCJB_ByOrgUnit_ViewTable = "//span[normalize-space()='View As Table']"
    Second_RC_SMMI_ADITTCJB_ByOrgUnit_ViewChart = "//span[normalize-space()='View As Chart']"

    ###Second Child Chart: Average Days It Takes To Close A Job By Work Site (Current Year) (ADITTCJB_by)
    Second_RC_SMMI_ADITTCJB_ByWorksite_Title = "//div[@class='section-card']//div[2]//div[1]//div[1]//label[1]"
    Second_RC_SMMI_ADITTCJB_ByWorksite_ThreeDot = "//div[@class='section-card']//div[2]//div[1]//div[1]//div[1]//div[1]//button[1]//span[1]//mat-icon[1]"
    Second_RC_SMMI_ADITTCJB_ByWorksite_ViewTable = "//span[normalize-space()='View As Table']"
    Second_RC_SMMI_ADITTCJB_ByWorksite_ViewChart = "//span[normalize-space()='View As Chart']"

    ###Third Child Chart: Average Days It Takes To Close A Job By Grade (Current Year) (ADITTCJB_by)
    Second_RC_SMMI_ADITTCJB_ByGrade_Title = "//div[@class='section-card']//div[3]//div[1]//div[1]//label[1]"
    Second_RC_SMMI_ADITTCJB_ByGrade_ThreeDot = "//div[@class='section-card']//div[3]//div[1]//div[1]//div[1]//div[1]//button[1]//span[1]//mat-icon[1]"
    Second_RC_SMMI_ADITTCJB_ByGrade_ViewTable = "//span[normalize-space()='View As Table']"
    Second_RC_SMMI_ADITTCJB_ByGrade_ViewChart = "//span[normalize-space()='View As Chart']"

    ###Fourth Child Chart: Average Days It Takes To Close A Job By Band (Current Year) (ADITTCJB_by)
    Second_RC_SMMI_ADITTCJB_ByBand_Title = "//div[@class='section-card']//div[4]//div[1]//div[1]//label[1]"
    Second_RC_SMMI_ADITTCJB_ByBand_ThreeDot = "//div[@class='section-card']//div[4]//div[1]//div[1]//div[1]//div[1]//button[1]//span[1]//mat-icon[1]"
    Second_RC_SMMI_ADITTCJB_ByBand_ViewTable = "//span[normalize-space()='View As Table']"
    Second_RC_SMMI_ADITTCJB_ByBand_ViewChart = "//span[normalize-space()='View As Chart']"

    ###Fifth Child Chart: Average Days It Takes To Close A Job By Designation (Current Year) (ADITTCJB_by)
    Second_RC_SMMI_ADITTCJB_ByDesignation_Title = "//div[@class='section-card']//div[5]//div[1]//div[1]//label[1]"

    ###Sixth Child Chart: Average Days To Close A Job (Quarter On Quarter Basis) (Current Year) (ADTCJB_Qtr_On_Qtr_basis)
    Second_RC_SMMI_ADTCJB_Qtr_On_Qtr_basis_Title = "//div[@class='section-card']//div[6]//div[1]//div[1]//label[1]"
    Second_RC_SMMI_ADTCJB_Qtr_On_Qtr_basis_ThreeDot = "//div[@class='section-card']//div[6]//div[1]//div[1]//div[1]//div[1]//button[1]//span[1]//mat-icon[1]"
    Second_RC_SMMI_ADTCJB_Qtr_On_Qtr_basis_ViewTable = "//span[normalize-space()='View As Table']"
    Second_RC_SMMI_ADTCJB_Qtr_On_Qtr_basis_ViewChart = "//span[normalize-space()='View As Chart']"

    ###Seventh Child Chart: AAverage Days It Takes To Close A Job By Hiring Manager (Current Year) (ADITTCJB_by)
    Second_RC_SMMI_ADITTCJB_ByHiringManager_Title = "//div[@class='section-card']//div[7]//div[1]//div[1]//label[1]"
    Second_RC_SMMI_ADITTCJB_ByHiringManager_ThreeDot = "//div[@class='section-card']//div[7]//div[1]//div[1]//div[1]//div[1]//button[1]//span[1]//mat-icon[1]"
    Second_RC_SMMI_ADITTCJB_ByHiringManager_ViewTable = "//span[normalize-space()='View As Table']"
    Second_RC_SMMI_ADITTCJB_ByHiringManager_ViewChart = "//span[normalize-space()='View As Chart']"


    def __init__(self, driver):
        self.logger = LogGen.loggen()
        self.driver = driver

    def Click_On_Dashboard_Dropdown(self):
        Dashboard_Dropdown = WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable((By.XPATH,self.ClickOn_DashboardDropdown))
        )
        Dashboard_Dropdown.click()

    def All_Dashobard_text_from_Home_Dashobard_dropdown(self):
        AllDashobard = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, self.Dashboards_dropdown_AllDashboard_text))
        )
        return AllDashobard

    def Select_Personalized_for_you_from_Home_dropdown(self):
        self.Click_On_Dashboard_Dropdown()
        time.sleep(3)
        elements = self.All_Dashobard_text_from_Home_Dashobard_dropdown()
        for element in elements:
            if element.text == "Personalized for you":
                element.click()
                self.logger.info("******* click on personalized for you successfully ...******")
                self.logger.info("Now breaking the loop i got my requirement")
                break
        else:
            print("Personalized for you not found")
            self.logger.error("***** personalized for you not found *******")

    def Capture_The_Text_From_Second_CardHeader(self):
        Header_text = WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located((By.XPATH,self.Second_RecruitCardHeader))
        )
        return Header_text.text


    def Title_Of_Second_Card(self):
        Second_Card_Question = WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located((By.XPATH,self.Second_RecruitCardQuestion))
        )
        return Second_Card_Question.text

    def Second_RC_HoverOn_I_Icon_Near_CQ(self):
        Info_icon = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.Second_RC_CardQuestion_Info_Icon))
        )
        ActionChains(self.driver).move_to_element(Info_icon).perform()
        self.logger.info("***** successfully hover on Info icon*******")

    def Click_On_ThreeDot_Base_Chart(self):
        Three_Dot = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,self.Second_RecruitCardHeaderClickOnThreeDot))
        )
        Three_Dot.click()

    def Click_On_View_Table(self):
        View_Table = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,self.Second_RecruitCardClickViewAsTable))
        )
        View_Table.click()

    def Click_On_View_Chart(self):
        View_Chart = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,self.Second_RecruitCardClickViewAsChart))
        )

    def Second_RC_Click_On_Yes(self):
        ClickOnYes = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,self.Second_RecruitCard_Helpful_Functionality_Yes))
        )
        ClickOnYes.click()

    def Second_RC_Click_On_No(self):
        ClickOnNo = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,self.Second_RecruitCard_Helpful_Functionality_No))
        )
        ClickOnNo.click()

    def Second_RC_Click_On_Yes_Radio(self):
        ClickOnYes_Radio = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,self.Second_RC_Helpful_Functionality_Yes_Radio))
        )
        ClickOnYes_Radio.click()

    def Second_RC_Click_On_No_Radio(self):
        ClickOnNo_Radio = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,self.Second_RC_Helpful_Functionality_No_Radio))
        )
        ClickOnNo_Radio.click()

    def Second_RC_Click_On_TextArea(self, input_text):
        TextArea = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,self.Second_RC_Helpful_Functionality_MSG))
        )
        TextArea.send_keys(input_text)


    def Second_RC_Click_On_Submit(self):
        SubmitButton = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,self.Second_RC_Helpful_Functionality_Submit))
        )
        SubmitButton.click()

    def Second_RC_Click_On_Cancel(self):
        CancelButton = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,self.Second_RC_Helpful_Functionality_Cancel))
        )
        CancelButton.click()

    def Second_RC_Click_On_Show_Me_More_Insight_Tab(self):
        Show_Me_More = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,self.Second_RC_Click_On_ShowMeMoreInsight))
        )
        Show_Me_More.click()

    def Second_RC_Click_On_Exit_From_Show_Me_More_Insight(self):
        Exit_From_Show_More = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,self.Second_RC_Click_Exit_From_ShowMeMoreInsight))
        )
        Exit_From_Show_More.click()

    def Second_RC_SMMI_CQ_Top_Of_Child_chart(self):
        Card_Question = WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located((By.XPATH,self.Second_RC_SMMI_CQ_TopOfChildChart))
        )
        return Card_Question.text

    def Second_RC_SMMI_ADITTCJ_By_Organization_Unit_Chart_Title(self):
        Chart_Title = WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located((By.XPATH,self.Second_RC_SMMI_ADITTCJB_ByOrgUnit_Title))
        )
        return Chart_Title.text

    def Second_RC_SMMI_ADITTCJ_By_Organization_Unit_Three_Dot(self):
        Three_Dot = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,self.Second_RC_SMMI_ADITTCJB_ByOrgUnit_ThreeDot))
        )
        Three_Dot.click()

    def Second_RC_SMMI_ADITTCJ_By_Organization_Unit_View_Table(self):
        View_Table = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,self.Second_RC_SMMI_ADITTCJB_ByOrgUnit_ViewTable))
        )
        View_Table.click()

    def Second_RC_SMMI_ADITTCJ_By_Organization_Unit_View_Chart(self):
        View_Chart = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,self.Second_RC_SMMI_ADITTCJB_ByOrgUnit_ViewChart))
        )
        View_Chart.click()

    def Second_RC_SMMI_ADITTCJ_By_Worksite_Chart_Title(self):
        Chart_Title = WebDriverWait(self.driver,20).until(
            EC.visibility_of_element_located((By.XPATH,self.Second_RC_SMMI_ADITTCJB_ByWorksite_Title))
        )
        return Chart_Title.text

    def Second_RC_SMMI_ADITTCJ_By_Worksite_Chart_Three_Dot(self):
        Three_Dot = WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable((By.XPATH,self.Second_RC_SMMI_ADITTCJB_ByWorksite_ThreeDot))
        )
        Three_Dot.click()

    def Second_RC_SMMI_ADITTCJ_By_Worksite_Chart_View_Table(self):
        View_Table = WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable((By.XPATH,self.Second_RC_SMMI_ADITTCJB_ByWorksite_ViewTable))
        )
        View_Table.click()

    def Second_RC_SMMI_ADITTCJ_By_Worksite_Chart_View_Chart(self):
        View_Chart = WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable((By.XPATH,self.Second_RC_SMMI_ADITTCJB_ByWorksite_ViewChart))
        )
        View_Chart.click()


    def Second_RC_SMMI_ADITTCJ_By_Grade_Chart_Title(self):
         Chart_Title = WebDriverWait(self.driver,20).until(
             EC.visibility_of_element_located((By.XPATH,self.Second_RC_SMMI_ADITTCJB_ByGrade_Title))
         )
         return Chart_Title.text

    def Second_RC_SMMI_ADITTCJ_By_Grade_Chart_Three_Dot(self):
        Three_Dot = WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable((By.XPATH,self.Second_RC_SMMI_ADITTCJB_ByGrade_ThreeDot))
        )
        Three_Dot.click()

    def Second_RC_SMMI_ADITTCJ_By_Grade_Chart_View_Table(self):
        View_Table = WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable((By.XPATH,self.Second_RC_SMMI_ADITTCJB_ByGrade_ViewTable))
        )
        View_Table.click()

    def Second_RC_SMMI_ADITTCJ_By_Grade_Chart_View_Chart(self):
        View_Chart = WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable((By.XPATH,self.Second_RC_SMMI_ADITTCJB_ByGrade_ViewChart))
        )
        View_Chart.click()













