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
from POM.ToolTipsPage import ToolTipsPage


@pytest.mark.usefixtures("test_setup")
class TestToolTips(BaseClass):

    def test_ToolTips(self):
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
        driver.execute_script("window.scrollTo(0, 550)")
        time.sleep(2)
        smp.selectToolTipsLink()
        time.sleep(2)
        tt = ToolTipsPage(driver)
        tt.moveHoverGreenButton()
        assert "buttonToolTip" == tt.getTitletooltipGreenButton()
        print("Se está visualizando el tooltip que dice: You hovered over the Button")
        time.sleep(2)












