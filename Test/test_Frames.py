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
from POM.FramesPage import FramesPage


@pytest.mark.usefixtures("test_setup")
class TestFrames(BaseClass):

    def test_Frames(self):
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
        smp.expandAlertsFrameItem()
        smp.selectFramesLink()
        time.sleep(2)
        fp = FramesPage(driver)
        title = fp.getTitleFirstFrame("frame1")
        time.sleep(2)
        print(title)
        driver.switch_to.default_content()
        driver.execute_script("window.scrollTo(0, 300)")
        time.sleep(2)
        title2 = fp.doSomeActionOnSecondFrame("frame2")
        print(title2)
        time.sleep(2)




