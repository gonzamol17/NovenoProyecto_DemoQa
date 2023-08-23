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
from POM.SelectablePage import SelectablePage


@pytest.mark.usefixtures("test_setup")
class TestSelectable(BaseClass):

    def test_Selectable(self):
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
        driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(2)
        smp.expandInteractionsItem()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(2)
        smp.selectSelectableLink()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 200)")
        sp = SelectablePage(driver)
        print("\nThis is the name of Items listed")
        sp.getListElements()
        time.sleep(1)
        sp.markEachListItems()
        time.sleep(1)
        itemcolor = sp.getColorOfEachItemsList()
        time.sleep(1)
        for li in range(len(itemcolor)):
            assert itemcolor[li] == "rgba(0, 123, 255, 1)"

        print("todos los elementos al ser seleccionados, se muestran con el color azul")
        time.sleep(1)








