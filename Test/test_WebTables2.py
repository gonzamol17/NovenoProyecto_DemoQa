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
from POM.WebTablesPage import WebTablesPage
from POM.ElementsPage import ElementsPage


@pytest.mark.usefixtures("test_setup")
class TestWebTables2(BaseClass):

    def test_WebTables2(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        driver.execute_script("window.scrollTo(0, 200)")
        time.sleep(2)
        hp.clickElementsButton()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 200)")
        time.sleep(2)
        ep = ElementsPage(driver)
        ep.clickWebTables()
        driver.execute_script("window.scrollTo(0, 200)")
        wtp = WebTablesPage(driver)
        name = "Kierra"
        wtp.editUserFromTable(name)
        age = 38
        wtp.updateAgeField(age)
        updatedage = wtp.verifyTheAgeWasUpdated(name)
        assert updatedage == str(age)
        print("El usuario: "+name+" se ha actualizado correctamente su edad, ahora tiene: "+updatedage)
        time.sleep(3)









