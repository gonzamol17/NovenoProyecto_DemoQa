import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class AutoCompleteLocators:
    textFieldMultipleColor = (By.ID, "autoCompleteMultipleInput")
    textFieldSingleColor = (By.ID, "autoCompleteSingleInput")
    multipleColorSelected = (By.CSS_SELECTOR, "#autoCompleteMultipleContainer div.css-1rhbuit-multiValue.auto-complete__multi-value> div.css-12jo7m5.auto-complete__multi-value__label")
    singleColorSelected = (By.CSS_SELECTOR, "#autoCompleteSingleContainer div.auto-complete__single-value.css-1uccc91-singleValue")

class AutoCompletePage:

    def __init__(self, driver):
        self.driver = driver

    def typeMultipleColorField(self, color):
        self.driver.find_element(*AutoCompleteLocators.textFieldMultipleColor).send_keys(color)
        time.sleep(2)
        self.driver.find_element(*AutoCompleteLocators.textFieldMultipleColor).send_keys(Keys.ENTER)

    def typeSingleColorField(self, color):
        self.driver.find_element(*AutoCompleteLocators.textFieldSingleColor).send_keys(color)
        time.sleep(2)
        self.driver.find_element(*AutoCompleteLocators.textFieldSingleColor).send_keys(Keys.ENTER)

    def getMultipleColorSelected(self):
        return self.driver.find_element(*AutoCompleteLocators.multipleColorSelected).text

    def getSingleColorSelected(self):
        return self.driver.find_element(*AutoCompleteLocators.singleColorSelected).text

