import sys
from commonmethods.Login import Login
from utils import utils as utils
from selenium.webdriver.common.action_chains import ActionChains
import logging
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Web Elements for Message App --- Settings Page
MessageAppIcon = "//*[@id='appMessages_menu']"
HomeIcon = "//*[@id = 'appHome_menu']"
Mail_Link = "//a[contains(text(),'Mail')]"
Settings_Link = "//a[text()='Settings']"
Settings_Page = "//div[text()='Internal To My Messaging Community ']"
Delegate_Button = "//div[text()='Delegate']"
Cannot_Delegate_PopUp = "//div[contains(text(),'More than one delegate is not allowed')]"
Exist_DelegatedUser_Delete = "//tbody//div/input[@type='button' and @text='Delete']"
Deleted_PopUp_Msg = "//div[contains(text(),'Delegate deleted successfully')]"
Deleted_PopUp_Ok = "//div[text()='Are you sure want to delete delegate ?']/..//following::td//div[contains(text(),'Ok')]"
Ok_Button = "//div[text()='Ok']"
Delegate_InputField = "//div[contains(text(),'Delegate Email')]/../following-sibling::td/input[@type='text']"
Email_Id = "test@escrowdirect.gsihealth.net"
UserName = "esautomationtwo"
User_Dropdown_click = "//td[text()='_"+Email_Id+"']/strong[text()='"+UserName+"']"
Create_Delegate = "//button[contains(text(),'Create Delegate')]"
Create_Delegate_PopUP="//p[contains(text(),'Are you sure want to create a delegate ')]"
Created_PopUp_Msg = "//div[contains(text(),'Delegate created successfully')]"
Inbox_folder = "//div/div[@title='INBOX']"
Refresh_Button = "//td/div/a[contains(text(),'Refresh')]"
Delegate_Mail_Verify = "(//tr[contains(@class,'msgtable-unseen')]//td[contains(text(),'You have been given delegate permission')])[1]"
Back_Button = "//button[contains(text(),'Back')]"
Switch_To_Email_Account = "//div[contains(text(),'Switch To Email Account : ')]"
Delegation_DropDown = "//select[@class='gwt-ListBox']"
Direct_Address_One = "esautomationone_test@escrowdirect.gsihealth.net"
Direct_Address_Two = "esautomationtwo_test@escrowdirect.gsihealth.net"
Own_Direct_Address = "//div[contains(@class,'loginfo-label')]"
Switch_To_Email_Account_PopUpMsg1 = "//div[contains(text(),'You are already with this email account')]"
Switch_To_Email_Account_PopUpMsg2 = "//div[contains(text(),'You have switched to email account :' '"+Direct_Address_Two+"')]"
Banner_Delegation_Address = "//div[contains(text(),'You are acting as delegate for "+UserName+" : "+Direct_Address_Two+"')]"

# Web Elements for Message App --- LoginPage
home_button_xpath = "//*[@id = 'appHome_menu']"
logout_image= "//md-icon[@aria-label='logout']"
logout_button = "//div[text()='Yes']"
username_textbox = "//input[@name='UserID']"
password_textbox = "//input[@name='Password']"
login_button = "//button[@id='btnLogin']/span"
samsha_checkbox = "//label[contains(text(),'I have read and ')]"
samsha_button = "//div[text()='I Agree']"
logintoaccount_text = "//div[@class='title ng-binding ng-scope']"
gotit_button = "//div[contains(text(),'Got it')]"
login_logo = "//div[@class='title ng-binding']"



