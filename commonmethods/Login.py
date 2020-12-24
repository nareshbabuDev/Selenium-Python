from objectrepository import loginPage as lp
from utils import utils as utils
import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

class Login():
    def __init__(self, driver,wait):
        self.driver = driver
        self.wait = wait

    # User login functionality
    def login(self):
        driver = self.driver
        wait = self.wait
        driver.get(utils.env["URL"])
        driver.find_element_by_xpath(lp.username_textbox_xpath).clear()
        driver.find_element_by_xpath(lp.username_textbox_xpath).send_keys(utils.env["USER_ID1"])
        driver.find_element_by_xpath(lp.password_textbox_xpath).clear()
        driver.find_element_by_xpath(lp.password_textbox_xpath).send_keys(utils.env["PASSWORD"])
        login = wait.until(EC.element_to_be_clickable((By.XPATH,lp.login_button_xpath )))
        # login = driver.find_element_by_xpath(lp.login_button_xpath)
        actions = ActionChains(driver)
        actions.move_to_element(login).click().perform()

        try:
            driver.find_element_by_xpath(lp.samsha_checkbox_xpath).click()
            driver.find_element_by_xpath(lp.samsha_button_xpath).click()
        except:
            pass
        try:
            driver.find_element_by_xpath(lp.gotit_button_xpath).click()
        except:
            pass

        logging.info("Logged into DashBoard")
