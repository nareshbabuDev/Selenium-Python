from objectrepository import homePage as hp
import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

class Logout():
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def logout(self):
        driver = self.driver
        wait = self.wait
        driver.find_element_by_xpath(hp.logout_image_xpath).click()
        wait.until(EC.presence_of_element_located((By.XPATH, hp.logout_button_xpath)))
        logging.info("Logged out DashBoard")