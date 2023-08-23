import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class ElementsLocators:
    textBoxItem = (By.CSS_SELECTOR, "#item-0")
    checkBoxItem = (By.XPATH, "//span[contains(text(),'Check Box')]")
    radioButtonItem = (By.XPATH, "//span[contains(text(),'Radio Button')]")
    webTablesItem = (By.XPATH, "//span[contains(text(),'Web Tables')]")
    buttonsItem = (By.XPATH, "//span[contains(text(),'Buttons')]")
    linksItem = (By.XPATH, "//span[contains(text(),'Links')]")
    brokenLinksItem = (By.XPATH, "//span[contains(text(),'Broken Links - Images')]")
    uploadAndDownloadItem = (By.XPATH, "//span[contains(text(),'Upload and Download')]")
    dynamicPropertiesItem = (By.XPATH, "//span[contains(text(),'Dynamic Properties')]")

class ElementsPage:

    def __init__(self, driver):
        self.driver = driver

    def clickTextBoxItem(self):
        self.driver.find_element(*ElementsLocators.textBoxItem).click()

    def clickCheckBoxItem(self):
        self.driver.find_element(*ElementsLocators.checkBoxItem).click()

    def clickRadioButtonItem(self):
        self.driver.find_element(*ElementsLocators.radioButtonItem).click()

    def clickWebTables(self):
        self.driver.find_element(*ElementsLocators.webTablesItem).click()

    def clickButtons(self):
        self.driver.find_element(*ElementsLocators.buttonsItem).click()

    def clickLinks(self):
        self.driver.find_element(*ElementsLocators.linksItem).click()

    def clickBrokenLinks(self):
        self.driver.find_element(*ElementsLocators.brokenLinksItem).click()

    def uploadAndDownloadLinks(self):
        self.driver.find_element(*ElementsLocators.uploadAndDownloadItem).click()

    def dynamicPropertiesLinks(self):
        self.driver.find_element(*ElementsLocators.dynamicPropertiesItem).click()

