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
from POM.TextBoxPage import TextBoxPage
from POM.ElementsPage import ElementsPage


@pytest.mark.usefixtures("test_setup")
class TestTextBox(BaseClass):

    def test_TextBox(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        driver.execute_script("window.scrollTo(0, 200)")
        time.sleep(2)
        hp.clickElementsButton()
        #driver.switch_to.frame(0)
        #driver.switch_to.default_content()
        time.sleep(2)
        ep = ElementsPage(driver)
        ep.clickTextBoxItem()
        tbp = TextBoxPage(driver)
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 230)")
        tbp.completeAllTheForm("pepe", "pepe@hotmail.com", "Olayon", "Mayas")
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 300)")
        print("\nTodos los datos ingresados son: \n"+tbp.getAllDataSumbited())
        time.sleep(3)


