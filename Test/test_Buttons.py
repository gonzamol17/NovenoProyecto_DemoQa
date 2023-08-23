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
from POM.ButtonsPage import ButtonsPage
from POM.ElementsPage import ElementsPage


@pytest.mark.usefixtures("test_setup")
class TestButtons(BaseClass):

    def test_Buttons(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        driver.execute_script("window.scrollTo(0, 300)")
        time.sleep(2)
        hp.clickElementsButton()
        time.sleep(2)
        ep = ElementsPage(driver)
        driver.execute_script("window.scrollTo(0, 200)")
        time.sleep(2)
        ep.clickButtons()
        bp = ButtonsPage(driver)
        time.sleep(2)
        bp.doDoubleClick()
        assert bp.getDoubleMessage() == "You have done a double click"
        time.sleep(2)
        bp.doRightClick()
        assert bp.getRightMessage() == "You have done a right click"
        driver.execute_script("window.scrollTo(0, 200)")
        time.sleep(2)
        bp.doClick()
        time.sleep(2)
        assert bp.getClickMessage() == "You have done a dynamic click"
        time.sleep(3)


