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
from POM.BrokenLinksPage import BrokenLinksPage
from POM.ElementsPage import ElementsPage

@pytest.mark.usefixtures("test_setup")
class TestBrokenLinks(BaseClass):

    def test_BrokenLinks(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        driver.execute_script("window.scrollTo(0, 300)")
        time.sleep(2)
        hp.clickElementsButton()
        time.sleep(2)
        ep = ElementsPage(driver)
        driver.execute_script("window.scrollTo(0, 300)")
        time.sleep(2)
        ep.clickBrokenLinks()
        driver.execute_script("window.scrollTo(0, 200)")
        blp = BrokenLinksPage(driver)
        actualurl = blp.selectValidLink()
        assert "https://demoqa.com/" == actualurl
        driver.execute_script("window.scrollTo(0, 300)")
        newUrl = blp.selectInvalidLink()
        time.sleep(2)
        assert "This page returned a 500 status code." in newUrl
        time.sleep(3)


