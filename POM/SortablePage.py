import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class SortableLocators:
    listItems = (By.CSS_SELECTOR, "#demo-tabpane-list > div>div")
    sixtab = (By.CSS_SELECTOR, "#demo-tabpane-list > div > div:nth-child(6)")
    onetab = (By.CSS_SELECTOR, "#demo-tabpane-list > div > div:nth-child(1)")
    gridTab = (By.ID, "demo-tab-grid")
    gridItems = (By.CSS_SELECTOR, "#demo-tabpane-grid > div > div > div")



class SortablePage:

    def __init__(self, driver):
        self.driver = driver

    def getListElements(self):
        items = self.driver.find_elements(*SortableLocators.listItems)
        for item in items:
            print(item.text)

    def moveOrderOfTabs(self):
        origin = self.driver.find_element(*SortableLocators.onetab)
        destination = self.driver.find_element(*SortableLocators.sixtab)
        action = ActionChains(self.driver)
        action.drag_and_drop(destination, origin).pause(4).perform()


    def selectGridTab(self):
        self.driver.find_element(*SortableLocators.gridTab).click()

    def getGridItemsList(self):
        items = self.driver.find_elements(*SortableLocators.gridItems)
        for item in items:
            print(item.text)

    def doHoverEffectOnGridItems(self):
        action = ActionChains(self.driver)
        items = self.driver.find_elements(*SortableLocators.gridItems)
        n = 1
        while n < 7:
            time.sleep(1)
            action.move_to_element(self.driver.find_element(By.CSS_SELECTOR, "#demo-tabpane-grid > div > div > div:nth-child("+ str(n) +")")).perform()
            n = n+1






