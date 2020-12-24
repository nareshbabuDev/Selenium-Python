import sys
from commonmethods.Login import Login
import logging
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import date
import datetime
from dateutil.relativedelta import relativedelta

# Web Elements for Message App --- Settings Page
MessageAppIcon = "//*[@id='appMessages_menu']"
HomeIcon = "//*[@id = 'appHome_menu']"
Mail_Link = "//a[contains(text(),'Mail')]"
Settings_Link = "//a[text()='Settings']"
Settings_Page = "//div[text()='Internal To My Messaging Community ']"
FromDate_InputField = "//tr/td/div[text()='Period']//following::td[5]/input[@type='text']"
ToDate_InputField = "//tr/td/div[text()='Period']//following::td[7]/input[@type='text']"
From_Date = "//td[@class='datePickerDay  datePickerDayIsToday  ']"
From_Date_GetText = "(//td/input[@class='gwt-DateBox'])[1]"
To_Date = "(//td[@class='datePickerDay  datePickerDayIsToday  ']//following::td[contains(@class,'datePickerDay datePickerDayIsWeekend')])[1]"
OutOfOffice_CheckBox = "//label[text()='Out Of Office']/../input[@type='checkbox']"
Save_Button = "//button[text()='Save']"
Ok_Button = "//div[text()='Ok']"
Reset_Button = "//button[text()='Reset']"
AutoReply_PopUp = "//div[text()='Your out-of-office setting is on']"

# Web Elements for Message App --- Contacts Page
Contacts_Link = "//a[text()='Contacts']"
New_Button = "//button[text()='New']"
First_Name_Field = "(//div[contains(text(),'First Name')]//following::input[@class='gwt-TextBox'])[1]"
First_Name = "Gsi"
Last_Name_Field = "(//div[contains(text(),'Last Name')]//following::input[@class='gwt-TextBox'])[1]"
Last_Name = "Power"
Email_Id_Field = "(//div[contains(text(),'E-Mail')]//following::input[@class='gwt-TextBox'])[1]"
Email_Id = "gsi.power@gsihealth.com"
Created_PopUp = "//div[contains(@class,'dialogContent')]//div[contains(text(),'Saved Successfully')]"
Created_Popup_Ok = "//div[contains(@class,'dialogContent')]//div[contains(text(),'Saved Successfully')]//following::div[contains(@class,'ButtonContent')]"
Contact_MailId_Verify = "//div[text()='"+Email_Id+"']"
Created_Contact_SearchClick = "//td[text()='_"+Last_Name+"']/strong[text()='"+First_Name+"']"
Delete_CheckBox = "//div[text()='"+Email_Id+"']//preceding::input[@type='checkbox']"
Delete_Button = "//button[contains(text(),'Delete')]"
Contact_Delete_Ok = "//div[contains(text(),'delete the Contact')]//following::div[text()='Ok']"
Contact_Search_Field = "//td/input[@class='gwt-SuggestBox hupa-search-box']"
Search_Button = "//button[contains(text(),'Search')]"
# Contact_NotFound = "//div[contains(text(),'Contact not found')]//following::div[text()='Ok']"



