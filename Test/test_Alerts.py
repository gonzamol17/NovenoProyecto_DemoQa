import time
import pytest
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
import HtmlTestRunner
from Utils import utils as utils
from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage
from POM.SubMenuPage import SubMenuPage
from POM.AlertsPage import AlertsPage


@pytest.mark.usefixtures("test_setup")
class TestAlerts(BaseClass):

    def test_Alerts(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        driver.execute_script("window.scrollTo(0, 300)")
        time.sleep(2)
        hp.clickElementsButton()
        time.sleep(2)
        smp = SubMenuPage(driver)
        time.sleep(2)
        smp.collapseElementsItem()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 300)")
        smp.expandAlertsFrameItem()
        smp.selectAlertsLink()
        time.sleep(2)
        ap = AlertsPage(driver)
        ap.selectSimpleAlertBtn()
        time.sleep(2)
        text = ap.handleSimpleAlert()
        assert text == "You clicked a button"
        ap.selectWaitAlertBtn()
        time.sleep(2)
        ap.handleWaitAlert()
        time.sleep(2)
        ap.selectConfirmAlertBtn()
        time.sleep(2)
        ap.handleConfirmAlert()
        print(ap.getConfirmAlertMsg())
        time.sleep(2)
        ap.selectPromtAlertBtn()
        time.sleep(2)
        name = "Gonzalo"
        ap.handlePromtAlert(name)
        time.sleep(2)
        #print(ap.getConfirmPromtAlertMsg())
        assert "You entered "+name == ap.getConfirmPromtAlertMsg()
        time.sleep(2)




