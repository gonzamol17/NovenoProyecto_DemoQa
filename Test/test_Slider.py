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
from POM.SliderPage import SliderPage


@pytest.mark.usefixtures("test_setup")
class TestSlider(BaseClass):

    def test_Slider(self):
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
        driver.execute_script("window.scrollTo(0, 400)")
        time.sleep(2)
        smp.selectSliderLink()
        time.sleep(2)
        sp = SliderPage(driver)
        sp.moveSlider(125)
        value1 = sp.getNumberOfSlider()
        print(value1)
        value2 = sp.getSliderValue()
        print(value2)
        assert value1 == value2
        print("El valor en el slider es el mismo que está en el textbox")
        time.sleep(2)








