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
from POM.RadioButtonPage import RadioButtonPage
from POM.ElementsPage import ElementsPage


@pytest.mark.usefixtures("test_setup")
class TestRadioButton(BaseClass):

    def test_RadioButton(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        driver.execute_script("window.scrollTo(0, 200)")
        time.sleep(2)
        hp.clickElementsButton()
        driver.execute_script("window.scrollTo(0, 100)")
        time.sleep(2)
        ep = ElementsPage(driver)
        ep.clickRadioButtonItem()
        time.sleep(2)
        rbp = RadioButtonPage(driver)
        radios = rbp.getAllRadioButton()
        n = 1
        for radio in radios:
            if n < 3:
                assert str(radio.is_enabled()) == "True"
                n = n + 1
            else:
                assert str(radio.is_enabled()) == "False"
                n = n + 1
        time.sleep(2)
        rbp.selectYesRadioButton()
        assert rbp.getTitleRadioButtonSelected() == "You have selected Yes"
        time.sleep(2)
        rbp.selectImpressiveRadioButton()
        assert rbp.getTitleRadioButtonSelected() == "You have selected Impressive"
        time.sleep(3)



