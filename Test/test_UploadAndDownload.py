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
from POM.UploadAndDownloadPage import UploadAndDownloadPage
from POM.ElementsPage import ElementsPage


@pytest.mark.usefixtures("test_setup")
class TestUploadAndDownload(BaseClass):

    def test_UploadAndDownload(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        driver.execute_script("window.scrollTo(0, 200)")
        time.sleep(2)
        hp.clickElementsButton()
        time.sleep(2)
        ep = ElementsPage(driver)
        driver.execute_script("window.scrollTo(0,370)")
        ep.uploadAndDownloadLinks()
        ud = UploadAndDownloadPage(driver)
        time.sleep(2)
        aux = "C:\\Users\\admin\\Desktop\\redBinance.png"
        ud.selectBtnUploadFile(aux)
        aux1 = str("C:\\fakepath\\redBinance.png")
        assert ud.getMessageUploadFile() == aux1
        time.sleep(2)
        ud.selectBtnDownloadFile()
        time.sleep(2)
        ud.verifyDownloadedFile()
        time.sleep(3)


