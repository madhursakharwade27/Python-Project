import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser...")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox Browser...")
    else:
        driver = webdriver.Edge()
    return driver


def pytest_addoption(parser):    # this will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):   # this will return the Browser value to setup method
    return request.config.getoption("--browser")


######################## To Genrate PyTest HTML Report###################

#### it is hook for adding environment info to HTML Report
#
def pytest_configure(config):
    metadata = getattr(config, '_metadata', None)
    if metadata is None:
        metadata = config._metadata = {}
    metadata['Project Name'] = 'PeopleStrong'
    metadata['Module Name'] = 'Analytics'
    metadata['Tester'] = 'Madhur'

##### It is hook for delete/Modify Environment info to HTML Report

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)
