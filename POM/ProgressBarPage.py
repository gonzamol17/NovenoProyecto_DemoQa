import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class ProgressBarLocators:
    startStopButton = (By.ID, "startStopButton")
    resetButton = (By.ID, "resetButton")
    progressBar = (By.CSS_SELECTOR, "#progressBar>div")




class ProgressBarPage:

    def __init__(self, driver):
        self.driver = driver

    def selectStartStopButton(self):
        self.driver.find_element(*ProgressBarLocators.startStopButton).click()

    def selectResetButton(self):
        self.driver.find_element(*ProgressBarLocators.resetButton).click()

    def verifyResetButton(self):
        return self.driver.find_element(*ProgressBarLocators.resetButton).is_displayed()

    def checkProgressBarColor(self):
        return self.driver.find_element(*ProgressBarLocators.progressBar).value_of_css_property('background-color')

    def verifyValueOnProgressBar(self):
        return self.driver.find_element(*ProgressBarLocators.progressBar).text




