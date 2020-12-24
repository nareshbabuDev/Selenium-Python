from commonmethods.Login import Login
from objectrepository import homePage as hp
import logging
import time
from utils import utils as utils
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

message_app        =         "//div[@class='ng-binding' and text()='Messages']"
New_mail_button           =       "//button[text()='New']"
Get_mailid_of_current_user      =  "//div[@class='gwt-Label hupa-loginfo-label']"
To                 =    "//div[contains(text(),'To')]//ancestor::td[@class='label']//following-sibling::td/textarea"
Cc                 =    "//div[contains(text(),'Cc')]//ancestor::td[@class='label']//following-sibling::td/textarea"
Bcc                =    "//div[contains(text(),'Bcc')]//ancestor::td[@class='label']//following-sibling::td/textarea"
Subject            =  "//div[text()='Subject:']/following::input[@class='gwt-TextBox']"
Send               =  "//button[text()='Send']"
# select_1st_mail    =  "//td[contains(text(),'"+login_user+"')]//following::td[text()='"+mailSubject+"']"
Inbox              =   "//div[@title='INBOX']"
sent               =   "//div[@title='Sent']"
Refresh            =   "//a[text()='Refresh']"
# Message App _ Send a email and verify the sent email is successfully received
class SingleUserMailSendAndReceive():

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def SingleUserMailSendAndReceive(self):
        try:
            driver = self.driver
            wait = self.wait
            wait.until(EC.element_to_be_clickable((By.XPATH,message_app ))).click()
            window_after = driver.window_handles[1]
            driver.switch_to.window(window_after)
            try:
                wait.until(EC.presence_of_element_located((By.XPATH,New_mail_button ))).click()
                login_user = wait.until(EC.presence_of_element_located((By.XPATH,Get_mailid_of_current_user ))).text
                time.sleep(2)
                wait.until(EC.presence_of_element_located((By.XPATH,To ))).send_keys(login_user)
                # Send random text in Subject
                mailsubject = utils.mailsubject
                wait.until(EC.presence_of_element_located((By.XPATH, Subject))).send_keys(mailsubject)
                wait.until(EC.presence_of_element_located((By.XPATH, Send))).click()
                wait.until(EC.presence_of_element_located((By.XPATH, Refresh))).click()
                try:
                    wait.until(EC.presence_of_element_located((By.XPATH, "//tr[contains(@class,'unseen')]/td[contains(text(),'"+login_user+"')]//following-sibling::td[contains(text(),'"+mailsubject+"')]"))).click()
                    logging.info('New Message is received')
                    # x = "Success"
                except:
                  logging.info('New Message is not received')
                  # x = "Failure"
                driver.close()
                window_before = driver.window_handles[0]
                driver.switch_to.window(window_before)
                wait.until(EC.element_to_be_clickable((By.XPATH, hp.home_button_xpath))).click()

            except:
                logging.info('Message App is Down')
                driver.close()
                window_before = driver.window_handles[0]
                driver.switch_to.window(window_before)
                wait.until(EC.element_to_be_clickable((By.XPATH, hp.home_button_xpath))).click()
                # x = "Failure"
        except:
            pass
