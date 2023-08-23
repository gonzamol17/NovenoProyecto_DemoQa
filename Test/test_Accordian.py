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
from POM.AccordianPage import AccordianPage


@pytest.mark.usefixtures("test_setup")
class TestAccordian(BaseClass):

    def test_Accordian(self):
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
        smp.selectAccordianLink()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 300)")
        time.sleep(2)
        ap = AccordianPage(driver)
        list = ap.getParagraphs()
        for i in range(0, len(list)):
            print(list[i])
            if [i] == 0:
                assert "Lorem Ipsum is simply" in list[i]
            if [i] == 1:
                assert "Contrary to popular belief" in list[i]
            if [i] == 2:
                assert "It is a long established" in list[i]




