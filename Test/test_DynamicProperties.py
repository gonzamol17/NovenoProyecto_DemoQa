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
from POM.DynamicPropertiesPage import DynamicPropertiesPage
from POM.ElementsPage import ElementsPage


@pytest.mark.usefixtures("test_setup")
class TestDynamicProperties(BaseClass):

    def test_DynamicProperties(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        driver.execute_script("window.scrollTo(0, 300)")
        time.sleep(2)
        hp.clickElementsButton()
        time.sleep(2)
        ep = ElementsPage(driver)
        driver.execute_script("window.scrollTo(0, 390)")
        time.sleep(2)
        ep.dynamicPropertiesLinks()
        dp = DynamicPropertiesPage(driver)
        assert str(dp.verifyEnabledBtn()) == "False"
        assert dp.verifyColorBtnBefore() == "rgba(255, 255, 255, 1)"
        time.sleep(5)
        assert str(dp.verifyEnabledBtn()) == "True"
        assert dp.verifyColorBtnBefore() == "rgba(230, 108, 120, 1)"
        time.sleep(3)


