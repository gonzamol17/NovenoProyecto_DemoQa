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
from POM.CheckBoxPage import CheckBoxPage
from POM.ElementsPage import ElementsPage


@pytest.mark.usefixtures("test_setup")
class TestCheckBox(BaseClass):

    def test_CheckBox(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        driver.execute_script("window.scrollTo(0, 200)")
        time.sleep(2)
        hp.clickElementsButton()
        time.sleep(2)
        ep = ElementsPage(driver)
        ep.clickCheckBoxItem()
        cbp = CheckBoxPage(driver)
        assert cbp.getMainTitle() == "Check Box"
        time.sleep(2)
        cbp.clickHomeChevron()
        chevrones = cbp.getAllChildChevron()
        lis1 = ['Desktop', 'Documents', 'Downloads']
        n = 0
        for chevron in chevrones:
            assert chevron.text == lis1[n]
            n = n + 1
        driver.execute_script("window.scrollTo(0, 100)")
        time.sleep(2)
        cbp.clickDownloadChevron()
        time.sleep(2)
        downs = cbp.getAllChildDownloadChevron()
        lis2 = ['Word File.doc', 'Excel File.doc']
        n = 0
        for down in downs:
            assert down.text == lis2[n]
            n = n + 1
        time.sleep(2)
        cbp.selectallChildDownloadCheckbox()
        time.sleep(2)
        assert cbp.getTheResult().text == "You have selected :\ndownloads\nwordFile\nexcelFile"
        time.sleep(3)


