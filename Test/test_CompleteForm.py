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
from POM.FormsPage import FormsPage


@pytest.mark.usefixtures("test_setup")
class TestCompleteForm(BaseClass):

    def test_CompleteForm(self):
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
        smp.expandFormsItem()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 100)")
        fp = FormsPage(driver)
        time.sleep(2)
        fp.clickPracticeFormItem()
        driver.execute_script("window.scrollTo(0, 200)")
        time.sleep(2)
        fp.completeForm("Pedro", "Lopez", "pedro@gmail.com", "Male", "23234243", "Reading")
        time.sleep(2)


