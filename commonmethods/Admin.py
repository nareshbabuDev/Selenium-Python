from commonmethods.Login import Login
from objectrepository import homePage as hp
from objectrepository import adminpage as ap
from utils import utils as utils
import time
import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Admin():

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def UserSearch(self):
        driver = self.driver
        wait = self.wait
        wait.until(EC.element_to_be_clickable((By.XPATH, hp.admin_icon))).click()
        logging.info('Admin App Navigated SuccessFully')
        wait.until(EC.element_to_be_clickable((By.XPATH, ap.updateuserbtn))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, ap.inputemailfield))).send_keys(utils.env["USER_ID2"])
        wait.until(EC.element_to_be_clickable((By.XPATH, ap.searchbutton))).click()


