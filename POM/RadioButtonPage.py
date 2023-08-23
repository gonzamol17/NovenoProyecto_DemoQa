import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class RadioButtonLocators:
    allRadioButton = (By.XPATH, "//input[@type='radio']")
    yesRadiobutton = (By.XPATH, "//label[contains(text(),'Yes')]")
    message = (By.CSS_SELECTOR, "#app div:nth-child(2)>p")
    impressiveRadioButton = (By.XPATH, "//label[contains(text(),'Impressive')]")



class RadioButtonPage:

    def __init__(self, driver):
        self.driver = driver

    def getAllRadioButton(self):
        return self.driver.find_elements(*RadioButtonLocators.allRadioButton)

    def selectYesRadioButton(self):
        self.driver.find_element(*RadioButtonLocators.yesRadiobutton).click()

    def selectImpressiveRadioButton(self):
        self.driver.find_element(*RadioButtonLocators.impressiveRadioButton).click()

    def getTitleRadioButtonSelected(self):
        return self.driver.find_element(*RadioButtonLocators.message).text




