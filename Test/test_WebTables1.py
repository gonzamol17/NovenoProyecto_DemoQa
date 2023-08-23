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
class TestWebTables1(BaseClass):

    def test_WebTables1(self):
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
        time.sleep(2)
        name = "Alina"
        wtp.makeASearch(name)
        time.sleep(2)
        assert wtp.getZeroResult() == "No rows found"
        time.sleep(2)
        wtp.selectAddButton()
        time.sleep(2)
        wtp.completeForm(name, "Marcial", "alinamarcial@yahoo.com", "22", "3000", "Marketing")
        time.sleep(2)
        employees = wtp.getAllEmployees()
        for i in employees:
            print(i)
            if i == name:
                assert name == i
                print("Se encontró en la lista, el usuario/a recientemente agregado/a, y es: "+name)
        time.sleep(3)









