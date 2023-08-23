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
from POM.ModalDialogsPage import ModalDialogsPage


@pytest.mark.usefixtures("test_setup")
class TestModalDialogs(BaseClass):

    def test_ModalDialogs(self):
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
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 350)")
        time.sleep(2)
        smp.selectModalDialogsLink()
        time.sleep(2)
        mp = ModalDialogsPage(driver)
        mp.selectSmallModalBtn()
        time.sleep(2)
        assert mp.getTitlePopUpSmallModal() == "This is a small modal. It has very less content"
        time.sleep(2)
        mp.selectCloseSmallModalBtn()
        time.sleep(2)
        mp.selectLargeModalBtn()
        time.sleep(2)
        assert " text ever since the 1500s" in mp.getTitlePopUpSmallModal()
        time.sleep(2)
        mp.selectCloseLargeModalBtn()
        time.sleep(2)



