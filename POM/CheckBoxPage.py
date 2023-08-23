import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class CheckBoxLocators:
    mainTitle = (By.CSS_SELECTOR, "#app div.playgound-header>div")
    homeChevron = (By.CSS_SELECTOR, "svg.rct-icon.rct-icon-expand-close")
    allChildChevron = (By.CSS_SELECTOR, "#tree-node li>ol span.rct-title")
    downloadChevron = (By.CSS_SELECTOR, "#tree-node li:nth-child(3) button>svg")
    allChildDownloadChevron = (By.CSS_SELECTOR, "#tree-node li>ol ol span>label>span.rct-title")
    childDownloadCheckBoxes = (By.CSS_SELECTOR, "#tree-node> ol ol >li.rct-node-expanded li>span span.rct-checkbox")
    labelResult = (By.CSS_SELECTOR, "#result")

class CheckBoxPage:

    def __init__(self, driver):
        self.driver = driver


    def getMainTitle(self):
        return self.driver.find_element(*CheckBoxLocators.mainTitle).text

    def clickHomeChevron(self):
        self.driver.find_element(*CheckBoxLocators.homeChevron).click()

    def getAllChildChevron(self):
        return self.driver.find_elements(*CheckBoxLocators.allChildChevron)

    def clickDownloadChevron(self):
        self.driver.find_element(*CheckBoxLocators.downloadChevron).click()

    def getAllChildDownloadChevron(self):
        return self.driver.find_elements(*CheckBoxLocators.allChildDownloadChevron)

    def selectallChildDownloadCheckbox(self):
        checkboxes = self.driver.find_elements(*CheckBoxLocators.childDownloadCheckBoxes)
        n = 1
        for checkbox in checkboxes:
            self.driver.find_element(By.CSS_SELECTOR, "#tree-node> ol ol >li.rct-node-expanded li:nth-child(" + str(n) + ")>span span.rct-checkbox").click()
            n = n + 1
            time.sleep(1)

    def getTheResult(self):
        return self.driver.find_element(*CheckBoxLocators.labelResult)






