import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class SelectableLocators:
    listItems = (By.CSS_SELECTOR, "#verticalListContainer > li")




class SelectablePage:

    def __init__(self, driver):
        self.driver = driver

    def getListElements(self):
        items = self.driver.find_elements(*SelectableLocators.listItems)
        for item in items:
            print(item.text)

    #def selectGridTab(self):
     #   self.driver.find_element(*SortableLocators.gridTab).click()

    def markEachListItems(self):
        items = self.driver.find_elements(*SelectableLocators.listItems)
        for item in items:
            time.sleep(1)
            item.click()

    def getColorOfEachItemsList(self):
        items = self.driver.find_elements(*SelectableLocators.listItems)
        itemcolor = []
        for item in items:
            #print(item.value_of_css_property('background-color'))
            itemcolor.append(item.value_of_css_property('background-color'))
        return itemcolor






