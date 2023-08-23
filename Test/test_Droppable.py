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
from POM.DroppablePage import DroppablePage


@pytest.mark.usefixtures("test_setup")
class TestDroppable(BaseClass):

    def test_Droppable(self):
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
        driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(2)
        smp.selectDroppableLink()
        time.sleep(2)
        dp = DroppablePage(driver)
        assert dp.getTitleBeforeDroppableAction() == "Drop here"
        time.sleep(1)
        dp.dragAndDrop()
        driver.execute_script("window.scrollTo(0, 200)")
        time.sleep(3)
        assert dp.getTitleAfterDroppableAction() == "Dropped!"
        assert dp.getColorAfterDroppableAction() == "rgba(70, 130, 180, 1)"
        print("\nAhora se está visualizando en color azul el box, y además se visualiza el título: "+dp.getTitleAfterDroppableAction())
        time.sleep(2)











