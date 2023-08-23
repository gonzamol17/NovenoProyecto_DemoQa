import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class DynamicPropertiesLocators:
    enabledBtn = (By.ID, "enableAfter")
    changeColorBtn = (By.ID, "colorChange")
    visibleBtn = (By.ID, "visibleAfter")

class DynamicPropertiesPage:

    def __init__(self, driver):
        self.driver = driver


    def verifyEnabledBtn(self):
        return self.driver.find_element(*DynamicPropertiesLocators.enabledBtn).is_enabled()

    def verifyVisibleBtn(self):
        return self.driver.find_element(*DynamicPropertiesLocators.visibleBtn).is_displayed()

    def verifyColorBtnBefore(self):
        return self.driver.find_element(*DynamicPropertiesLocators.changeColorBtn).value_of_css_property('color')












