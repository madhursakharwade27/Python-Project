# from selenium import  webdriver
#
# class LoginPage:
#     textbox_username_id = "username"
#     textbox_password_id = "password"
#     button_login_xpath = "//input[@id='kc-login']"
#
#     def __init__(self,driver):
#         self.driver = driver
#
#     def setUserName(self,username):
#         self.driver.find_element_by_id(self.textbox_username_id).clear()
#         self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)
#
#     def setPassword(self,password):
#         self.driver.find_element_by_id(self.textbox_password_id).clear()
#         self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)
#
#     def clickLogin(self):
#         self.driver.find_element_by_xpath(self.button_login_xpath).click()
#
#
#
#
# class LoginPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.textbox_username_id = "username"  # Replace with your actual ID for username field
#         self.textbox_password_id = "password"  # Replace with your actual ID for password field
#         self.button_login_id = "//input[@id='kc-login']"        # Replace with your actual ID for login button
#
#     def setUserName(self, username):
#         self.driver.find_element_by_id(self.textbox_username_id).clear()
#         self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)
#
#     def setPassword(self, password):
#         self.driver.find_element_by_id(self.textbox_password_id).clear()
#         self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)
#
#     def clickLogin(self):
#         self.driver.find_element_by_id(self.button_login_id).click()


#
# class LoginPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.textbox_username_id = "username"  # Replace with your actual ID for username field
#         self.textbox_password_id = "password"  # Replace with your actual ID for password field
#         self.button_login_id = "kc-login"  # Replace with your actual ID for login button
#
#     def setUserName(self, username):
#         self.driver.find_element_by_id(self.textbox_username_id).clear()
#         self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)
#
#     def setPassword(self, password):
#         self.driver.find_element_by_id(self.textbox_password_id).clear()
#         self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)
#
#     def clickLogin(self):
#         self.driver.find_element_by_id(self.button_login_id).click()


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.textbox_username_id = "username"  # Replace with your actual ID for username field
        self.textbox_password_id = "password"  # Replace with your actual ID for password field
        self.button_login_id = "kc-login"  # Replace with your actual ID for login button

    def setUserName(self, username):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.textbox_username_id))).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.textbox_password_id))).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.button_login_id))).click()