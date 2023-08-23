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
from POM.ResizablePage import ResizablePage


@pytest.mark.usefixtures("test_setup")
class TestResizable(BaseClass):

    def test_Resizable(self):
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
        driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(2)
        smp.expandInteractionsItem()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(2)
        smp.selectResizableLink()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 400)")
        rp = ResizablePage(driver)
        rp.setSizeFirstBox()
        time.sleep(2)
        print(rp.getRestrictionFirstBox())
        time.sleep(2)
        #driver.execute_script("window.scrollTo(0, 200)")
        time.sleep(1)
        rp.setSizeSecondBox()
        time.sleep(2)
        print(rp.getRestrictionSecondBox())
        time.sleep(2)









