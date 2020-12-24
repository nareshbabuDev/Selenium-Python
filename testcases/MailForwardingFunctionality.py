from commonmethods.Login import Login
from objectrepository import homePage as hp
from objectrepository import loginPage as lp
import logging
import time
from utils import utils as utils
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

message_app        =         "//div[@class='ng-binding' and text()='Messages']"
New_mail_button           =       "//button[text()='New']"
Get_mailid_of_current_user      =  "//div[@class='gwt-Label hupa-loginfo-label']"
To                 =    "//div[contains(text(),'To')]//ancestor::td[@class='label']//following-sibling::td/textarea"
Cc                 =    "//div[contains(text(),'Cc')]//ancestor::td[@class='label']//following-sibling::td/textarea"
Bcc                =    "//div[contains(text(),'Bcc')]//ancestor::td[@class='label']//following-sibling::td/textarea"
Subject            =  "//div[text()='Subject:']/following::input[@class='gwt-TextBox']"
Send               =  "//button[text()='Send']"
To_select_1st_mail = "//tr[@class='hupa-msgtable-row'][1]"
# To_select_1st_dropdown_user = "//strong[text() = utils.env["UserMailID2"]]"
# select_1st_mail    =  "//td[contains(text(),'"+login_user+"')]//following::td[text()='"+mailSubject+"']"
Inbox              =   "//div[@title='INBOX']"
sent               =   "//div[@title='Sent']"
Refresh            =   "//a[text()='Refresh']"
Forward_Mail       =  "//button[text()='Forward']"
# Message App _ Send a email and verify the sent email is successfully received
class MailForwardingFunctionality():

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def MailForwardingFunctionality(self):
        try:
            driver = self.driver
            wait = self.wait
            wait.until(EC.element_to_be_clickable((By.XPATH,message_app ))).click()
            window_after = driver.window_handles[1]
            driver.switch_to.window(window_after)
            try:

                wait.until(EC.presence_of_element_located((By.XPATH, Inbox)))
                time.sleep(3)
                login_user = wait.until(EC.presence_of_element_located((By.XPATH, Get_mailid_of_current_user))).text
                wait.until(EC.presence_of_element_located((By.XPATH,"//tr[@class='hupa-msgtable-row'][1]"))).click()
                time.sleep(3)
                wait.until(EC.presence_of_element_located((By.XPATH,Forward_Mail ))).click()
                time.sleep(3)
                wait.until(EC.presence_of_element_located((By.XPATH,To))).send_keys(utils.env["UserMailID1"])
                wait.until(EC.presence_of_element_located((By.XPATH, "//strong[text() = 'gsi.power_gsihealth@escrowdirect.gsihealth.net']"))).click()
                Current_subject = wait.until(EC.presence_of_element_located((By.XPATH, Subject))).get_attribute("value")
                # logging.info(Current_subject)
                # print(Current_subject)
                wait.until(EC.presence_of_element_located((By.XPATH, Send))).click()
                logging.info('Mail is Forwarded')
                try:
                    wait.until(EC.presence_of_element_located((By.XPATH, Refresh))).click()
                    time.sleep(5)
                    wait.until(EC.presence_of_element_located((By.XPATH, "//tr[contains(@class,'unseen')]/td[contains(text(),'"+login_user+"')]//following-sibling::td[contains(text(),'"+Current_subject+"')]"))).click()
                    logging.info('New Mail is received')
                    driver.close()
                    window_before = driver.window_handles[0]
                    driver.switch_to.window(window_before)
                    wait.until(EC.element_to_be_clickable((By.XPATH, hp.home_button_xpath))).click()
                    # x = "Success"
                except:
                  logging.info('New Message is not received')
                  driver.close()
                  window_before = driver.window_handles[0]
                  driver.switch_to.window(window_before)
                  wait.until(EC.element_to_be_clickable((By.XPATH, hp.home_button_xpath))).click()

            except:
              logging.info('Mail is not Forwarded')
              driver.close()
              window_before = driver.window_handles[0]
              driver.switch_to.window(window_before)
              wait.until(EC.element_to_be_clickable((By.XPATH, hp.home_button_xpath))).click()

        except:
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.home_button_xpath))).click()
            pass

