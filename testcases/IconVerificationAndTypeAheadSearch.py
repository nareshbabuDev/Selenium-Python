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
Bcc_label = "//a[@class='gwt-Anchor' and text()='Bcc:']"
App_logo = "//div[contains(@style,'logo.png')]"
First_mail_in_inbox = "//table[@class= 'dataTable']//tr[@class= 'hupa-msgtable-row']"
Reply = "//button[text()='Reply']"
Reply_All = "//button[text()='Reply All']"
Forward = "//button[text()='Forward']"
# "//td[@role ='menuitem' and contains(normalize-space( ) ,'Gsi ')]"
# "//td[contains(normalize-space( ) ,'escrow')]/strong[contains(.,'Power')]"
# "//td[contains(normalize-space( ) ,'escrow')]/strong[contains(.,'Power')]"
# "//td[@role= 'menuitem' and 'esautomationone_test@escrowdirect.gsihealth.net']"
# Message App _ Send a email and verify the sent email is successfully received
class IconVerificationAndTypeAheadSearch():

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def IconVerificationAndTypeAheadSearch(self):
        try:
            driver = self.driver
            wait = self.wait
            wait.until(EC.element_to_be_clickable((By.XPATH,message_app ))).click()
            window_after = driver.window_handles[1]
            driver.switch_to.window(window_after)
            try:
                wait.until(EC.presence_of_element_located((By.XPATH,Inbox ))).click()
                wait.until(EC.presence_of_element_located((By.XPATH, App_logo)))
                logging.info('App Logo is present')
            except:
                logging.info('App Logo is present')
            try:
                wait.until(EC.presence_of_element_located((By.XPATH, New_mail_button))).click()
                time.sleep(1)
                login_user = wait.until(EC.presence_of_element_located((By.XPATH, Get_mailid_of_current_user))).text
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, To))).send_keys(login_user)
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, "//td[@role='menuitem']"))).click()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, To))).clear()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, To))).send_keys(utils.env["User1FirstName"])
                time.sleep(1)
                wait.until(EC.presence_of_element_located(
                    (By.XPATH, "//td[contains(normalize-space( ),"+utils.env['User1LastName']+")]/strong[contains(.,"+utils.env['User1FirstName']+")]"))).click()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, To))).clear()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, To))).send_keys(utils.env["User1LastName"])
                time.sleep(1)
                wait.until(EC.presence_of_element_located(
                    (By.XPATH, "//td[contains(normalize-space( ),"+utils.env['User1FirstName']+")]/strong[contains(.,"+utils.env['User1LastName']+")]"))).click()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Cc))).send_keys(login_user)
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, "//td[@role='menuitem']"))).click()
                wait.until(EC.presence_of_element_located((By.XPATH, Cc))).clear()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Cc))).send_keys(utils.env["User1FirstName"])
                time.sleep(1)
                wait.until(EC.presence_of_element_located(
                    (By.XPATH,
                     "//td[contains(normalize-space( ) ,"+utils.env['User1LastName']+")]/strong[contains(.,"+utils.env['User1FirstName']+")]"))).click()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Cc))).clear()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Cc))).send_keys(utils.env["User1LastName"])
                time.sleep(1)
                wait.until(EC.presence_of_element_located(
                    (By.XPATH,
                     "//td[contains(normalize-space( ) ,"+utils.env['User1FirstName']+")]/strong[contains(.,"+utils.env['User1LastName']+")]"))).click()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Bcc_label))).click()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Bcc))).send_keys(login_user)
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, "//td[@role='menuitem']"))).click()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Bcc))).clear()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Bcc))).send_keys(utils.env["User1FirstName"])
                time.sleep(1)
                wait.until(EC.presence_of_element_located(
                    (By.XPATH,
                     "//td[contains(normalize-space( ) ,"+utils.env['User1LastName']+")]/strong[contains(.,"+utils.env['User1FirstName']+")]"))).click()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Bcc))).clear()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Bcc))).send_keys(utils.env["User1LastName"])
                time.sleep(1)
                wait.until(EC.presence_of_element_located(
                    (By.XPATH,
                     "//td[contains(normalize-space( ) ,"+utils.env['User1FirstName']+")]/strong[contains(.,"+utils.env['User1LastName']+")]"))).click()
                time.sleep(1)

                wait.until(EC.presence_of_element_located((By.XPATH, Inbox))).click()
                logging.info('Compose email page user filtering got success')
            except:
                logging.info('Compose email page user filtering got fail')
                pass
            try:
                wait.until(EC.presence_of_element_located((By.XPATH, First_mail_in_inbox))).click()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Reply))).click()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Cc))).send_keys(login_user)
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, "//td[@role='menuitem']"))).click()
                wait.until(EC.presence_of_element_located((By.XPATH, Cc))).clear()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Cc))).send_keys(utils.env["User1FirstName"])
                time.sleep(1)
                wait.until(EC.presence_of_element_located(
                    (By.XPATH,
                     "//td[contains(normalize-space( ) ," + utils.env['User1LastName'] + ")]/strong[contains(.," +
                     utils.env['User1FirstName'] + ")]"))).click()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Cc))).clear()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Cc))).send_keys(utils.env["User1LastName"])
                time.sleep(1)
                wait.until(EC.presence_of_element_located(
                    (By.XPATH,
                     "//td[contains(normalize-space( ) ," + utils.env['User1FirstName'] + ")]/strong[contains(.," +
                     utils.env['User1LastName'] + ")]"))).click()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Bcc_label))).click()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Bcc))).send_keys(login_user)
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, "//td[@role='menuitem']"))).click()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Bcc))).clear()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Bcc))).send_keys(utils.env["User1FirstName"])
                time.sleep(1)
                wait.until(EC.presence_of_element_located(
                    (By.XPATH,
                     "//td[contains(normalize-space( ) ," + utils.env['User1LastName'] + ")]/strong[contains(.," +
                     utils.env['User1FirstName'] + ")]"))).click()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Bcc))).clear()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Bcc))).send_keys(utils.env["User1LastName"])
                time.sleep(1)
                wait.until(EC.presence_of_element_located(
                    (By.XPATH,
                     "//td[contains(normalize-space( ) ," + utils.env['User1FirstName'] + ")]/strong[contains(.," +
                     utils.env['User1LastName'] + ")]"))).click()
                time.sleep(1)

                wait.until(EC.presence_of_element_located((By.XPATH, Inbox))).click()
                logging.info('Reply email page user filtering got success')
            except:
                logging.info('Reply email page user filtering got fail')
                pass
            try:
                wait.until(EC.presence_of_element_located((By.XPATH, First_mail_in_inbox))).click()
                # time.sleep(1)
                # login_user = wait.until(EC.presence_of_element_located((By.XPATH, Get_mailid_of_current_user))).text
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Reply_All))).click()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Cc))).clear()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Cc))).send_keys(login_user)
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, "//td[@role='menuitem']"))).click()
                wait.until(EC.presence_of_element_located((By.XPATH, Cc))).clear()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Cc))).send_keys(utils.env["User1FirstName"])
                time.sleep(1)
                wait.until(EC.presence_of_element_located(
                    (By.XPATH,
                     "//td[contains(normalize-space( ) ," + utils.env['User1LastName'] + ")]/strong[contains(.," +
                     utils.env['User1FirstName'] + ")]"))).click()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Cc))).clear()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Cc))).send_keys(utils.env["User1LastName"])
                time.sleep(1)
                wait.until(EC.presence_of_element_located(
                    (By.XPATH,
                     "//td[contains(normalize-space( ) ," + utils.env['User1FirstName'] + ")]/strong[contains(.," +
                     utils.env['User1LastName'] + ")]"))).click()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Bcc_label))).click()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Bcc))).send_keys(login_user)
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, "//td[@role='menuitem']"))).click()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Bcc))).clear()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Bcc))).send_keys(utils.env["User1FirstName"])
                time.sleep(1)
                wait.until(EC.presence_of_element_located(
                    (By.XPATH,
                     "//td[contains(normalize-space( ) ," + utils.env['User1LastName'] + ")]/strong[contains(.," +
                     utils.env['User1FirstName'] + ")]"))).click()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Bcc))).clear()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Bcc))).send_keys(utils.env["User1LastName"])
                time.sleep(1)
                wait.until(EC.presence_of_element_located(
                    (By.XPATH,
                     "//td[contains(normalize-space( ) ," + utils.env['User1FirstName'] + ")]/strong[contains(.," +
                     utils.env['User1LastName'] + ")]"))).click()
                time.sleep(1)

                wait.until(EC.presence_of_element_located((By.XPATH, Inbox))).click()
                logging.info('Reply_All email page user filtering got success')
            except:
                logging.info('Reply_All email page user filtering got fail')
                pass
            try:
                wait.until(EC.presence_of_element_located((By.XPATH, First_mail_in_inbox))).click()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Forward))).click()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, To))).send_keys(login_user)
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, "//td[@role='menuitem']"))).click()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, To))).clear()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, To))).send_keys(utils.env["User1FirstName"])
                time.sleep(1)
                wait.until(EC.presence_of_element_located(
                    (By.XPATH,
                     "//td[contains(normalize-space( )," + utils.env['User1LastName'] + ")]/strong[contains(.," +
                     utils.env['User1FirstName'] + ")]"))).click()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, To))).clear()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, To))).send_keys(utils.env["User1LastName"])
                time.sleep(1)
                wait.until(EC.presence_of_element_located(
                    (By.XPATH,
                     "//td[contains(normalize-space( )," + utils.env['User1FirstName'] + ")]/strong[contains(.," +
                     utils.env['User1LastName'] + ")]"))).click()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Cc))).clear()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Cc))).send_keys(login_user)
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, "//td[@role='menuitem']"))).click()
                wait.until(EC.presence_of_element_located((By.XPATH, Cc))).clear()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Cc))).send_keys(utils.env["User1FirstName"])
                time.sleep(1)
                wait.until(EC.presence_of_element_located(
                    (By.XPATH,
                     "//td[contains(normalize-space( ) ," + utils.env['User1LastName'] + ")]/strong[contains(.," +
                     utils.env['User1FirstName'] + ")]"))).click()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Cc))).clear()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Cc))).send_keys(utils.env["User1LastName"])
                time.sleep(1)
                wait.until(EC.presence_of_element_located(
                    (By.XPATH,
                     "//td[contains(normalize-space( ) ," + utils.env['User1FirstName'] + ")]/strong[contains(.," +
                     utils.env['User1LastName'] + ")]"))).click()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Bcc_label))).click()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Bcc))).send_keys(login_user)
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, "//td[@role='menuitem']"))).click()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Bcc))).clear()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Bcc))).send_keys(utils.env["User1FirstName"])
                time.sleep(1)
                wait.until(EC.presence_of_element_located(
                    (By.XPATH,
                     "//td[contains(normalize-space( ) ," + utils.env['User1LastName'] + ")]/strong[contains(.," +
                     utils.env['User1FirstName'] + ")]"))).click()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Bcc))).clear()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, Bcc))).send_keys(utils.env["User1LastName"])
                time.sleep(1)
                wait.until(EC.presence_of_element_located(
                    (By.XPATH,
                     "//td[contains(normalize-space( ) ," + utils.env['User1FirstName'] + ")]/strong[contains(.," +
                     utils.env['User1LastName'] + ")]"))).click()
                time.sleep(1)

                wait.until(EC.presence_of_element_located((By.XPATH, Inbox))).click()
                logging.info('Forward email page user filtering got success')
                driver.close()
                window_before = driver.window_handles[0]
                driver.switch_to.window(window_before)
                wait.until(EC.element_to_be_clickable((By.XPATH, hp.home_button_xpath))).click()
                # driver.close()
            except:
                logging.info('Forward email page user filtering got fail')
                pass

        except:
            driver.close()
            window_before = driver.window_handles[0]
            driver.switch_to.window(window_before)
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.home_button_xpath))).click()
            # driver.close()
            pass




