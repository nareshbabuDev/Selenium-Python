import pytest
import logging
import allure
from utils import utils as utils
from testcases.SingleUserMailSendAndReceive import SingleUserMailSendAndReceive
from testcases.MailForwardingFunctionality import MailForwardingFunctionality
from testcases.ReplyToMailFunctionality import ReplyToMailFunctionality
from testcases.Cc_Bcc_Functionality import Cc_Bcc_Functionality
from testcases.IconVerificationAndTypeAheadSearch import IconVerificationAndTypeAheadSearch
from testcases.RootFolder_and_SubFolder_CreationandDelection import RootFolder_and_SubFolder_CreationandDelection
from testcases.Draft_Deletion_MarkRearUnread_Functionality import Draft_Deletion_MarkRearUnread_Functionality
from testcases.OutOfOffice_AutoReply_NewContactCreation import OutOfOffice_AutoReply_NewContactCreation
from testcases.DelegationFuntionality import Delegation_Funtionality

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

@pytest.mark.usefixtures("test_setup")
class TestDailyProd():

    @allure.title(utils.configdata['ENVIRONMENT'] + "SingleUserMailSendandReceive")
    def test_SingleUserMailSendAndReceive(self):
        driver = self.driver
        wait = self.wait
        SingleUserMailSendAndReceive(driver, wait).SingleUserMailSendAndReceive()

    @allure.title(utils.configdata['ENVIRONMENT'] + "MailForwardingFunctionality")
    def test_MailForwardingFunctionality(self):
        driver = self.driver
        wait = self.wait
        MailForwardingFunctionality(driver, wait).MailForwardingFunctionality()

    @allure.title(utils.configdata['ENVIRONMENT'] + "ReplyToMailFunctionality")
    def test_ReplyToMailFunctionality(self):
        driver = self.driver
        wait = self.wait
        ReplyToMailFunctionality(driver, wait).ReplyToMailFunctionality()

    @allure.title(utils.configdata['ENVIRONMENT']+"Cc_Bcc_Functionality")
    def test_Cc_Bcc_Functionality(self):
        driver = self.driver
        wait = self.wait
        Cc_Bcc_Functionality(driver, wait).Cc_Bcc_Functionality()

    @allure.title(utils.configdata['ENVIRONMENT'] + "IconVerificationAndTypeAheadSearch")
    def test_IconVerificationAndTypeAheadSearch(self):
        driver = self.driver
        wait = self.wait
        IconVerificationAndTypeAheadSearch(driver, wait).IconVerificationAndTypeAheadSearch()

    @allure.title(utils.configdata['ENVIRONMENT'] + "Draft_Deletion_MarkRearUnread_Functionality")
    def test_Draft_Deletion_MarkRearUnread_Functionality(self):
        driver = self.driver
        wait = self.wait
        Draft_Deletion_MarkRearUnread_Functionality(driver, wait).Draft_Deletion_MarkRearUnread_Functionality()

    @allure.title(utils.configdata['ENVIRONMENT'] + "RootFolder_and_SubFolder_CreationandDelection")
    def test_RootFolder_and_SubFolder_CreationandDelection(self):
        driver = self.driver
        wait = self.wait
        RootFolder_and_SubFolder_CreationandDelection(driver, wait).RootFolder_and_SubFolder_CreationandDelection()

    @allure.title(utils.configdata['ENVIRONMENT'] + "OutOfOffice_AutoReply_NewContactCreation")
    def test_OutOfOffice_AutoReply_NewContactCreation(self):
        driver = self.driver
        wait = self.wait
        OutOfOffice_AutoReply_NewContactCreation(driver, wait).OutOfOffice_AutoReply_NewContactCreation()

    @allure.title(utils.configdata['ENVIRONMENT'] + "Delegation_Funtionality")
    def test_Delegation_Functionality(self):
        driver = self.driver
        wait = self.wait
        Delegation_Funtionality(driver, wait).Delegation_Funtionality()










