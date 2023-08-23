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
from POM.TabsPage import TabsPage


@pytest.mark.usefixtures("test_setup")
class TestTabs(BaseClass):

    def test_Tabs(self):
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
        driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(2)
        smp.selectTabsLink()
        time.sleep(2)
        tp = TabsPage(driver)
        whattab = tp.getWhatStatusTabsSelected()
        assert str(whattab) == "true"
        assert "Lorem Ipsum is simply" in tp.getFirstPharagraph()
        time.sleep(2)
        tp.selectSecondTab()
        assert "Contrary to popular belief" in tp.getSecondPharagraph()
        time.sleep(2)
        tp.selectThirdTab()
        assert "It is a long established" in tp.getThirdPharagraph()
        time.sleep(2)









