import pytest
from selenium import webdriver


@pytest.fixture()
def setup():
    #if browser == 'Chrome':
      #  driver= webdriver.Chrome()
       # print("lounching chrome browser.....")
    #elif browser == 'Firefox':
        driver = webdriver.Firefox()
      #  print("lounching Firefox browser.....")
    #else:
      #  driver=webdriver.Ie
        return driver


# def pytest_adoption(parser):
#     parser.addoption("--browser")
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")
#####################################################pytest HTML rEPORT############3
def pytest_configure(config):
    config._metadata['Project Name']='nop Commerce'
    config._metadata['Module Name']='Customer'
    config._metadata['Tester']='Pavan'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)


