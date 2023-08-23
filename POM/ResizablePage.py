import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class ResizableLocators:
    firstCorner = (By.CSS_SELECTOR, "#resizableBoxWithRestriction > span")
    restriccionFirsBox = (By.ID, "resizableBoxWithRestriction")
    secondCorner = (By.CSS_SELECTOR, "#resizable>span")
    restriccionSecondBox = (By.ID, "resizable")



class ResizablePage:

    def __init__(self, driver):
        self.driver = driver

    def setSizeFirstBox(self):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(self.driver.find_element(*ResizableLocators.firstCorner), 300, 250).perform()


    def getRestrictionFirstBox(self):
        return self.driver.find_element(*ResizableLocators.restriccionFirsBox).get_attribute('style')


    def setSizeSecondBox(self):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(self.driver.find_element(*ResizableLocators.secondCorner), 100, 100).perform()


    def getRestrictionSecondBox(self):
        return self.driver.find_element(*ResizableLocators.restriccionSecondBox).get_attribute('style')