class Delegation_Funtionality():

    def __init__(self,driver,wait):
        self.driver = driver
        self.wait = wait

    def Delegation_Funtionality(self):
        try:
            driver = self.driver
            wait = self.wait

            try:
                wait.until(EC.element_to_be_clickable((By.XPATH, HomeIcon))).click()
                logging.info('Home Page is Navigated SuccessFully')
            except:
                Login(driver, wait).login_failure_handling()

            wait.until(EC.element_to_be_clickable((By.XPATH, MessageAppIcon))).click()
            window_after = driver.window_handles[1]
            driver.switch_to.window(window_after)
            driver.maximize_window()

            try:
                # Mail Page
                wait.until(EC.presence_of_element_located((By.XPATH, Mail_Link)))
                logging.info('Message App is Navigated SuccessFully')
                time.sleep(5)
                Direct_Address_One_Txt = wait.until(EC.presence_of_element_located((By.XPATH, Own_Direct_Address))).text
                print(Direct_Address_One_Txt)

                # Settings Page
                wait.until(EC.presence_of_element_located((By.XPATH, Settings_Link))).click()
                logging.info('Settings Page is Navigated SuccessFully')
                time.sleep(2)

                # Delegate Section
                wait.until(EC.presence_of_element_located((By.XPATH, Delegate_Button))).click()
                logging.info('Delegate Section is Navigated SuccessFully')
                time.sleep(2)

                try:
                    if(wait.until(EC.presence_of_element_located((By.XPATH,Exist_DelegatedUser_Delete)))):
                        wait.until(EC.presence_of_element_located((By.XPATH, Exist_DelegatedUser_Delete))).click()
                        time.sleep(2)
                        Del_Popup_txt = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='dialogMiddleCenterInner dialogContent']/table/tbody/tr/td/div"))).text
                        print(Del_Popup_txt)
                        wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Are you sure want to delete delegate ?')]//following::div[text()='Ok']"))).click()
                        logging.info("After clicking the delete Button, then Popup shoud be displayed as : "+Del_Popup_txt)
                        Del_msg_txt = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='dialogMiddleCenterInner dialogContent']/table/tbody/tr/td/div[contains(text(),'Delegate deleted successfully')]"))).text
                        print(Del_msg_txt)
                        logging.info("After clicking the delete_PopUp Ok Button, then Popup shoud be displayed as : "+Del_msg_txt)
                        time.sleep(2)
                        wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Delegate deleted successfully')]/..//following::td//div[contains(text(),'Ok')]"))).click()
                        time.sleep(3)
                except:
                    pass
                wait.until(EC.presence_of_element_located((By.XPATH, Delegate_InputField))).click()
                driver.find_element_by_xpath(Delegate_InputField).clear()
                driver.find_element_by_xpath(Delegate_InputField).send_keys(utils.env.UserMailID1)
                time.sleep(2)
                wait.until(EC.presence_of_element_located((By.XPATH, User_Dropdown_click))).click()
                time.sleep(2)
                wait.until(EC.presence_of_element_located((By.XPATH, Create_Delegate))).click()
                logging.info('Create a Delegate for the user : '+Direct_Address_Two)
                time.sleep(3)
                wait.until(EC.presence_of_element_located((By.XPATH, "//p[text()='Are you sure want to create a delegate ']/..//following::td//div[contains(text(),'Ok')]"))).click()
                logging.info("Delegation is Created Successfully")
                time.sleep(3)
                driver.close()
                window_before = driver.window_handles[0]
                driver.switch_to.window(window_before)

                # logout the Dashboard
                driver.find_element_by_xpath(logout_image).click()
                time.sleep(5)
                wait.until(EC.presence_of_element_located((By.XPATH, logout_button))).click()
                logging.info("Logged out the DashBoard")
                time.sleep(8)

                driver.find_element_by_xpath(username_textbox).clear()
                driver.find_element_by_xpath(username_textbox).send_keys(utils.env["USER_ID2"])
                driver.find_element_by_xpath(password_textbox).clear()
                driver.find_element_by_xpath(password_textbox).send_keys(utils.env["PASSWORD"])
                login = wait.until(EC.element_to_be_clickable((By.XPATH, login_button)))
                actions = ActionChains(driver)
                actions.move_to_element(login).click().perform()
                try:
                    driver.find_element_by_xpath(samsha_checkbox)
                    if "SAMHSA" in driver.page_source:
                        driver.find_element_by_xpath(samsha_checkbox).click()
                        driver.find_element_by_xpath(samsha_button).click()
                except:
                    pass
                try:
                    driver.find_element_by_xpath(gotit_button)
                    if "Got it" in driver.page_source:
                        driver.find_element_by_xpath(gotit_button).click()
                except:
                    pass
                try:
                    wait.until(EC.element_to_be_clickable((By.XPATH, home_button_xpath))).click()
                    logging.info('Login to the Dashboard SuccessFully')
                except:
                    logging.info('Login Failed!!!')

                # Navigate to message app again
                wait.until(EC.element_to_be_clickable((By.XPATH, MessageAppIcon))).click()
                window_after = driver.window_handles[1]
                driver.switch_to.window(window_after)
                driver.maximize_window()

                try:
                    # Mail Page
                    time.sleep(5)
                    wait.until(EC.presence_of_element_located((By.XPATH,Inbox_folder))).click()
                    logging.info('Message App is Navigated SuccessFully')
                    time.sleep(2)
                    wait.until(EC.presence_of_element_located((By.XPATH, Refresh_Button))).click()
                    time.sleep(5)
                    wait.until(EC.presence_of_element_located((By.XPATH, Delegate_Mail_Verify))).click()
                    time.sleep(5)
                    wait.until(EC.presence_of_element_located((By.XPATH, Back_Button))).click()
                    time.sleep(2)
                    Direct_Address_Two_txt = wait.until(EC.presence_of_element_located((By.XPATH, Own_Direct_Address))).text
                    print(Direct_Address_Two_txt)

                    try:
                        wait.until(EC.presence_of_element_located((By.XPATH, Switch_To_Email_Account))).click()
                        logging.info("Switch To Email Account : Dropdown is Displayed")
                        time.sleep(2)
                        wait.until(EC.presence_of_element_located((By.XPATH, Delegation_DropDown))).click()
                        wait.until(EC.presence_of_element_located((By.XPATH,"//select[@class='gwt-ListBox']/option[@value='"+Direct_Address_Two+"']"))).click()
                        time.sleep(3)
                        if "GSIHealth Message" in driver.page_source:
                            msg1 = driver.find_element_by_xpath(Switch_To_Email_Account_PopUpMsg1).text
                            print(msg1)
                            try:
                                logging.info("Navigate to Delegation Dropdown and click the Own EmailId then Popup should be displayed as :" +msg1 )
                                wait.until(EC.presence_of_element_located((By.XPATH, Ok_Button))).click()
                            except:
                                pass
                        time.sleep(3)
                        wait.until(EC.presence_of_element_located((By.XPATH, Switch_To_Email_Account))).click()
                        time.sleep(2)
                        wait.until(EC.presence_of_element_located((By.XPATH, Delegation_DropDown))).click()
                        wait.until(EC.presence_of_element_located((By.XPATH,"//select[@class='gwt-ListBox']/option[@value='" +Direct_Address_One+ "']"))).click()
                        time.sleep(3)
                        msg2 = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='dialogMiddleCenterInner dialogContent']/table/tbody/tr/td/div[@class='gwt-HTML']"))).text
                        print(msg2)
                        logging.info("Navigate to Delegation Dropdown and click the Delegated EmailId then Popup should be displayed as :" + msg2)
                        wait.until(EC.presence_of_element_located((By.XPATH, "//td[@class='dialogMiddleCenter']//div[text()='Ok']"))).click()

                        time.sleep(3)
                        Banner_txt = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='hupa-top-wrap']/table/tbody/tr/td/div[@class='GK40RFKDN1']"))).text
                        print(Banner_txt)
                        logging.info("The Banner Address should be displayed as :" +Banner_txt)
                        time.sleep(3)
                        driver.close()
                        window_before = driver.window_handles[0]
                        driver.switch_to.window(window_before)
                        time.sleep(3)
                        wait.until(EC.element_to_be_clickable((By.XPATH, HomeIcon))).click()

                    except:
                        logging.info("Switch To Email Account : Dropdown is Not Displayed")

                except:
                    driver.close()
                    window_before = driver.window_handles[0]
                    driver.switch_to.window(window_before)
                    logging.info('Message App is Down, So Again Navigated to Home page!!!')
                    wait.until(EC.element_to_be_clickable((By.XPATH, HomeIcon))).click()


            except:
                driver.close()
                window_before = driver.window_handles[0]
                driver.switch_to.window(window_before)
                logging.info('Message App is Down, So Again Navigated to Home page!!!')
                wait.until(EC.element_to_be_clickable((By.XPATH, HomeIcon))).click()

        except:
            driver.close()
            window_before = driver.window_handles[0]
            driver.switch_to.window(window_before)
            Login(driver, wait).login()
            sys.exit()
