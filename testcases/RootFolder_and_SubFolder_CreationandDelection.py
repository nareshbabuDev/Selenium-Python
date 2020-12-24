import sys
from commonmethods import Login
import logging
import time
from utils import utils as utils
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# test data
home_button_xpath="//*[@id = 'appHome_menu']"
msgicon="//*[@id='appMessages_menu']"
inboxbtn="//div[@title='INBOX']"
rootfolder="//div[contains(@class,'gwt-Hyperlink')]/following::a[contains(text(),'Root Folder')]"
refreshbtn="//td/div/a[contains(text(),'Refresh')]"
SubFolder="//div[contains(@class,'gwt-Hyperlink')]/following::a[contains(text(),'Sub Folder')]"
rename="//a[text()='Rename']"

class RootFolder_and_SubFolder_CreationandDelection():
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def RootFolder_and_SubFolder_CreationandDelection(self):
        try:
            driver = self.driver
            wait = self.wait
            try:
                wait.until(EC.element_to_be_clickable((By.XPATH, home_button_xpath))).click()
                logging.info('Home page Navigated SuccessFully')
            except:
                Login(driver, wait).login_failure_handling()

            wait.until(EC.element_to_be_clickable((By.XPATH, msgicon))).click()
            window_after = driver.window_handles[1]
            driver.switch_to.window(window_after)

            try:
                #rootfolder creation
                logging.info('Navigated to Message app home page SuccessFully')
                time.sleep(3)
                wait.until(EC.element_to_be_clickable((By.XPATH, inboxbtn))).click()
                time.sleep(3)
                wait.until(EC.element_to_be_clickable((By.XPATH, refreshbtn))).click()
                time.sleep(3)
                wait.until(EC.element_to_be_clickable((By.XPATH, rootfolder))).click()
                time.sleep(3)
                wait.until(EC.element_to_be_clickable((By.XPATH, rootfolder)))
                actions = ActionChains(driver)
                actions.send_keys("RootFolder").perform()
                time.sleep(3)
                ActionChains(driver).send_keys(Keys.ENTER).perform()
                time.sleep(3)
                logging.info("Root folder created")
                time.sleep(3)
                #rename
                # a=wait.until(EC.element_to_be_clickable((By.XPATH, "// div[text() = 'RootFolder']"))).text
                # print(a)
                # wait.until(EC.element_to_be_clickable((By.XPATH, "// div[text() = 'RootFolder']"))).click()
                # wait.until(EC.element_to_be_clickable((By.XPATH,rename))).click()
                # time.sleep(3)
                # actions1 = ActionChains(driver)
                # actions1.send_keys(Keys.CLEAR).perform()
                # actions1.send_keys("RENAME").perform()
                # actions1.send_keys(Keys.ENTER).perform()
                # b=wait.until(EC.element_to_be_clickable((By.XPATH,"// div[contains(text(),'RootFolder')]" ))).text
                # print(b)
                # if a!=b:
                #     logging.info("Root folder renamed")
                # else:
                #     logging.info("Root folder not renamed")

                #delete
                time.sleep(3)
                wait.until(EC.element_to_be_clickable((By.XPATH,"// div[contains(text(),'RootFolder')]" ))).click()
                time.sleep(3)
                wait.until(EC.element_to_be_clickable((By.XPATH, "// a[text() = 'Delete']"))).click()
                time.sleep(3)
                wait.until(EC.element_to_be_clickable((By.XPATH, "// div[@class ='cbg-ButtonContent'][text()='Ok']"))).click()
                time.sleep(5)
                logging.info("Root folder deleted")

                #subfoldercreation
                time.sleep(3)
                wait.until(EC.element_to_be_clickable((By.XPATH, inboxbtn))).click()
                time.sleep(3)
                wait.until(EC.element_to_be_clickable((By.XPATH, refreshbtn))).click()
                time.sleep(3)
                wait.until(EC.element_to_be_clickable((By.XPATH,SubFolder))).click()
                time.sleep(3)
                b = wait.until(EC.element_to_be_clickable((By.XPATH, SubFolder)))
                b.actions = ActionChains(driver)
                b.actions.send_keys("subFolder").perform()
                time.sleep(3)
                ActionChains(driver).send_keys(Keys.ENTER).perform()
                time.sleep(3)
                logging.info("subFolder folder created")
                time.sleep(3)
                wait.until(EC.element_to_be_clickable((By.XPATH, inboxbtn))).click()
                wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[contains(text(),'INBOX')]/preceding::img )[2]"))).click()
                time.sleep(3)
                wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='subFolder']"))).click()
                time.sleep(3)
                #rename
                # c = wait.until(EC.element_to_be_clickable((By.XPATH, "// div[text() = 'subFolder']"))).text
                # print(c)
                # wait.until(EC.element_to_be_clickable((By.XPATH, "// div[text() = 'subFolder']"))).click()
                # wait.until(EC.element_to_be_clickable((By.XPATH, rename))).click()
                # time.sleep(3)
                # actions.send_keys("renamed").perform()
                # ActionChains(driver).send_keys(Keys.ENTER).perform()
                # d = wait.until(EC.element_to_be_clickable((By.XPATH, "// div[contains(text(),'subFolder')]"))).text
                # print(d)
                # if c != d:
                #     logging.info("sub  folder renamed")
                # else:
                #     logging.info("sub folder not renamed")
                #delete
                wait.until(EC.element_to_be_clickable((By.XPATH, "// a[text() = 'Delete']"))).click()
                time.sleep(3)
                wait.until(EC.element_to_be_clickable((By.XPATH, "// div[@class ='cbg-ButtonContent'][text()='Ok']"))).click()
                logging.info("subFolder folder Deleted")
                time.sleep(3)
                driver.close()
                window_before = driver.window_handles[0]
                driver.switch_to.window(window_before)
                wait.until(EC.element_to_be_clickable((By.XPATH, home_button_xpath))).click()

            except:
                driver.close()
                window_before = driver.window_handles[0]
                driver.switch_to.window(window_before)
                logging.info('Message App is Down, So Again Navigated to Home page!!!')
                wait.until(EC.element_to_be_clickable((By.XPATH, home_button_xpath))).click()

        except:
            driver.close()
            window_before = driver.window_handles[0]
            driver.switch_to.window(window_before)
            wait.until(EC.element_to_be_clickable((By.XPATH, home_button_xpath))).click()