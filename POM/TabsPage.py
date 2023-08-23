import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class TabsLocators:
    whatTabs = (By.ID, "demo-tab-what")
    originTabs = (By.ID, "demo-tab-origin")
    useTabs = (By.ID, "demo-tab-use")
    firstParagraph = (By.CSS_SELECTOR, "#demo-tabpane-what > p")
    secondParagraph = (By.CSS_SELECTOR, "#demo-tabpane-origin > p")
    thirdParagraph = (By.CSS_SELECTOR, "#demo-tabpane-use > p")



class TabsPage:

    def __init__(self, driver):
        self.driver = driver

    def getWhatStatusTabsSelected(self):
        return self.driver.find_element(*TabsLocators.whatTabs).get_attribute('aria-selected')

    def getFirstPharagraph(self):
        return self.driver.find_element(*TabsLocators.firstParagraph).text

    def selectSecondTab(self):
        self.driver.find_element(*TabsLocators.originTabs).click()

    def getSecondPharagraph(self):
        return self.driver.find_element(*TabsLocators.secondParagraph).text

    def selectThirdTab(self):
        self.driver.find_element(*TabsLocators.useTabs).click()

    def getThirdPharagraph(self):
        return self.driver.find_element(*TabsLocators.thirdParagraph).text






