import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

@pytest.fixture()
def setup():
    if browser == 'firefox':
        service_obj = FirefoxService('\\geckodriver.exe')  # Path to GeckoDriver
        driver = webdriver.Firefox(service=service_obj)
    elif browser == 'edge':
        service_obj = EdgeService('\\msedgedriver.exe')  # Path to EdgeDriver
        driver = webdriver.Edge(service=service_obj)
    else:
        # default browser, if you miss to pass an argument it will pick default browser
        service_obj = Service('C:\\browserdriver\\chromedriver-win64\\chromedriver.exe')  # Path to ChromeDriver
        driver = webdriver.Chrome(service=service_obj)
    return driver

def pytest_addoption(parser):  # This will get the value from cli/hooks
    parser.addoption('--browser')

@pytest.fixture()
def browser(request):  # This will return the browser value to the setup method
    return request.config.getoption('--browser')

####################### PyTest HTML hooks #######################
# It is hook for adding environment info to HTML reports
def pytest_configure(config):
    config.stash['Project Name'] = 'nop commerce'
    config.stash['Module name'] = 'customers'
    config.stash['Tester'] = 'Deepa'

# It is hook for delete/modify environment info in HTML report
@pytest.mark.optionalhook
def pytest_metada(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


