import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        print("Launching Chrome Browser...")
    elif browser == 'firefox':
        firefox_options = Options()
        firefox_options.add_argument("--headless")
        driver = webdriver.Firefox(options=firefox_options)
        print("Launching Firefox Browser...")
    elif browser == 'edge':
        edge_options = Options()
        edge_options.add_argument("--headless")
        driver = webdriver.Edge(options=edge_options)
        print("Launching Edge Browser...")
    else:
        raise ValueError(f"Invalid browser option: {browser}. Please use 'chrome', 'firefox', or 'edge'")
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name e.g. chrome/firefox/edge")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# Rest of the code remains unchanged

######################## To Generate PyTest HTML Report ###################

def pytest_configure(config):
    metadata = getattr(config, '_metadata', None)
    if metadata is None:
        metadata = config._metadata = {}
    metadata['Project Name'] = 'PeopleStrong'
    metadata['Module Name'] = 'Analytics'
    metadata['Tester'] = 'Madhur'

##### It is a hook for deleting/Modifying Environment info to HTML Report

# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)

import pytest

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


