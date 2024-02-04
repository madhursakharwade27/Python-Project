import time
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from pageObjects.HowManyOpenJobsAreThereInCompany import HowManyOpenJobsInTheCompany


class Test_How_Many_Opn_Jobs_Are_There_In_The_Company:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()


    def test_verifyModuleNameOfFirstCard(self, setup):
        self.logger.info("************** TC_003__verifying the module Name of First card********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**************Login Successfully....*************")
        time.sleep(4)
        self.logger.info("*********Starting verifying your test********* ")

        # Create an instance of the page object
        ModuleNameOfFirstCard = HowManyOpenJobsInTheCompany(self.driver)
        time.sleep(2)
        ModuleNameOfFirstCard.Select_Personalized_for_you_from_Home_dropdown()
        time.sleep(10)

        actual_text = ModuleNameOfFirstCard.capture_the_text_from_first_card_header()
        expected_text = "Recruitment"
        assert actual_text == expected_text, f"Text mismatch. Expected: {expected_text}, Actual: {actual_text}"

    def test_verifyTitleOfFirstCard(self, setup):
        self.logger.info("************** TC_003A__verifying Title Of First card********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**************Login Successfully....*************")
        time.sleep(4)
        self.logger.info("*********Starting verifying your test********* ")

        # Create an instance of the page object
        TitleOfFirstCard = HowManyOpenJobsInTheCompany(self.driver)
        time.sleep(2)
        TitleOfFirstCard.Select_Personalized_for_you_from_Home_dropdown()
        time.sleep(10)

        actual_text = TitleOfFirstCard.capture_the_text_from_first_card_question()
        expected_text = "How many open jobs are there in the company?"
        assert actual_text == expected_text, f"Text mismatch. Expected: {expected_text}, Actual: {actual_text}"


    def test_Info_from_i_Icon_for_RC_FirstCard(self, setup):
        self.logger.info("*** verifying the Info of I icon for First Card (Open job in the company) ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******** Login successfully ....********")
        time.sleep(10)

        InfoiconFor_RC_FirstCard = HowManyOpenJobsInTheCompany(self.driver)
        InfoiconFor_RC_FirstCard.Select_Personalized_for_you_from_Home_dropdown()
        self.logger.info("****** Open personalized for you successfully...**")
        time.sleep(10)
        InfoiconFor_RC_FirstCard.First_RC_HoverOn_I_Icon_Near_CQ()
        time.sleep(5)

        tooltip_xpath = "//div[contains(@class, 'cdk-overlay-container')]//div[contains(@class, 'mat-tooltip')]"
        tooltip = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, tooltip_xpath)))
        time.sleep(3)

        tooltip_Info = tooltip.text
        print(tooltip_Info)

        if tooltip.text == "Shows The Jobs Which Were Approved And Open For This Year. Turn Around Time Is Defined As The Time Duration Between Job Approval Date - Job Closure Date.":
            assert True
            self.logger.info("The information of I icon is coming according to Requirement which is below")
            self.logger.info("Shows The Jobs Which Were Approved And Open For This Year. Turn Around Time Is Defined As The Time Duration Between Job Approval Date - Job Closure Date.")
            self.logger.info("Test case passed...")
        else:
            assert False
        print("Test case executed successfully...")
        self.logger.info("*** Test case executed successfully...")

    def test_ViewTable(self, setup):
        self.logger.info("************** TC_005__verifying view as table and chart functionality********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(10)
        # assert "dashboard" in self.driver.current_url.lower(), "Login not successful"

        self.logger.info("***********Login successfully......... **************")
        self.logger.info("*********** Starting view as table and view as chart validation *******")

        self.ViewAsTableChart = HowManyOpenJobsInTheCompany(self.driver)
        time.sleep(2)
        self.ViewAsTableChart.Select_Personalized_for_you_from_Home_dropdown()
        time.sleep(10)
        self.ViewAsTableChart.click_on_three_dot()
        assert self.ViewAsTableChart.is_three_dot_visible(), "Three dots not visible"

        self.ViewAsTableChart.click_on_view_table()
        self.ViewAsTableChart.is_view_table_visible()

        self.ViewAsTableChart.click_on_three_dot_again()
        assert self.ViewAsTableChart.is_three_dot_visible(), "Three dots not visible"

        self.ViewAsTableChart.click_on_view_chart()
        self.ViewAsTableChart.is_view_chart_visible()

        self.logger.info("********* your view as table and view as chart test case run successfully...******")
        self.logger.info("***********test cases Execution End*********")



###### ++++++++++++Is this Helful functionality for How many open jobs are there in the company card +++

    def test_After_Clicking_On_Submit_Button_for_First_Card(self,setup):
        self.logger.info("**** verifying the msg after clicking on submit button for open jobs *******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****** Login Successfully...*****")
        time.sleep(10)

        Msg_AfterClickingOnSubmit = HowManyOpenJobsInTheCompany(self.driver)
        Msg_AfterClickingOnSubmit.Select_Personalized_for_you_from_Home_dropdown()
        time.sleep(10)
        Msg_AfterClickingOnSubmit.First_Recruit_Card_Click_On_Yes()
        self.logger.info("**** Clicked On Yes Button Successfully...*****")
        time.sleep(3)
        self.logger.info("**** Now validating Yes & No Radio button *******")
        Msg_AfterClickingOnSubmit.First_Recruit_Card_Click_Radio_Button_No()
        self.logger.info("**** clicked on No Radio button successfully...****")
        time.sleep(3)
        Msg_AfterClickingOnSubmit.First_Recruit_Card_Click_Radio_Button_Yes()
        self.logger.info("*** Clicked on Yes Radio Button Successfully..***")
        time.sleep(2)
        Msg_AfterClickingOnSubmit.First_Recruit_Card_IsThisHelpful_SendInput("Yeah!, It is excellent!")
        time.sleep(4)
        Msg_AfterClickingOnSubmit.First_Recruit_Card_IsThisHelpful_Submit()
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
        self.driver.implicitly_wait(10)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******* Login Successfully...****")
        time.sleep(10)

        AfterClickingOnCancelButton = HowManyOpenJobsInTheCompany(self.driver)
        AfterClickingOnCancelButton.Select_Personalized_for_you_from_Home_dropdown()
        time.sleep(10)
        AfterClickingOnCancelButton.First_Recruit_Card_Click_On_No()
        time.sleep(3)
        self.logger.info("**** Now validating Yes & No Radio button *******")
        AfterClickingOnCancelButton.First_Recruit_Card_Click_Radio_Button_Yes()
        self.logger.info("**** clicked on Yes Radio button successfully...****")
        time.sleep(3)
        AfterClickingOnCancelButton.First_Recruit_Card_Click_Radio_Button_No()
        self.logger.info("*** Clicked on NO Radio Button Successfully..***")
        time.sleep(2)

        AfterClickingOnCancelButton.First_Recruit_Card_IsThisHelpful_SendInput("It is Just OK!")
        time.sleep(2)
        AfterClickingOnCancelButton.First_Recruit_Card_IsThisHelpful_Cancel()

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
        self.driver.implicitly_wait(10)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**** Login successfully...****")
        time.sleep(10)

        ClickingOn_No_Then_Submit = HowManyOpenJobsInTheCompany(self.driver)
        ClickingOn_No_Then_Submit.Select_Personalized_for_you_from_Home_dropdown()
        time.sleep(10)

        ClickingOn_No_Then_Submit.First_Recruit_Card_Click_On_No()
        time.sleep(2)
        ClickingOn_No_Then_Submit.First_Recruit_Card_IsThisHelpful_Submit()
        time.sleep(3)

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



######++ Verifying show me more insights and child charts for How many Open jobs are there in the company+++


    def test_TC_006A_Verifying_show_me_more_Tab(self, setup):
        self.logger.info("************** Tc_006A_verifying show me more insight tab ********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(10)
        self.logger.info("******** Now validation start on show me more insight ********")

        show_me_more_instance = HowManyOpenJobsInTheCompany(self.driver)
        time.sleep(2)
        show_me_more_instance.Select_Personalized_for_you_from_Home_dropdown()
        time.sleep(10)
        show_me_more_instance.click_on_show_me_more()
        time.sleep(5)
        self.logger.info("********Clicked on Show me more insight successfully********")
        show_me_more_instance.click_on_cross_to_exit_from_show_more()  # Corrected method name
        self.logger.info("*************** Quited successfully from show me more insight********")


    def test_TC_006B_CQ_RC_SMMI_OnTopOfChildChart_OpenJobCard(self, setup):
        self.logger.info("************ TC_006B validating the card Question on top of child chart *********** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(10)
        self.logger.info("********** login Successfully...**********")
        self.logger.info("****validating card question which is available on the top of child chart*******")

        show_me_more_charts = HowManyOpenJobsInTheCompany(self.driver)
        show_me_more_charts.Select_Personalized_for_you_from_Home_dropdown()
        show_me_more_charts.click_on_show_me_more()
        time.sleep(5)
        actual_text = show_me_more_charts.First_RC_SMMI_CQ_OnTopOfChildChart()
        expected_text = "HOW MANY OPEN JOBS ARE THERE IN THE COMPANY?"
        assert actual_text == expected_text, f"Text mismatch. Expected: {expected_text}, Actual: {actual_text}"


    def test_TC_006C_RC_SMMI_TitleOfFirstChildChart_OpenJobCard(self,setup):
        self.logger.info("******** TC_006C validating title of first Child chart**************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**********Login successfully....**********")
        self.logger.info("********* validating Title of first Child chart ***********")

        Title_Of_First_Child_Chart = HowManyOpenJobsInTheCompany(self.driver)
        time.sleep(2)
        Title_Of_First_Child_Chart.Select_Personalized_for_you_from_Home_dropdown()
        time.sleep(10)
        Title_Of_First_Child_Chart.click_on_show_me_more()
        time.sleep(5)
        actual_text = Title_Of_First_Child_Chart.First_RC_SMMI_OJ_ByGradeAndBand()
        print(actual_text)
        expected_text = "Number Of Open Jobs By Grade And Band (Current Year)"
        if actual_text == expected_text:
            assert True
        else:
            assert False
        print("Test case executed successfully")



    def test_TC_006D_RC_SMMI_FC_DrillIcon(self, setup):
        self.logger.info("****** TC_006D_verifying Drill_icon_first child chart in Recruit open job****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***********Login successful... **************")
        self.logger.info("***********Starting hover and capture text validation *******")

        self.Drill_Icon_OpenJobsByGradeAndBand = HowManyOpenJobsInTheCompany(self.driver)
        time.sleep(2)
        self.Drill_Icon_OpenJobsByGradeAndBand.Select_Personalized_for_you_from_Home_dropdown()
        time.sleep(10)
        self.Drill_Icon_OpenJobsByGradeAndBand.click_on_show_me_more()
        time.sleep(5)
        self.logger.info("********* clicked on Show me more insight successfully...*****")
        captured_text = self.Drill_Icon_OpenJobsByGradeAndBand.capture_text_after_hovering()
        time.sleep(5)
        print(captured_text)

        expected_text = "Click On Column To Drilldown On The Charts"

        if captured_text == expected_text:
            self.logger.info(f"Captured text after hovering: {captured_text}")
            self.logger.info("Captured text matches the expected text.")
        else:
            self.logger.error(f"Expected text: {expected_text}")
            self.logger.error(f"Captured text after hovering: {captured_text}")
            self.logger.error("Captured text does not match the expected text.")

        self.driver.close()
        self.logger.info("********** Ending hover and capture text validation test *********")


    def test_TC_006E_RC_SMMI_FC_ViewTableChart(self,setup):
        self.logger.info("*****TC_006E Verifying view as table chart for open job grade and band******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("******* Login Successfully...***********")
        self.logger.info("**** verifying view as table and view as chart for open job by grade and band ***")

        jobs_grade_band_viewTableChart = HowManyOpenJobsInTheCompany(self.driver)
        time.sleep(2)
        jobs_grade_band_viewTableChart.Select_Personalized_for_you_from_Home_dropdown()
        time.sleep(10)
        jobs_grade_band_viewTableChart.click_on_show_me_more()
        self.logger.info("****** Clicked on show me more insight successfully*****")

        jobs_grade_band_viewTableChart.First_RC_SMMI_OJ_ByGradeAndBand_ThreeDot()
        time.sleep(4)
        jobs_grade_band_viewTableChart.First_RC_SMMI_OJ_ByGradeAndBand_ViewAsTable()
        time.sleep(4)
        jobs_grade_band_viewTableChart.First_RC_SMMI_OJ_ByGradeAndBand_ThreeDot()
        time.sleep(4)
        jobs_grade_band_viewTableChart.First_RC_SMMI_OJ_ByGradeAndBand_ViewAsChart()

    def test_TC_006F_RC_SMMI_SC_Scroll_To_OpeingByHiringMngr(self, setup):
        self.logger.info("*** TC_006F scrolling to the hiring manager chart *** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********* login successfully...********")

        time.sleep(10)  # Add a wait to ensure the page is loaded completely

        ScrollToOpeningByHiringManager = HowManyOpenJobsInTheCompany(self.driver)
        time.sleep(2)
        ScrollToOpeningByHiringManager.Select_Personalized_for_you_from_Home_dropdown()
        time.sleep(10)
        ScrollToOpeningByHiringManager.click_on_show_me_more()
        time.sleep(10)
        self.logger.info("********** Clicked on show me more insight successfully")
        # Call the method to scroll to the desired element
        ScrollToOpeningByHiringManager.First_RC_SMMI_Opening_By_Hiring_mngr_scroll_to_element()

        assert True, "Opening by hiring manager element is not visible after scrolling"

        self.driver.close()
        self.logger.info("********** Scroll to Opening by hiring manager element test completed *********")


    def test_TC_006G_RC_SMMI_SC_VerifyTitle_OpeningByHiringMngr(self, setup):
        self.logger.info("*** TC_006G verifying the opening by hiring manager title *** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********* login successfully...********")

        time.sleep(10)  # Add a wait to ensure the page is loaded completely

        TitleOpeningByHiringManager = HowManyOpenJobsInTheCompany(self.driver)
        time.sleep(2)
        TitleOpeningByHiringManager.Select_Personalized_for_you_from_Home_dropdown()
        time.sleep(10)
        TitleOpeningByHiringManager.click_on_show_me_more()
        time.sleep(15)
        self.logger.info("********** Clicked on show me more insight successfully")

        actual_text = TitleOpeningByHiringManager.First_RC_SMMI_Opening_By_Hiring_mngr_chartTitle()
        expected_text = "Opening By Hiring Manager (Current Year)"

        if actual_text == expected_text:
            assert True
            self.logger.info("****** Test case is passed actual_text is matching with expected_text*******")
        else:
            assert False

        self.driver.quit()
        self.logger.info("******* Test case executed successfully.. ***********")



    def test_TC_006H_RC_SMMI_TC_Scroll_To_OpeingByRecruiter(self, setup):
        self.logger.info("*** TC_006H scrolling to the Opening By Recruiter chart *** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********* login successfully...********")

        time.sleep(10)  # Add a wait to ensure the page is loaded completely

        ScrollToOpeningRecruiter = HowManyOpenJobsInTheCompany(self.driver)
        time.sleep(2)
        ScrollToOpeningRecruiter.Select_Personalized_for_you_from_Home_dropdown()
        time.sleep(10)
        ScrollToOpeningRecruiter.click_on_show_me_more()
        time.sleep(10)
        self.logger.info("********** Clicked on show me more insight successfully")
        # Call the method to scroll to the desired element
        ScrollToOpeningRecruiter.First_RC_SMMI_Opening_By_Recruiter_scroll_to_element()

        assert True, "Opening by Recruiter element is not visible after scrolling"

        self.driver.close()
        self.logger.info("********** Scroll to Opening by Recruiter element test completed *********")


    def test_TC_006I_RC_SMMI_TC_VerifyTitle_OpeningByRecruiter(self, setup):
        self.logger.info("*** TC_006I verifying the opening by Recruiter Chart title *******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********* login successfully...********")
        self.logger.info("******** Validating The chart title for Opening By Recruiter*************")

        time.sleep(10)  # Add a wait to ensure the page is loaded completely

        TitleOpeningByRecruiter = HowManyOpenJobsInTheCompany(self.driver)
        time.sleep(2)
        TitleOpeningByRecruiter.Select_Personalized_for_you_from_Home_dropdown()
        time.sleep(10)
        TitleOpeningByRecruiter.click_on_show_me_more()
        time.sleep(10)
        self.logger.info("********** Clicked on show me more insight successfully")

        actual_text = TitleOpeningByRecruiter.First_RC_SMMI_Opening_By_Recruiter_chartTitle()
        expected_text = "Opening By Recruiter (Current Year)"

        if actual_text == expected_text:
            assert True
            self.logger.info("****** Test case is passed actual_text is matching with expected_text*******")
        else:
            assert False

        self.driver.quit()
        self.logger.info("******* Test case executed successfully.. ***********")


    def test_TC_006J_RC_SMMI_FC_Scroll_To_OpenJobsByWorklocation(self, setup):
        self.logger.info("*** TC_006J scrolling to the Open jobs by worklocation chart *** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********* login successfully...********")

        time.sleep(10)  # Add a wait to ensure the page is loaded completely

        ScrollToOpenJobsByWorklocation = HowManyOpenJobsInTheCompany(self.driver)
        time.sleep(2)
        ScrollToOpenJobsByWorklocation.Select_Personalized_for_you_from_Home_dropdown()
        time.sleep(10)
        ScrollToOpenJobsByWorklocation.click_on_show_me_more()
        time.sleep(10)
        self.logger.info("********** Clicked on show me more insight successfully")
        # Call the method to scroll to the desired element
        ScrollToOpenJobsByWorklocation.First_RC_SMMI_OpenJobsByWorklocation_scroll_to_element()

        assert True, "Open Jobs By Work location element is not visible after scrolling"

        self.driver.close()
        self.logger.info("********** Scroll to Open jobs by worklocation element test completed *********")


    def test_TC_006K_RC_SMMI_FC_VerifyTitle_OpenJobsByWorklocation(self, setup):
        self.logger.info("*** TC_006K verifying the open jobs by work location Chart title *******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********* login successfully...********")
        self.logger.info("******** Validating The chart title for Open Jobs by work location*************")

        time.sleep(10)  # Add a wait to ensure the page is loaded completely

        TitleOpenJobsByWorklocation = HowManyOpenJobsInTheCompany(self.driver)
        time.sleep(2)
        TitleOpenJobsByWorklocation.Select_Personalized_for_you_from_Home_dropdown()
        time.sleep(10)
        TitleOpenJobsByWorklocation.click_on_show_me_more()
        time.sleep(10)
        self.logger.info("********** Clicked on show me more insight successfully")

        actual_text = TitleOpenJobsByWorklocation.First_RC_SMMI_OpenJobsByWorklocation_chartTitle()
        expected_text = "Number Of Open Jobs By Work Location (Current Year)"

        if actual_text == expected_text:
            assert True
            self.logger.info("****** Test case is passed actual_text is matching with expected_text*******")
        else:
            assert False

        self.driver.quit()
        self.logger.info("******* Test case executed successfully.. ***********")


    def test_TC_006L_RC_SMMI_FC_DrillIcon_OpenJobsByWorklocation(self,setup):
        self.logger.info("************** TC_006L Validating the drill icon for open jobs by work location chart *********** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****** Login Successfully...**********")
        self.logger.info(" ******* validation Start for drill icon **************")
        time.sleep(10)

        self.OpenJobsByWorklocation_drillIcon = HowManyOpenJobsInTheCompany(self.driver)
        time.sleep(2)
        self.OpenJobsByWorklocation_drillIcon.Select_Personalized_for_you_from_Home_dropdown()
        time.sleep(10)
        self.OpenJobsByWorklocation_drillIcon.click_on_show_me_more()
        time.sleep(5)
        self.logger.info("********* clicked on Show me more insight successfully...*****")
        captured_text = self.OpenJobsByWorklocation_drillIcon.First_RC_SMMI_OpenJobsByWorklocation_DrillIcon()
        time.sleep(5)
        print(captured_text)

        expected_text = "Click On Column To Drilldown On The Charts"

        if captured_text == expected_text:
            self.logger.info(f"Captured text after hovering: {captured_text}")
            self.logger.info("Captured text matches the expected text.")
        else:
            self.logger.error(f"Expected text: {expected_text}")
            self.logger.error(f"Captured text after hovering: {captured_text}")
            self.logger.error("Captured text does not match the expected text.")

        self.driver.close()
        self.logger.info("********** Ending hover and capture text validation test *********")


    def test_TC_006M_RC_SMMI_FC_ViewTableChart_OpenJobsByWorklocation(self,setup):
        self.logger.info("******* TC_006M Verifyting the View as table and view as chart functionality for open jobs by worklocation chart ********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********* Login successfully...************")
        self.logger.info("********* validating view as table/chart fuctionality for open jobs by worklocation chart *********")

        OpenJobsByWorklocation = HowManyOpenJobsInTheCompany(self.driver)
        time.sleep(2)
        OpenJobsByWorklocation.Select_Personalized_for_you_from_Home_dropdown()
        time.sleep(10)
        OpenJobsByWorklocation.click_on_show_me_more()
        self.logger.info("********** click on show me more insight successfully *************")

        OpenJobsByWorklocation.First_RC_SMMI_OpenJobsByWorklocation_ThreeDot()
        time.sleep(4)
        OpenJobsByWorklocation.First_RC_SMMI_OpenJobsByWorklocation_ViewTable()
        time.sleep(4)
        OpenJobsByWorklocation.First_RC_SMMI_OpenJobsByWorklocation_ThreeDot()
        time.sleep(4)
        OpenJobsByWorklocation.First_RC_SMMI_OpenJobsByWorklocation_ViewChart()
        assert True



##### ++++++++++++++++++Applicant By Stage For Open Jobs++++++++++++++++++++++++

    def test_TC_006N_RC_SMMI_FC_Scroll_To_ApplicantByStageForOpenJobs(self,setup):
        self.logger.info("*** TC_006N scrolling to the Applicant By Stage For Open Job chart *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********* login successfully...********")

        time.sleep(10)  # Add a wait to ensure the page is loaded completely

        ScrollToApplicantByStageForOpenJob = HowManyOpenJobsInTheCompany(self.driver)
        time.sleep(2)
        ScrollToApplicantByStageForOpenJob.Select_Personalized_for_you_from_Home_dropdown()
        time.sleep(10)
        ScrollToApplicantByStageForOpenJob.click_on_show_me_more()
        time.sleep(10)
        self.logger.info("********** Clicked on show me more insight successfully")
        # Call the method to scroll to the desired element
        ScrollToApplicantByStageForOpenJob.First_RC_SMMI_ApplicantByStageForOpenJobs_scroll_to_element()

        assert True, "Applicant By Stage For Open Job element is not visible after scrolling"

        self.driver.close()
        self.logger.info("********** Scroll to Applicant By stage for open job element test completed *********")


    def test_TC_006O_RC_SMMI_FC_VerifyTitle_ApplicantByStageForOpenJob(self, setup):
        self.logger.info("*** TC_006O verifying the Applicant By Stage for open job Chart title *******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********* login successfully...********")
        self.logger.info("******** Validating The chart title for Applicant by Stage for open jobs*************")

        time.sleep(10)  # Add a wait to ensure the page is loaded completely

        TitleApplicantByStageForOpenJob = HowManyOpenJobsInTheCompany(self.driver)
        time.sleep(2)
        TitleApplicantByStageForOpenJob.Select_Personalized_for_you_from_Home_dropdown()
        time.sleep(10)
        TitleApplicantByStageForOpenJob.click_on_show_me_more()
        time.sleep(10)
        self.logger.info("********** Clicked on show me more insight successfully")

        actual_text = TitleApplicantByStageForOpenJob.First_RC_SMMI_ApplicantByStageForOpenJobs_chartTitle()
        expected_text = "Applicant By Stage For Open Jobs (Current Year)"

        if actual_text == expected_text:
            assert True
            self.logger.info("****** Test case is passed actual_text is matching with expected_text*******")
        else:
            assert False

        self.driver.quit()
        self.logger.info("******* Test case executed successfully.. ***********")


    def test_TC_006P_RC_SMMI_FC_DrillIcon_ApplicantByStageForOpenJob(self,setup):
        self.logger.info("************** TC_006P Validating the drill icon for Applicant By Stage for open job chart *********** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****** Login Successfully...**********")
        self.logger.info(" ******* validation Start for drill icon **************")
        time.sleep(10)

        self.ApplicantByStageForOpenJob_drillIcon = HowManyOpenJobsInTheCompany(self.driver)
        time.sleep(2)
        self.ApplicantByStageForOpenJob_drillIcon.Select_Personalized_for_you_from_Home_dropdown()
        time.sleep(10)
        self.ApplicantByStageForOpenJob_drillIcon.click_on_show_me_more()
        time.sleep(5)
        self.logger.info("********* clicked on Show me more insight successfully...*****")
        captured_text = self.ApplicantByStageForOpenJob_drillIcon.First_RC_SMMI_Applicant_By_Stage_For_OpenJobs_DrillIcon()
        time.sleep(5)
        print(captured_text)

        expected_text = "Click On Column To Drilldown On The Charts"

        if captured_text == expected_text:
            self.logger.info(f"Captured text after hovering: {captured_text}")
            self.logger.info("Captured text matches the expected text.")
        else:
            self.logger.error(f"Expected text: {expected_text}")
            self.logger.error(f"Captured text after hovering: {captured_text}")
            self.logger.error("Captured text does not match the expected text.")

        self.driver.close()
        self.logger.info("********** Ending hover and capture text validation test *********")


    def test_TC_006Q_RC_SMMI_FC_ViewTableChart_ApplicantByStageForOpenJob(self,setup):
        self.logger.info("**TC_006Q Verifyting the View as table/chart functionality for Applicant By stage for open job chart**")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********* Login successfully...************")
        self.logger.info("*** validating view as table/chart functionality for applicant by stage for OpenJobs chart**")

        ApplicantByStageForOpenJob = HowManyOpenJobsInTheCompany(self.driver)
        time.sleep(2)
        ApplicantByStageForOpenJob.Select_Personalized_for_you_from_Home_dropdown()
        time.sleep(10)
        ApplicantByStageForOpenJob.click_on_show_me_more()
        self.logger.info("********** click on show me more insight successfully *************")

        ApplicantByStageForOpenJob.First_RC_SMMI_Applicant_By_Stage_For_Open_Jobs_ThreeDot()
        time.sleep(4)
        ApplicantByStageForOpenJob.First_RC_SMMI_Applicant_By_Stage_For_Open_Jobs_ViewTable()
        time.sleep(4)
        ApplicantByStageForOpenJob.First_RC_SMMI_Applicant_By_Stage_For_Open_Jobs_ThreeDot()
        time.sleep(4)
        ApplicantByStageForOpenJob.First_RC_SMMI_Applicant_By_Stage_For_Open_Jobs_ViewChart()
        assert True


