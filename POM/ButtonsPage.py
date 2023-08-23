import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class ButtonsLocators:
    doubleClickBtn = (By.ID, "doubleClickBtn")
    clickMeBtn = (By.XPATH, "//button[(text()='Click Me')]")
    rightClickBtn = (By.ID, "rightClickBtn")
    doubleMessage = (By.ID, "doubleClickMessage")
    rightMessage = (By.ID, "rightClickMessage")
    clickMessage = (By.CSS_SELECTOR, "p#dynamicClickMessage")


class ButtonsPage:

    def __init__(self, driver):
        self.driver = driver

    def doDoubleClick(self):
        action = ActionChains(self.driver)
        action.double_click(self.driver.find_element(*ButtonsLocators.doubleClickBtn)).perform()

    def getDoubleMessage(self):
        return self.driver.find_element(*ButtonsLocators.doubleMessage).text

    def doRightClick(self):
        action = ActionChains(self.driver)
        action.context_click(self.driver.find_element(*ButtonsLocators.rightClickBtn)).perform()

    def getRightMessage(self):
        return self.driver.find_element(*ButtonsLocators.rightMessage).text


    def doClick(self):
        self.driver.find_element(*ButtonsLocators.clickMeBtn).click()

    def getClickMessage(self):
        return self.driver.find_element(*ButtonsLocators.clickMessage).text




