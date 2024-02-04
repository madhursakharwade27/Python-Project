import pytest
import time
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from pageObjects.HowManyOpenJobsAreThereInCompany import HowManyOpenJobsInTheCompany
from pageObjects.LoginPage import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.HowMuchTimeItTakesToCloseTheJobs import TimeTakesToCloseTheJob

class Test_How_Much_Time_It_Takes_To_Close_The_Job:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_TC_verifyModuleNameOfSecondCard(self, setup):
        self.logger.info("******** Verify the Module Name of second Card ***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********* Login Successfully...*********")
        ModuleNameOfSecondCard = TimeTakesToCloseTheJob(self.driver)
        ModuleNameOfSecondCard.Select_Personalized_for_you_from_Home_dropdown()
        actual_text = ModuleNameOfSecondCard.Capture_The_Text_From_Second_CardHeader()
        expected_text = "Recruitment"

        if actual_text == expected_text:
            assert True
            self.logger.info("****** Verifying Module Name of second card test Passed...*****")
        else:
            assert False
        print("Test case executed successfully...")


    def test_VerifyTitleOfSecondCard(self,setup):
        self.logger.info("******* Verifying the title of second card **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****** Login succcessfully *************")
        self.logger.info("******* Now validating the tile of second card/ card question of second card ***")

        SecondCardTitle = TimeTakesToCloseTheJob(self.driver)
        SecondCardTitle.Select_Personalized_for_you_from_Home_dropdown()
        actual_text = SecondCardTitle.Title_Of_Second_Card()
        expected_text = "How much time it takes to close the jobs?"

        if actual_text == expected_text:
            assert True
            self.logger.info("******* Actual Title is matching with Expected Title *********")
            self.logger.info("******* Test case passed **********")
        else:
            assert False
        print(" Test Case Executed successfully....")


    def test_Info_from_i_Icon_for_RC_SecondCard(self,setup):
        self.logger.info("*** verifying the Info of I icon for second chart (Time Takes to close job) ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******** Login successfully ....********")

        InfoiconFor_RC_SecondCard = TimeTakesToCloseTheJob(self.driver)
        InfoiconFor_RC_SecondCard.Select_Personalized_for_you_from_Home_dropdown()
        self.logger.info("****** Open personalized for you successfully...**")
        InfoiconFor_RC_SecondCard.Second_RC_HoverOn_I_Icon_Near_CQ()

        tooltip_xpath = "//div[contains(@class, 'cdk-overlay-container')]//div[contains(@class, 'mat-tooltip')]"
        tooltip = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, tooltip_xpath)))
        time.sleep(3)

        tooltip_text = tooltip.text
        print(tooltip_text)

        if tooltip.text == "It Shows The Average Time It Takes To Fill Up An Job Based On Historic Data Points. These Data Points Work On Timeframe As Per The Job Approved On The Selected Timeframe":
            assert True
            self.logger.info("The information of I icon is coming according to Requirement")
            self.logger.info("Test case passed...")
        else:
            assert False
        print("Test case executed successfully...")
        self.logger.info("*** Test case executed successfully...")



    def test_ViewTableChart_For_TimeTakesToCloseJob(self,setup):
        self.logger.info("**Verifying the view as table/chart Functionality for Time takes to close the job**")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****** Login Successfully...*******")

        ViewAsTableChart = TimeTakesToCloseTheJob(self.driver)
        ViewAsTableChart.Select_Personalized_for_you_from_Home_dropdown()
        ViewAsTableChart.Click_On_ThreeDot_Base_Chart()
        ViewAsTableChart.Click_On_View_Table()
        ViewAsTableChart.Click_On_ThreeDot_Base_Chart()
        ViewAsTableChart.Click_On_View_Chart()
        assert True


    def test_After_Clicking_On_Submit_Button(self,setup):
        self.logger.info("**** verifying the msg after clicking on submit button *******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****** Login Successfully...*****")

        Msg_AfterClickingOnSubmit = TimeTakesToCloseTheJob(self.driver)
        Msg_AfterClickingOnSubmit.Select_Personalized_for_you_from_Home_dropdown()
        Msg_AfterClickingOnSubmit.Second_RC_Click_On_Yes()
        time.sleep(2)
        self.logger.info("**** Clicked On Yes Button Successfully...*****")
        self.logger.info("**** Now validating Yes & No Radio button *******")
        Msg_AfterClickingOnSubmit.Second_RC_Click_On_No_Radio()
        self.logger.info("**** clicked on No Radio button successfully...****")
        Msg_AfterClickingOnSubmit.Second_RC_Click_On_Yes_Radio()
        self.logger.info("*** Clicked on Yes Radio Button Successfully..***")
        Msg_AfterClickingOnSubmit.Second_RC_Click_On_TextArea("yes!, excellent!")
        Msg_AfterClickingOnSubmit.Second_RC_Click_On_Submit()
        time.sleep(3)

        UI_Confirmation_Msg = WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located((By.TAG_NAME,"body"))
        )
        Confirmation = UI_Confirmation_Msg.text
        print(Confirmation)

        if 'Thank You. Your response is saved successfully.' in Confirmation:
            assert True
            self.logger.info("***** Test case is passed **********")
            self.logger.info("Thank You. Your response is saved successfully. showing after clicking on submit button")
        else:
            assert False
        print("Test case executed successfully....")


    def test_After_Clicking_On_Cancel_Button(self,setup):
        self.logger.info("** verify is this helpful functionality after clicking on Cancel button **")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******* Login Successfully...****")

        AfterClickingOnCancelButton = TimeTakesToCloseTheJob(self.driver)
        AfterClickingOnCancelButton.Select_Personalized_for_you_from_Home_dropdown()
        AfterClickingOnCancelButton.Second_RC_Click_On_No()
        time.sleep(2)
        self.logger.info("**** Now validating Yes & No Radio button *******")
        AfterClickingOnCancelButton.Second_RC_Click_On_Yes_Radio()
        self.logger.info("**** clicked on Yes Radio button successfully...****")
        AfterClickingOnCancelButton.Second_RC_Click_On_No_Radio()
        self.logger.info("*** Clicked on NO Radio Button Successfully..***")
        AfterClickingOnCancelButton.Second_RC_Click_On_TextArea("Just OK!")
        AfterClickingOnCancelButton.Second_RC_Click_On_Cancel()
        time.sleep(2)

        UI_Confirmation_Msg = WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located((By.TAG_NAME,"body"))
        )
        Confirmation = UI_Confirmation_Msg.text
        print(Confirmation)

        if 'Thank You. Your response is saved successfully.' not in Confirmation:
            assert True
            self.logger.info("*** Test case is passed..******")
            self.logger.info("Thank You.Your response is saved successfully.text not visible after clicking on cancel button")
        else:
            assert False

        print("Test case executed successfully...")


    def test_After_ClickingOn_NO_Submit(self,setup):
        self.logger.info("** Verifying the functionality after clicking on NO button and then submit button")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**** Login successfully...****")

        ClickingOn_No_Then_Submit = TimeTakesToCloseTheJob(self.driver)
        ClickingOn_No_Then_Submit.Select_Personalized_for_you_from_Home_dropdown()
        ClickingOn_No_Then_Submit.Second_RC_Click_On_No()
        ClickingOn_No_Then_Submit.Second_RC_Click_On_Submit()
        alert_text = WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located((By.TAG_NAME,"body"))
        )
        all_text = alert_text.text
        print(all_text)

        if "Please Enter Your Valuable Comment" in all_text:
            assert True
            self.logger.info("*** Test case is Passed...***")
            self.logger.info("Please Enter Your Valuable Comment is showing as alert")
        else:
            assert False
        print("Test Case Executed Successfully...")


    def test_Second_RC_Verifying_show_me_more_Tab(self,setup):
        self.logger.info("verifying show me more insight tab for Recruit second card/Time takes to close job")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*** Login Successfully...***")

        ShowMeMoreTab = TimeTakesToCloseTheJob(self.driver)
        ShowMeMoreTab.Select_Personalized_for_you_from_Home_dropdown()
        self.logger.info("Personalized for you open successfully, Now verifying show me more tab")
        ShowMeMoreTab.Second_RC_Click_On_Show_Me_More_Insight_Tab()
        self.logger.info("** Click on show me more insight tab successfully..")
        ShowMeMoreTab.Second_RC_Click_On_Exit_From_Show_Me_More_Insight()
        assert True


    def test_Second_RC_SMMI_CQ_Top_Of_Child_Chart(self,setup):
        self.logger.info("* Verifying the Card Question on Top of Child chart")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("Login successfully....")

        Card_Question = TimeTakesToCloseTheJob(self.driver)
        Card_Question.Select_Personalized_for_you_from_Home_dropdown()
        Card_Question.Second_RC_Click_On_Show_Me_More_Insight_Tab()
        time.sleep(5)
        self.logger.info("Clicked on show me more insight tab successfully...")
        actual_text = Card_Question.Second_RC_SMMI_CQ_Top_Of_Child_chart()
        print(actual_text)
        expected_text = "HOW MUCH TIME IT TAKES TO CLOSE A JOB?"
        assert actual_text == expected_text, f"Text mismatch. Expected: {expected_text}, Actual: {actual_text}"


    def test_Second_RC_SMMI_FC_ADITTCJB_By_Organization_Unit_Title(self,setup):
        self.logger.info("Verifying first child chart of How much time it takes to close job? card")
        self.logger.info("Child chart Name: Average days it takes to close the job by organization unit ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("Login successfully....")

        ChildChartTitle = TimeTakesToCloseTheJob(self.driver)
        ChildChartTitle.Select_Personalized_for_you_from_Home_dropdown()
        self.logger.info("Personalized for you open successfully..")
        ChildChartTitle.Second_RC_Click_On_Show_Me_More_Insight_Tab()
        time.sleep(2)
        actual_Title = ChildChartTitle.Second_RC_SMMI_ADITTCJ_By_Organization_Unit_Chart_Title()
        print(actual_Title)
        expected_Title = "Average Days It Takes To Close A Job By Organization Unit (Current Year)"

        if actual_Title == expected_Title:
            assert True
            self.logger.info("actual_title is matching with expected_title")
            self.logger.info("Test case passed...")
            self.logger.info("Test case executed successfully...")
        else:
            assert False
        print("Test case executed successfully...")

    def test_Second_RC_SMMI_FC_ADITTCJB_By_Organization_Unit_ViewChartTable(self,setup):
        self.logger.info("Verifying view as chart/table functionality for 1st child chart of 2nd Recruit Card ")
        self.logger.info("Child chart Name: Average days it takes to close the job by organization unit ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("Login successfully...")

        ViewChartTable = TimeTakesToCloseTheJob(self.driver)
        ViewChartTable.Select_Personalized_for_you_from_Home_dropdown()
        ViewChartTable.Second_RC_Click_On_Show_Me_More_Insight_Tab()
        time.sleep(2)
        self.logger.info("Clicked on show me more insight tab successfully...")
        ViewChartTable.Second_RC_SMMI_ADITTCJ_By_Organization_Unit_Three_Dot()
        ViewChartTable.Second_RC_SMMI_ADITTCJ_By_Organization_Unit_View_Table()
        time.sleep(3)
        ViewChartTable.Second_RC_SMMI_ADITTCJ_By_Organization_Unit_Three_Dot()
        ViewChartTable.Second_RC_SMMI_ADITTCJ_By_Organization_Unit_View_Chart()
        assert True
        self.logger.info("Test case passed...")
        self.logger.info("Test case executed successfully...")

    def test_Second_RC_SMMI_SC_ADITTCJB_By_Worksite_Title(self,setup):
        self.logger.info("Verifying the title of second child chart for How much time takes to close the job? card")
        self.logger.info("Child chart Name: Average days it takes to close the job by worksite")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("Login successfully....")

        ChildChartTitle = TimeTakesToCloseTheJob(self.driver)
        ChildChartTitle.Select_Personalized_for_you_from_Home_dropdown()
        ChildChartTitle.Second_RC_Click_On_Show_Me_More_Insight_Tab()
        self.logger.info("Clicked On show me more insight tab successfully.")
        time.sleep(2)
        actual_Title = ChildChartTitle.Second_RC_SMMI_ADITTCJ_By_Worksite_Chart_Title()
        print(actual_Title)
        expected_Title = "Average Days It Takes To Close A Job By Work Site (Current Year)"

        if actual_Title == expected_Title:
            assert True
            self.logger.info("actual_title is matching with expected_title")
            self.logger.info("Test case passed...")
            self.logger.info("Test case executed successfully...")
        else:
            assert False
        print("Test case executed successfully...")


    def test_Second_RC_SMMI_SC_ADITTCJB_By_Worksite_ViewChartTable(self,setup):
        self.logger.info("Verifying the view as table/chart functionlity of second child chart for How much time takes to close the job? card")
        self.logger.info("Child chart Name: Average days it takes to close the job by worksite")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("Login Successfully....")

        ViewTableChart = TimeTakesToCloseTheJob(self.driver)
        ViewTableChart.Select_Personalized_for_you_from_Home_dropdown()
        ViewTableChart.Second_RC_Click_On_Show_Me_More_Insight_Tab()
        time.sleep(3)
        ViewTableChart.Second_RC_SMMI_ADITTCJ_By_Worksite_Chart_Three_Dot()
        self.logger.info("clicked on Three dot successfully...")
        ViewTableChart.Second_RC_SMMI_ADITTCJ_By_Worksite_Chart_View_Table()
        self.logger.info("clicked on View as Table successfully...")
        ViewTableChart.Second_RC_SMMI_ADITTCJ_By_Worksite_Chart_Three_Dot()
        self.logger.info("Again clicked on Three dot successfully...")
        ViewTableChart.Second_RC_SMMI_ADITTCJ_By_Worksite_Chart_View_Chart()
        self.logger.info("clicked on View as Chart successfully...")
        assert True
        print("Test case executed successfully...")



    def test_Second_RC_SMMI_TC_ADITTCJB_By_Grade_Title(self,setup):
        self.logger.info("Verifying the Title of Third child chart for How much time takes to close the job? card")
        self.logger.info("Child chart Name: Average Days It Takes To Close A Job By Grade")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("Login Successfully....")

        Chart_Title = TimeTakesToCloseTheJob(self.driver)
        Chart_Title.Select_Personalized_for_you_from_Home_dropdown()
        Chart_Title.Second_RC_Click_On_Show_Me_More_Insight_Tab()
        time.sleep(2)
        actual_Title = Chart_Title.Second_RC_SMMI_ADITTCJ_By_Grade_Chart_Title()
        print(actual_Title)
        expected_Title = "Average Days It Takes To Close A Job By Grade (Current Year)"

        if actual_Title == expected_Title:
            assert True
            self.logger.info("actual_title is matching with expected_title")
            self.logger.info("Test case passed...")
            self.logger.info("Child chart title is :Average Days It Takes To Close A Job By Grade (Current Year)")
        else:
            assert False
        print("Test case executed successfully...")
        self.logger.info("Test case executed successfully...")


    def test_Second_RC_SMMI_TC_ADITTCJB_By_Grade_ViewChartTable(self,setup):
            self.logger.info("Verifying the view as chart/table functionality for How much time takes to close the job? card")
            self.logger.info("Child chart Name: Average Days It Takes To Close A Job By Grade")
            self.driver = setup
            self.driver.get(self.baseURL)
            self.driver.maximize_window()
            self.driver.implicitly_wait(30)
            self.lp = LoginPage(self.driver)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            self.logger.info("Login Successfully....")

            ViewChartTable = TimeTakesToCloseTheJob(self.driver)
            ViewChartTable.Select_Personalized_for_you_from_Home_dropdown()
            ViewChartTable.Second_RC_Click_On_Show_Me_More_Insight_Tab()
            self.logger.info("Clicked on Show me more insight successfully...")
            ViewChartTable.Second_RC_SMMI_ADITTCJ_By_Grade_Chart_Three_Dot()

            self.logger.info("clicked on Three dot successfully...")
            ViewChartTable.Second_RC_SMMI_ADITTCJ_By_Grade_Chart_View_Table()
            self.logger.info("clicked on View as Table successfully...")
            ViewChartTable.Second_RC_SMMI_ADITTCJ_By_Grade_Chart_Three_Dot()
            self.logger.info("Again clicked on Three dot successfully...")
            ViewChartTable.Second_RC_SMMI_ADITTCJ_By_Grade_Chart_View_Chart()
            self.logger.info("clicked on View as Chart successfully...")
            assert True
            print("Test case executed successfully...")


