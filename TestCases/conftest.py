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


# def pytest_addoption(parser):    # this will get the value from CLI /hooks
#     parser.addoption("--browser")

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name e.g. chrome/firefox/edge")


@pytest.fixture()
def browser(request):   # this will return the Browser value to setup method
    return request.config.getoption("--browser")


######################## To Genrate PyTest HTML Report###################

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





# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#
#
# import pytest
# from selenium import webdriver
#
# @pytest.fixture()
# def setup(browser):
#     if browser == 'chrome':
#         driver = webdriver.Chrome()
#         print("Launching Chrome Browser...")
#     elif browser == 'firefox':
#         driver = webdriver.Firefox()
#         print("Launching Firefox Browser...")
#     else:
#         driver = webdriver.Edge()
#     return driver
#
# def pytest_addoption(parser):    # This will get the value from CLI/hooks
#     parser.addoption("--browser")
#
# @pytest.fixture()
# def browser(request):   # This will return the Browser value to the setup method
#     return request.config.getoption("--browser")
#
# # To Generate PyTest HTML Report
#
# def pytest_configure(config):
#     metadata = getattr(config, '_metadata', None)
#     if metadata is None:
#         metadata = config._metadata = {}
#     metadata['Project Name'] = 'PeopleStrong'
#     metadata['Module Name'] = 'Analytics'
#     metadata['Tester'] = 'Madhur'
#
# # Use tryfirst=True to resolve the deprecation warning
# @pytest.hookimpl(tryfirst=True)
# def pytest_metadata(request, config, metadata):
#     metadata['PeopleStrong'] = config.getini('metadata_line').split('=')[1].strip()
#     metadata['Analytics'] = config.getini('metadata_line').split('=')[2].strip()
#     metadata['Madhur'] = config.getini('metadata_line').split('=')[3].strip()
#
# # It is a hook for deleting/Modifying Environment info in the HTML Report
# # This hook is optional, and you can remove it if not needed.
# @pytest.hookimpl(optionalhook=True)
# def pytest_metadata(config, metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)









