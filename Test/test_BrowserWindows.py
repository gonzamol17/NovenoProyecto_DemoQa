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
from POM.AlertFramePage import AlertFramePage


@pytest.mark.usefixtures("test_setup")
class TestBrowserWindow(BaseClass):

    def test_BrowserWindow(self):
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
        driver.execute_script("window.scrollTo(0, 300)")
        time.sleep(2)
        smp.expandAlertsFrameItem()
        time.sleep(2)
        ap = AlertFramePage(driver)
        smp.selectBrowserWindowLink()
        time.sleep(2)
        ap.selectNewTabBtn()
        ap.handleWindows()
        time.sleep(2)
        ap.selectNewWindowBtn()
        time.sleep(2)
        ap.handleWindows()
        time.sleep(2)
        ap.selectNewWidowsMsgBtn()
        time.sleep(2)




