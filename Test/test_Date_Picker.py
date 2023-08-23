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
from POM.DatePickerPage import DatePickerPage


@pytest.mark.usefixtures("test_setup")
class TestDatePicker(BaseClass):

    def test_DatePicker(self):
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
        smp.selectDatePickerLink()
        time.sleep(2)
        dp = DatePickerPage(driver)
        dp.selectDate()
        time.sleep(2)
        year = "1990"
        month = "July"
        day = "003"
        flag = dp.selectYearMonthAndDay(year, month, day)
        if flag == 1:
            print("Now the date selected and visualized in the text box is: "+dp.showDateSelected())
        else:
            print("The selected date could not be found")
        time.sleep(2)
        assert year in dp.showDateSelected()
        time.sleep(2)





