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
# select_1st_mail    =  "//td[contains(text(),'"+login_user+"')]//following::td[text()='"+mailSubject+"']"
Inbox              =   "//div[@title='INBOX']"
sent               =   "//div[@title='Sent']"
Refresh            =   "//a[text()='Refresh']"
Bcc_label = "//a[@class='gwt-Anchor' and text()='Bcc:']"
# Message App _ Send a email and verify the sent email is successfully received
class Cc_Bcc_Functionality():

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def Cc_Bcc_Functionality(self):
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
                wait.until(EC.presence_of_element_located((By.XPATH,To ))).send_keys(utils.env["UserMailID1"])
                wait.until(EC.presence_of_element_located(
                    (By.XPATH, "//strong[text() = 'gsi.power_gsihealth@escrowdirect.gsihealth.net']"))).click()
                wait.until(EC.presence_of_element_located((By.XPATH, Cc))).send_keys(utils.env["UserMailID2"])
                wait.until(EC.presence_of_element_located(
                    (By.XPATH, "//strong[text() = 'esautomationone_test@escrowdirect.gsihealth.net']"))).click()
                wait.until(EC.presence_of_element_located((By.XPATH, Bcc_label))).click()
                wait.until(EC.presence_of_element_located((By.XPATH, Bcc))).send_keys(utils.env["UserMailID3"])
                wait.until(EC.presence_of_element_located(
                    (By.XPATH, "//strong[text() = 'esautomationtwo_test@escrowdirect.gsihealth.net']"))).click()
                # Send random text in Subject
                mailsubject = utils.mailsubject
                wait.until(EC.presence_of_element_located((By.XPATH, Subject))).send_keys(mailsubject)
                wait.until(EC.presence_of_element_located((By.XPATH, Send))).click()
                logging.info('New Mail is sent with To,Cc,Bcc')
                wait.until(EC.presence_of_element_located((By.XPATH, Refresh))).click()
                try:
                    wait.until(EC.presence_of_element_located((By.XPATH, "//tr[contains(@class,'unseen')]/td[contains(text(),'"+login_user+"')]//following-sibling::td[contains(text(),'"+mailsubject+"')]"))).click()
                    logging.info('New Message is received to To: User')
                    driver.close()
                    window_before = driver.window_handles[0]
                    driver.switch_to.window(window_before)
                    wait.until(EC.presence_of_element_located((By.XPATH, "//md-icon[@aria-label='logout']"))).click()
                    time.sleep(5)
                    wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Yes']"))).click()
                    time.sleep(5)
                except:
                  logging.info('New Message is not received to To: User')
                  driver.close()
                  window_before = driver.window_handles[0]
                  driver.switch_to.window(window_before)
                  wait.until(EC.presence_of_element_located((By.XPATH, "//md-icon[@aria-label='logout']"))).click()
                  time.sleep(5)
                  wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Yes']"))).click()
                  time.sleep(5)

            except:
                logging.info('new mail is not sent')

            try:
                time.sleep(5)
                wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='UserID']"))).click()
                time.sleep(3)
                wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='UserID']"))).send_keys(utils.env["User_ID2"])
                time.sleep(3)
                wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='Password']"))).send_keys(utils.env["PASSWORD"])
                time.sleep(3)
                wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='Password']"))).click()
                login_Button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btnLogin']/span")))
                actions = ActionChains(driver)
                actions.move_to_element(login_Button).click().perform()
                logging.info("Logged into DashBoard")
                try:
                    driver.find_element_by_xpath(lp.samsha_checkbox_xpath).click()
                    driver.find_element_by_xpath(lp.samsha_button_xpath).click()
                except:
                    pass
                try:
                    driver.find_element_by_xpath(lp.gotit_button_xpath).click()
                except:
                    pass
                try:
                    wait.until(EC.element_to_be_clickable((By.XPATH, message_app))).click()
                    window_after = driver.window_handles[1]
                    driver.switch_to.window(window_after)
                    try:
                        wait.until(EC.presence_of_element_located((By.XPATH, Inbox))).click()
                        # login_user = wait.until(EC.presence_of_element_located((By.XPATH, Get_mailid_of_current_user))).text
                        time.sleep(2)
                        wait.until(EC.presence_of_element_located((By.XPATH,
                                                                   "//tr[contains(@class,'unseen')]/td[contains(text(),'" + utils.env["UserMailID1"] + "')]//following-sibling::td[contains(text(),'" + mailsubject + "')]"))).click()
                        logging.info('New Message is received to Cc: User')
                        driver.close()
                        window_before = driver.window_handles[0]
                        driver.switch_to.window(window_before)
                        wait.until(EC.presence_of_element_located((By.XPATH, "//md-icon[@aria-label='logout']"))).click()
                        time.sleep(5)
                        wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Yes']"))).click()
                        time.sleep(5)
                        # driver.close()
                    except:
                        logging.info('New Message is not received to Cc: User')
                        driver.close()
                        window_before = driver.window_handles[0]
                        driver.switch_to.window(window_before)
                        wait.until(
                            EC.presence_of_element_located((By.XPATH, "//md-icon[@aria-label='logout']"))).click()
                        time.sleep(5)
                        wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Yes']"))).click()
                        time.sleep(5)
                        driver.close()
                except:
                    pass
            except:
                pass
            try:
                time.sleep(5)
                wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='UserID']"))).click()
                time.sleep(3)
                wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='UserID']"))).send_keys(utils.env["User_ID3"])
                time.sleep(3)
                wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='Password']"))).send_keys(utils.env["PASSWORD"])
                time.sleep(3)
                wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='Password']"))).click()
                login_Button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btnLogin']/span")))
                actions = ActionChains(driver)
                actions.move_to_element(login_Button).click().perform()
                logging.info("Logged into DashBoard")
                try:
                    driver.find_element_by_xpath(lp.samsha_checkbox_xpath).click()
                    driver.find_element_by_xpath(lp.samsha_button_xpath).click()
                except:
                    pass
                try:
                    driver.find_element_by_xpath(lp.gotit_button_xpath).click()
                except:
                    pass
                try:
                    wait.until(EC.element_to_be_clickable((By.XPATH, message_app))).click()
                    window_after = driver.window_handles[1]
                    driver.switch_to.window(window_after)
                    try:
                        wait.until(EC.presence_of_element_located((By.XPATH, Inbox))).click()
                        login_user = wait.until(EC.presence_of_element_located((By.XPATH, Get_mailid_of_current_user))).text
                        time.sleep(2)
                        wait.until(EC.presence_of_element_located((By.XPATH,
                                                                   "//tr[contains(@class,'unseen')]/td[contains(text(),'"+ utils.env["UserMailID1"] + "')]//following-sibling::td[contains(text(),'" + mailsubject + "')]"))).click()
                        logging.info('New Message is received to Bcc: User')
                        driver.close()
                        window_before = driver.window_handles[0]
                        driver.switch_to.window(window_before)
                        wait.until(EC.element_to_be_clickable((By.XPATH, hp.home_button_xpath))).click()
                        # wait.until(EC.presence_of_element_located((By.XPATH, "//md-icon[@aria-label='logout']"))).click()
                        # time.sleep(5)
                        # wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Yes']"))).click()
                        time.sleep(3)
                        # driver.close()
                    except:
                        logging.info('New Message is not received to Bcc: User')

                except:
                    pass

            except:
              pass

        except:
            logging.info('Message App is Down')
            driver.close()
            window_before = driver.window_handles[0]
            driver.switch_to.window(window_before)
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.home_button_xpath))).click()
            # driver.close()