from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://opensource-demo.orangehrmlive.com/")

    # Wait for the username input field to be visible
    username_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "txtUsername"))
    )
    # Enter the username
    username_input.send_keys("Admin")

    # Find and enter the password
    password_input = driver.find_element_by_id("txtPassword")
    password_input.send_keys("admin123")

    # Find and click the login button
    login_button = driver.find_element_by_id("btnLogin")
    login_button.click()

    # Wait for the dashboard page to load (you can use a different condition)
    WebDriverWait(driver, 10).until(EC.title_contains("OrangeHRM"))

    # Compare the titles
    act_title = driver.title
    exp_title = "OrangeHRM"

    if act_title == exp_title:
        print("Login test passed..")
    else:
        print("Login test failed..")

except Exception as e:
    print("An error occurred:", e)

finally:
    driver.quit()

