import time
import pytest
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
from Utils import utils as utils
from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage
from POM.UploadAndDownloadPage import UploadAndDownloadPage
from POM.ElementsPage import ElementsPage


class TestUploadAndDownload(BaseClass):

    def test_UploadAndDownload(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        driver.execute_script("window.scrollTo(0,200)")
        time.sleep(2)
        hp.clickElementsButton()
        time.sleep(2)
        ep = ElementsPage(driver)
        driver.execute_script("window.scrollTo(0,500)")
        time.sleep(2)
        ep.uploadAndDownloadLinks()
        ud = UploadAndDownloadPage(driver)
        driver.execute_script("window.scrollTo(0,400)")
        time.sleep(2)
        aux = "C:\\Users\\user\\Downloads\\IMG-20240422-WA0039.jpg"
        ud.selectBtnUploadFile(aux)
        aux1 = str("C:\\fakepath\\IMG-20240422-WA0039.jpg")
        assert ud.getMessageUploadFile() == aux1
        time.sleep(2)
        ud.selectBtnDownloadFile()
        time.sleep(2)
        ud.verifyDownloadedFile()
        time.sleep(3)


