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
from POM.LoginPage import LoginPage


@pytest.mark.usefixtures("test_setup")
class TestLogin(BaseClass):

    def test_Login(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        driver.execute_script("window.scrollTo(0, 700)")
        time.sleep(2)
        hp.clickbookStoreButton()
        time.sleep(2)
        smp = SubMenuPage(driver)
        driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(2)
        smp.selectLoginLink()
        driver.execute_script("window.scrollTo(0, 200)")
        time.sleep(2)
        lp = LoginPage(driver)
        user = "pepe1"
        password = "Lorenzo10*"
        lp.tryLogin(user, password)
        time.sleep(2)
        assert lp.checkIfUserItsLogin() == user
        time.sleep(2)













