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
from POM.SortablePage import SortablePage


@pytest.mark.usefixtures("test_setup")
class TestSortable(BaseClass):

    def test_Sortable(self):
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
        driver.execute_script("window.scrollTo(0, 400)")
        time.sleep(2)
        smp.expandInteractionsItem()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 400)")
        time.sleep(2)
        smp.selectSortableLink()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 200)")
        sp = SortablePage(driver)
        sp.getListElements()
        time.sleep(1)
        sp.moveOrderOfTabs()
        print("Y cambiando el orden de dos de los numeros, el orden ahora queda así:")
        sp.getListElements()
        time.sleep(2)
        print("Y el orden de los items en la tab Grid, es:")
        sp.selectGridTab()
        time.sleep(1)
        sp.getGridItemsList()
        time.sleep(1)
        sp.doHoverEffectOnGridItems()
        time.sleep(2)









