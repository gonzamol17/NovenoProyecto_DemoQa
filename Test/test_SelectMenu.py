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
from POM.SelectMenuPage import SelectMenuPage


@pytest.mark.usefixtures("test_setup")
class TestSelectMenu(BaseClass):

    def test_SelectMenu(self):
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
        driver.execute_script("window.scrollTo(0, 700)")
        time.sleep(2)
        smp.selectSelectMenuLink()
        time.sleep(2)
        smp = SelectMenuPage(driver)
        time.sleep(2)
        smp.selectItemDropdown1()
        time.sleep(1)
        smp.selectValue1("Group 1, option 1")
        time.sleep(1)
        smp.selectItemDropdown2()
        time.sleep(1)
        smp.selectValue2("Mr.")
        time.sleep(1)
        smp.selectItemDropdown3()
        smp.selectColor("Purple")
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 400)")
        time.sleep(2)
        smp.selectCars("Saab", "Audi")
        time.sleep(2)










