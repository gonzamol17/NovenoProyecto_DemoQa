import time
import pytest
import unittest
import sys
import os

import softest

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
import HtmlTestRunner
from Utils import utils as utils
from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage
from POM.LinksPage import LinksPage
from POM.ElementsPage import ElementsPage


@pytest.mark.usefixtures("test_setup")
class TestLinks(BaseClass, softest.TestCase):

    def test_Links(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        driver.execute_script("window.scrollTo(0, 300)")
        time.sleep(2)
        hp.clickElementsButton()
        time.sleep(2)
        ep = ElementsPage(driver)
        driver.execute_script("window.scrollTo(0, 200)")
        time.sleep(2)
        ep.clickLinks()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 300)")
        lp = LinksPage(driver)
        lp.selectSimpleLink()
        urls = lp.switchBetweenMoreThanOneTabs()
        #los siguientes assert que se usan abajo son softassert
        #y para usarlos primero hay que extender el test de la clase softest
        #y para esto se pone esto "softest" dentro de class TestLinks(BaseClass, softest.TestCase):
        #esto nos permite usar los soft assert como assertIn o assertNotIn
        #antes de esto debemos ejecutar también en la consola el comando pip install softest para
        #descargarnos esa libreria, y ya estamos en condiciones de usarlos con los siguientes comando:
        #self.assertIn("https://demoqa.com/", urls), en este caso url es una lista con dos elementos, y
        #quiero ver si la url que yo le paso está dentro de esa lista, si está ok me devuelve true
        #driver.assertIn("https://demoqa.com/", urls)
        #self.soft_assert(self.assertIn, "https://demoqa.com/", urls)
        self.assertIn("https://demoqa.com/", urls)
        self.assertIn("https://demoqa.com/links", urls)
        message = lp.verifyBrokenLink()
        assert "401" in message
        time.sleep(3)