class OutOfOffice_AutoReply_NewContactCreation():

    def __init__(self,driver,wait):
        self.driver =  driver
        self.wait = wait

    def OutOfOffice_AutoReply_NewContactCreation(self):
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

                #PopUP OkButton
                try:
                    driver.find_element_by_xpath(AutoReply_PopUp)
                    logging.info('Your out-of-office setting is on')
                    if "GSIHealth Message" in driver.page_source:
                        driver.find_element_by_xpath(Ok_Button).click()
                        # Settings Page
                        wait.until(EC.presence_of_element_located((By.XPATH, Settings_Link))).click()
                        logging.info('Settings Page is Navigated SuccessFully')
                        time.sleep(2)
                        #Reset Button
                        wait.until(EC.presence_of_element_located((By.XPATH, Reset_Button))).click()
                        wait.until(EC.presence_of_element_located((By.XPATH, Save_Button))).click()
                        time.sleep(2)
                        wait.until(EC.presence_of_element_located((By.XPATH, Ok_Button))).click()
                        logging.info('Reset the Out-of-office setting SuccessFully')
                except:
                    # Settings Page
                    wait.until(EC.presence_of_element_located((By.XPATH, Settings_Link))).click()
                    logging.info('Settings Page is Navigated SuccessFully')
                    time.sleep(2)


                Start_Date = date.today()
                print(Start_Date)
                From_Date = Start_Date.strftime('%m/%d/%Y')
                print(From_Date)
                End_Date = datetime.datetime.today() + relativedelta(days=+4)
                print(End_Date)
                To_Date = End_Date.strftime('%m/%d/%Y')
                print(To_Date)

                #  Set From date and To date for AutoReply
                logging.info('To Set the Out Of Office-Setting Mode On')
                wait.until(EC.presence_of_element_located((By.XPATH, FromDate_InputField))).click()
                driver.find_element_by_xpath(FromDate_InputField).clear()
                time.sleep(3)
                driver.find_element_by_xpath(FromDate_InputField).send_keys(From_Date)
                time.sleep(2)

                wait.until(EC.presence_of_element_located((By.XPATH, ToDate_InputField))).click()
                driver.find_element_by_xpath(ToDate_InputField).clear()
                time.sleep(3)
                driver.find_element_by_xpath(ToDate_InputField).send_keys(To_Date)
                time.sleep(2)

                # Click the OutOfOffice checkbox and Save it
                wait.until(EC.presence_of_element_located((By.XPATH, OutOfOffice_CheckBox))).click()
                time.sleep(2)
                wait.until(EC.presence_of_element_located((By.XPATH, Save_Button))).click()
                time.sleep(2)

                # Verify Out Of Office-Auto Reply PopUp Ok Button and logout
                try:
                  wait.until(EC.presence_of_element_located((By.XPATH, Ok_Button))).click()
                  logging.info("OutOfOffice-AutoReply OkPopUp is displayed and Out Of Office-Setting is Saved Successfully!!!")
                except:
                  logging.info("OutOfOffice-AutoReply OkPopUp is Not displayed and Out Of Office- Setting is Not Saved ")
                  sys.exit()
                driver.close()
                window_before = driver.window_handles[0]
                driver.switch_to.window(window_before)

                # Navigate to message app again
                time.sleep(3)
                wait.until(EC.element_to_be_clickable((By.XPATH, MessageAppIcon))).click()
                window_after = driver.window_handles[1]
                driver.switch_to.window(window_after)
                driver.maximize_window()

                try:
                    # Mail Page
                    wait.until(EC.presence_of_element_located((By.XPATH, Mail_Link)))
                    logging.info('Message App is Navigated SuccessFully')
                    time.sleep(5)

                    # PopUP OkButton
                    try:
                        driver.find_element_by_xpath(AutoReply_PopUp)
                        logging.info('Your out-of-office setting is on')
                        if "GSIHealth Message" in driver.page_source:
                            driver.find_element_by_xpath(Ok_Button).click()

                            # Settings Page
                            wait.until(EC.presence_of_element_located((By.XPATH, Settings_Link))).click()
                            logging.info('Settings Page is Navigated SuccessFully')
                            time.sleep(2)

                            # Reset the Out Of Office-Setting and logout
                            wait.until(EC.presence_of_element_located((By.XPATH, Reset_Button))).click()
                            wait.until(EC.presence_of_element_located((By.XPATH, Save_Button))).click()
                            time.sleep(2)
                            if "GSIHealth Message" in driver.page_source:
                                driver.find_element_by_xpath(Ok_Button)
                                try:
                                    wait.until(EC.presence_of_element_located((By.XPATH, Ok_Button))).click()
                                    logging.info("Reset the Out Of Office-Setting is Saved Successfully!!!")
                                except:
                                    logging.info("Reset the Out Of Office- Setting is Not Saved ")

                    except:
                        pass
                    try:
                        # Contacts Page
                        time.sleep(3)
                        wait.until(EC.presence_of_element_located((By.XPATH, Contacts_Link))).click()
                        logging.info('Contacts Page is Navigated SuccessFully')
                        time.sleep(3)

                        # Create a New contact
                        wait.until(EC.presence_of_element_located((By.XPATH, New_Button))).click()
                        logging.info("Create a New contact")
                        time.sleep(2)

                        # First Name
                        wait.until(EC.presence_of_element_located((By.XPATH, First_Name_Field))).click()
                        driver.find_element_by_xpath(First_Name_Field).clear()
                        driver.find_element_by_xpath(First_Name_Field).send_keys(First_Name)
                        time.sleep(2)

                        # Second Name
                        wait.until(EC.presence_of_element_located((By.XPATH, Last_Name_Field))).click()
                        driver.find_element_by_xpath(Last_Name_Field).clear()
                        driver.find_element_by_xpath(Last_Name_Field).send_keys(Last_Name)
                        time.sleep(2)

                        # Email Id
                        wait.until(EC.presence_of_element_located((By.XPATH, Email_Id_Field))).click()
                        driver.find_element_by_xpath(Email_Id_Field).clear()
                        driver.find_element_by_xpath(Email_Id_Field).send_keys(Email_Id)
                        time.sleep(2)

                        # Save It and verify Created Contact Popup
                        wait.until(EC.presence_of_element_located((By.XPATH, Save_Button))).click()
                        time.sleep(2)
                        wait.until(EC.presence_of_element_located((By.XPATH, Created_PopUp)))
                        if "GSIHealth Message" in driver.page_source:
                            driver.find_element_by_xpath(Created_Popup_Ok)
                            try:
                                wait.until(EC.presence_of_element_located((By.XPATH, Created_Popup_Ok))).click()
                                logging.info("Create Contact OkPopUp is displayed and New Contact is Created Successfully")
                            except:
                                logging.info("Create Contact OkPopUp is Not displayed and New Contact is Not Created ")

                        # Search the Created Contact and verify
                        time.sleep(2)
                        wait.until(EC.presence_of_element_located((By.XPATH, Contact_Search_Field))).click()
                        driver.find_element_by_xpath(Contact_Search_Field).clear()
                        driver.find_element_by_xpath(Contact_Search_Field).send_keys(First_Name)
                        time.sleep(2)
                        wait.until(EC.presence_of_element_located((By.XPATH, Created_Contact_SearchClick))).click()
                        wait.until(EC.presence_of_element_located((By.XPATH, Search_Button))).click()
                        time.sleep(3)
                        wait.until(EC.presence_of_element_located((By.XPATH, Contact_MailId_Verify)))

                        # Delete the Created Contact
                        wait.until(EC.presence_of_element_located((By.XPATH, Contact_Search_Field))).click()
                        driver.find_element_by_xpath(Contact_Search_Field).clear()
                        wait.until(EC.presence_of_element_located((By.XPATH, Search_Button))).click()
                        time.sleep(4)
                        driver.find_element_by_xpath(Delete_CheckBox)
                        wait.until(EC.presence_of_element_located((By.XPATH, Delete_CheckBox))).click()
                        time.sleep(2)
                        wait.until(EC.presence_of_element_located((By.XPATH, Delete_Button))).click()
                        time.sleep(2)

                        if "GSIHealth Message" in driver.page_source:
                            driver.find_element_by_xpath(Contact_Delete_Ok)
                            try:
                                wait.until(EC.presence_of_element_located((By.XPATH, Contact_Delete_Ok))).click()
                                logging.info("Delete Contact OkPopUp is displayed and Contact is Deleted Successfully")
                            except:
                                logging.info("Delete Contact OkPopUp is Not displayed and Contact is Not Deleted ")

                        # Search the Deleted Contact and verify
                        wait.until(EC.presence_of_element_located((By.XPATH, Contact_Search_Field))).click()
                        driver.find_element_by_xpath(Contact_Search_Field).clear()
                        wait.until(EC.presence_of_element_located((By.XPATH, Search_Button))).click()
                        time.sleep(3)
                        # sys.exit()
                        driver.close()
                        window_before = driver.window_handles[0]
                        driver.switch_to.window(window_before)

                    except:
                            pass
                except:
                    driver.close()
                    window_before = driver.window_handles[0]
                    driver.switch_to.window(window_before)
                    logging.info('Message App is Down, So Again Navigated to Home page!!!')
                    wait.until(EC.element_to_be_clickable((By.XPATH, HomeIcon))).click()


                try:
                    wait.until(EC.element_to_be_clickable((By.XPATH, HomeIcon))).click()
                except:
                    logging.info("Message App Not Closed!!!")

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
            Login(driver,wait).login()
