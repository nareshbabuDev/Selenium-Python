import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from utils import utils as utils
from commonmethods.Login import Login
import os
from commonmethods.Logout import Logout
global driver
@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver
    desired_cap = {
                'platform': utils.saucelabsconfig["platform"],
                'browserName': utils.saucelabsconfig["browserName"],
                'version': utils.saucelabsconfig["version"],
                'build': utils.saucelabsconfig["build"],
                'name': utils.saucelabsconfig["name"],
            }
    username = utils.saucelabsconfig["username"]
    access_key = utils.saucelabsconfig["access_key"]

    file_path = os.getcwd()
    if (utils.saucelabsconfig["SAUCELABSSTATUS"] == False):
        options = Options()
        options.add_argument("--headless") # Runs Chrome in headless mode.
        options.add_argument('--no-sandbox') # # Bypass OS security model
        options.add_argument('start-maximized')
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        # driver = webdriver.Chrome(executable_path=file_path+"/drivers/chromedriver", chrome_options=options)
        print ("Headless Chrome Initialized on Linux OS")
        driver = webdriver.Chrome(executable_path=file_path+"/drivers/chromedriver")
        #options = webdriver.ChromeOptions()
        #options.add_experimental_option('w3c', False)
    else:
        driver = webdriver.Remote(
            command_executor='https://{}:{}@ondemand.saucelabs.com:443/wd/hub'.format(username, access_key),
            desired_capabilities=desired_cap)
    wait = WebDriverWait(driver, 15)
    driver.implicitly_wait(20)
    # driver.maximize_window()
    driver.set_window_size(1920, 1080)
    request.cls.driver = driver
    request.cls.wait = wait
    Login(driver,wait).login()
    yield
    Logout(driver,wait).logout()
    driver.close()
    driver.quit()
