import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class DroppableLocators:
    draggablebox = (By.ID, "draggable")
    droppablebox = (By.ID, "droppable")
    titleOnBoxDroppable = (By.CSS_SELECTOR, "#droppable > p")
    gridTab = (By.ID, "demo-tab-grid")
    gridItems = (By.CSS_SELECTOR, "#demo-tabpane-grid > div > div > div")



class DroppablePage:

    def __init__(self, driver):
        self.driver = driver

    def getTitleBeforeDroppableAction(self):
        return self.driver.find_element(*DroppableLocators.titleOnBoxDroppable).text

    def dragAndDrop(self):
        action = ActionChains(self.driver)
        action.drag_and_drop(self.driver.find_element(*DroppableLocators.draggablebox), self.driver.find_element(*DroppableLocators.droppablebox)).perform()

    def getTitleAfterDroppableAction(self):
        return self.driver.find_element(*DroppableLocators.titleOnBoxDroppable).text

    def getColorAfterDroppableAction(self):
        return self.driver.find_element(*DroppableLocators.droppablebox).value_of_css_property('background-color')






