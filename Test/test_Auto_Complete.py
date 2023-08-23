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
from POM.AutoCompletePage import AutoCompletePage


@pytest.mark.usefixtures("test_setup")
class TestAutoComplete(BaseClass):

    def test_Auto_Complete(self):
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
        time.sleep(2)
        smp.expandWidgetsItem()
        time.sleep(2)
        smp.selectAutoCompleteLink()
        time.sleep(2)
        value = str("Red")
        value1 = str("Blue")
        ap = AutoCompletePage(driver)
        ap.typeMultipleColorField(value)
        assert ap.getMultipleColorSelected() == value
        time.sleep(4)
        ap.typeSingleColorField(value1)
        assert ap.getSingleColorSelected() == value1
        time.sleep(2)


