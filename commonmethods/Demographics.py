from objectrepository import demographicsPage as dp
from objectrepository import homePage as hp
from utils import utils as utils
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class Demographics():
    def __init__(self, driver,wait):
        self.driver = driver
        self.wait = wait

    # patient search functionality
    def demographics_search(self):
        driver= self.driver
        wait = self.wait
        wait.until(EC.presence_of_element_located((By.XPATH, hp.demographics_button_xpath))).click()
        try:
            self.driver.find_element_by_xpath(hp.reset_button_xpath).click()
        except:
            pass
        wait.until(EC.presence_of_element_located((By.XPATH, dp.patient_lastname_textbox_xpath))).send_keys(utils.env["PATIENT_LAST_NAME"])
        wait.until(EC.presence_of_element_located((By.XPATH, dp.patient_firstname_textbox_xpath))).send_keys(utils.env["PATIENT_FIRST_NAME"])
        time.sleep(3)
        wait.until(EC.presence_of_element_located((By.XPATH, dp.patient_search_button_xpath))).click()



