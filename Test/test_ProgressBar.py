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
from POM.ProgressBarPage import ProgressBarPage


@pytest.mark.usefixtures("test_setup")
class TestProgressBar(BaseClass):

    def test_ProgressBar(self):
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
        driver.execute_script("window.scrollTo(0, 400)")
        time.sleep(2)
        smp.selectProgressBarLink()
        time.sleep(2)
        pbp = ProgressBarPage(driver)
        pbp.selectStartStopButton()
        time.sleep(7)
        result = str(pbp.verifyResetButton())
        assert result == "True"
        assert "rgba(40, 167, 69, 1)" == pbp.checkProgressBarColor()
        time.sleep(2)
        assert "100%" == pbp.verifyValueOnProgressBar()
        pbp.selectResetButton()
        print(pbp.checkProgressBarColor())
        time.sleep(2)








