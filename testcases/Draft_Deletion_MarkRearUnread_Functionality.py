import sys
from commonmethods import Login
import logging
import time
from utils import utils as utils
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from collections import MutableMapping
from collections import Mapping

# test data
home_button_xpath="//*[@id = 'appHome_menu']"
msgicon="//*[@id='appMessages_menu']"
inboxbtn="//div[@title='INBOX']"
new_mail_button_xpath ="//button[text()='New']"
loginfo_xpath ="//div[contains(@class,'loginfo')]/../..//following-sibling::tr/td/div"
to_textarea_xpath="//div[contains(text(),'To')]//ancestor::td[@class='label']//following-sibling::td/textarea"
subject_input_xpath ="//div[contains(text(),'Subject')]/..//following-sibling::td/input"
save_as_draft="//button[contains(text(),'Save As Draft')]"
refreshbtn="//td/div/a[contains(text(),'Refresh')]"
drafticon="//div[contains(@title,'Drafts')]"
logout="//div[contains(@class,'Hyperlink')]//a[text()='Logout']"
snewmail="//button[contains(text(),'New')]"
drafticoncounts="//div[contains(@title,'Drafts')]"
delete="//button[text()='Delete']"
markasread="//button[text()='Mark as Read']"
markasunread="//button[text()='Mark as Unread']"
send_btn="//button[contains(text(),'Send')]"
trash="//div[@title='Trash']"
sentbtn="//div[@title='Sent']"
trashokbtn="//div[@class='cbg-ButtonContent'][text()='Ok']"

