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
from POM.MenuPage import MenuPage


@pytest.mark.usefixtures("test_setup")
class TestMenu(BaseClass):

    def test_Menu(self):
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
        driver.execute_script("window.scrollTo(0, 600)")
        time.sleep(2)
        smp.selectMenuLink()
        time.sleep(2)
        mp = MenuPage(driver)
        items = mp.getAllItems()
        mp.selectMenuItem2Button(items)
        time.sleep(2)