class Draft_Deletion_MarkRearUnread_Functionality():

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def Draft_Deletion_MarkRearUnread_Functionality(self):
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
                wait.until(EC.presence_of_element_located((By.XPATH, new_mail_button_xpath))).click()
                logging.info('Message App Page Navigated SuccessFully')
                login_user = wait.until(EC.presence_of_element_located((By.XPATH, loginfo_xpath))).text
                time.sleep(2)
                wait.until(EC.presence_of_element_located((By.XPATH, to_textarea_xpath))).send_keys(login_user)
                # Send random text in Subject
                mailsubject = utils.mailsubject
                wait.until(EC.presence_of_element_located((By.XPATH, subject_input_xpath))).send_keys(mailsubject)
                #save as draft
                try:
                    wait.until(EC.presence_of_element_located((By.XPATH, save_as_draft))).click()
                    logging.info('Save as draft icon clicked')
                    time.sleep(3)
                except:
                      logging.info('Save as draft icon not available')
                try:
                    wait.until(EC.presence_of_element_located((By.XPATH, refreshbtn))).click()
                    time.sleep(3)
                    wait.until(EC.presence_of_element_located((By.XPATH, drafticon))).click()
                    time.sleep(3)
                    wait.until(EC.presence_of_element_located((By.XPATH, refreshbtn))).click()
                    time.sleep(3)
                    sub=wait.until(EC.presence_of_element_located((By.XPATH, "// tr[contains( @class ,'msgtable-unseen')] // following-sibling::td[contains(text(), '"+mailsubject+"')]"))).text
                    # print(sub)
                    time.sleep(3)
                    if sub==mailsubject:
                      logging.info("Message saved to draft")
                except:
                      logging.info("Not saved")

                #draft count verification
                try:
                    time.sleep(5)
                    count=wait.until(EC.presence_of_element_located((By.XPATH, drafticoncounts))).text
                    logging.info("count-"+count)
                    time.sleep(3)
                    logging.info("Compose a Second Mail")
                    time.sleep(3)
                    wait.until(EC.presence_of_element_located((By.XPATH, new_mail_button_xpath))).click()
                    logging.info('Message App Page Navigated SuccessFully')
                    login_user = wait.until(EC.presence_of_element_located((By.XPATH, loginfo_xpath))).text
                    time.sleep(2)
                    wait.until(EC.presence_of_element_located((By.XPATH, to_textarea_xpath))).send_keys(login_user)
                    # Send random text in Subject
                    mailsubject = utils.mailsubject
                    wait.until(EC.presence_of_element_located((By.XPATH, subject_input_xpath))).send_keys(mailsubject)
                    time.sleep(3)
                    wait.until(EC.presence_of_element_located((By.XPATH, logout))).click()
                    logging.info("LogOut from MessageApp!!!")
                    time.sleep(15)
                    # driver.close()
                    window_before = driver.window_handles[-1]
                    driver.switch_to.window(window_before)
                    driver.switch_to.default_content()
                except:
                    logging.info("Failed")

                try:
                    time.sleep(15)
                    wait.until(EC.presence_of_element_located((By.XPATH, home_button_xpath)))
                    logging.info('Home page Navigated SuccessFully')
                    time.sleep(5)
                except:
                    Login(driver, wait).login_failure_handling()

                try:
                    wait.until(EC.element_to_be_clickable((By.XPATH, msgicon))).click()
                    time.sleep(5)
                    window_after = driver.window_handles[1]
                    driver.switch_to.window(window_after)

                    wait.until(EC.presence_of_element_located((By.XPATH, refreshbtn))).click()
                    time.sleep(3)
                    wait.until(EC.presence_of_element_located((By.XPATH, drafticon))).click()
                    time.sleep(3)
                    wait.until(EC.presence_of_element_located((By.XPATH, refreshbtn))).click()
                    time.sleep(3)
                    count2 = wait.until(EC.presence_of_element_located((By.XPATH, drafticoncounts))).text
                    logging.info(count2)
                    if count2>count:
                        logging.info("Draft Message count increased")
                    else:
                        logging.info("Draft Message count not increased")

                # mark as read functionality
                    time.sleep(3)

                    wait.until(EC.presence_of_element_located((By.XPATH, "(//tr[contains(@class,'msgtable-unseen')]//following-sibling::td[contains(text(),"+mailsubject+")]//preceding::input[@type='checkbox'])[1]"))).click()
                    wait.until(EC.presence_of_element_located((By.XPATH, markasread))).click()
                    logging.info("msg has been read")

                    # msg unread functionality
                    time.sleep(3)
                    # logging.info("(//tr[contains(@class,'msgtable-unseen')]//following-sibling::td[contains(text()," + mailsubject + ")]//preceding::input[@type='checkbox'])[1]")
                    wait.until(EC.presence_of_element_located((By.XPATH,"(//tr[contains(@class,'msgtable-unseen')]//following-sibling::td[contains(text()," + mailsubject + ")]//preceding::input[@type='checkbox'])[1]"))).click()
                    wait.until(EC.presence_of_element_located((By.XPATH, markasunread))).click()
                    logging.info("msg has been unread")

                # delete msg from draft
                    time.sleep(3)

                    wait.until(EC.presence_of_element_located((By.XPATH,"(//tr[contains(@class,'msgtable-unseen')]//following-sibling::td[contains(text()," + mailsubject + ")]//preceding::input[@type='checkbox'])[1]"))).click()
                    wait.until(EC.presence_of_element_located((By.XPATH, delete))).click()
                    logging.info("msg has been deleted from draft")

                #logout of the window
                    # window_before = driver.window_handles[-1]
                    # driver.switch_to.window(window_before)
                    # driver.switch_to.default_content()


                    #checking deleted msg(draft) in trash
                    time.sleep(3)
                    wait.until(EC.presence_of_element_located((By.XPATH, trash))).click()
                    time.sleep(3)
                    wait.until(EC.presence_of_element_located((By.XPATH, refreshbtn))).click()
                    dd=wait.until(EC.presence_of_element_located((By.XPATH,"// tr[contains( @class ,'msgtable-unseen')] // following-sibling::td[contains(text(), '" + mailsubject + "')]"))).text
                    if dd==mailsubject:
                        logging.info("Msg deleted from draft has been moved to trash")
                    else:
                        logging.info("Msg deleted from draft has not been moved to trash")

                #inbox
                    time.sleep(3)
                    wait.until(EC.presence_of_element_located((By.XPATH,inboxbtn))).click()
                    time.sleep(3)
                    wait.until(EC.presence_of_element_located((By.XPATH, new_mail_button_xpath))).click()
                    login_user = wait.until(EC.presence_of_element_located((By.XPATH, loginfo_xpath))).text
                    time.sleep(2)
                    wait.until(EC.presence_of_element_located((By.XPATH, to_textarea_xpath))).send_keys(login_user)
                    # Send random text in Subject
                    newmailsubject = utils.mailsubject
                    wait.until(EC.presence_of_element_located((By.XPATH, subject_input_xpath))).send_keys(newmailsubject)
                    wait.until(EC.presence_of_element_located((By.XPATH, send_btn))).click()
                    wait.until(EC.presence_of_element_located((By.XPATH, inboxbtn))).click()
                    time.sleep(3)
                    wait.until(EC.presence_of_element_located((By.XPATH, refreshbtn))).click()
                    newmailsub = wait.until(EC.presence_of_element_located((By.XPATH,"// tr[contains( @class ,'msgtable-unseen')] // following-sibling::td[contains(text(), '" + newmailsubject + "')]"))).text
                    # print(newmailsub)
                    # logging.info(newmailsub)
                    # logging.info(newmailsubject)
                    time.sleep(3)
                    if newmailsub == newmailsubject:
                        logging.info("new msg has been received")
                    else:
                        logging.info("new msg not received")

                    #inbox delete
                    wait.until(EC.presence_of_element_located((By.XPATH,"(//tr[contains(@class,'msgtable-unseen')]//following-sibling::td[contains(text()," + newmailsubject + ")]//preceding::input[@type='checkbox'])[1]"))).click()
                    time.sleep(3)
                    wait.until(EC.presence_of_element_located((By.XPATH, delete))).click()
                    logging.info("msg has been deleted from inbox")

                    #verifying in trash
                    time.sleep(3)
                    wait.until(EC.presence_of_element_located((By.XPATH, trash))).click()
                    time.sleep(3)
                    wait.until(EC.presence_of_element_located((By.XPATH, refreshbtn))).click()
                    inbox = wait.until(EC.presence_of_element_located((By.XPATH,"// tr[contains( @class ,'msgtable-unseen')] // following-sibling::td[contains(text(), '" + newmailsubject + "')]"))).text
                    if inbox == newmailsubject:
                        logging.info("inbox msg moved to trash")
                    else:
                        logging.info("inbox msg not moved to trash")

                    #sent msg delete
                    time.sleep(3)
                    wait.until(EC.presence_of_element_located((By.XPATH, sentbtn))).click()
                    # wait.until(EC.presence_of_element_located((By.XPATH,"(//tr[contains(@class,'msgtable-unseen')]//following-sibling::td[contains(text()," + newmailsubject + ")]//preceding::input[@type='checkbox'])[1]"))).click()
                    time.sleep(3)
                    wait.until(EC.presence_of_element_located((By.XPATH,"//td[@class='GK40RFKDD3B']//tr[2]//td[1]//input[1]"))).click()
                    time.sleep(3)
                    wait.until(EC.presence_of_element_located((By.XPATH, delete))).click()
                    logging.info(" sent msg has been deleted  ")

                    # verifying in trash
                    time.sleep(3)
                    wait.until(EC.presence_of_element_located((By.XPATH, trash))).click()
                    time.sleep(3)
                    wait.until(EC.presence_of_element_located((By.XPATH, refreshbtn))).click()
                    sentmsg = wait.until(EC.presence_of_element_located((By.XPATH,"// tr[contains( @class ,'msgtable-unseen')] // following-sibling::td[contains(text(), '" + newmailsubject + "')]"))).text
                    time.sleep(3)
                    if sentmsg == newmailsubject:
                        logging.info("sent msg moved to trash")
                    else:
                        logging.info("sent msg not moved to trash")


                    #delete msg from trash
                    try:
                        time.sleep(3)
                        wait.until(EC.presence_of_element_located((By.XPATH, trash))).click()
                        time.sleep(3)
                        wait.until(EC.presence_of_element_located((By.XPATH, refreshbtn))).click()
                        time.sleep(3)
                        wait.until(EC.presence_of_element_located((By.XPATH, "//td[ @class ='GK40RFKDD3B']//tr[2]//td[1]// input[1]"))).click()
                        time.sleep(6)
                        wait.until(EC.presence_of_element_located((By.XPATH, delete))).click()
                        time.sleep(5)
                        # wait.until(EC.presence_of_element_located((By.XPATH, refreshbtn))).click()
                        time.sleep(3)
                        wait.until(EC.presence_of_element_located((By.XPATH, trashokbtn))).click()
                        time.sleep(3)
                        logging.info(" trash msg has been deleted ")
                        driver.close()
                        window_before = driver.window_handles[0]
                        driver.switch_to.window(window_before)
                        wait.until(EC.element_to_be_clickable((By.XPATH, home_button_xpath))).click()
                        wait.until(EC.element_to_be_clickable((By.XPATH, home_button_xpath))).click()


                    except:
                        logging.info("Failed in trash")

                except:
                    logging.info("Failed")
            except:
                driver.close()
                window_before = driver.window_handles[0]
                driver.switch_to.window(window_before)
                logging.info('Message App is Down, So Again Navigated to Home page!!!')
                wait.until(EC.element_to_be_clickable((By.XPATH, home_button_xpath))).click()
                sys.exit()
        except:
            driver.close()
            window_before = driver.window_handles[0]
            driver.switch_to.window(window_before)

            sys.exit()
            assert 0