import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class MenuLocators:
    mainMenuItem2 = (By.CSS_SELECTOR, "#nav > li:nth-child(2) > a")
    subItems = (By.CSS_SELECTOR, "#nav > li:nth-child(2) > ul > li > a")
    subListItems = (By.CSS_SELECTOR, "#nav  ul > li:nth-child(3) > ul > li> a")





class MenuPage:

    def __init__(self, driver):
        self.driver = driver

    def getAllItems(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(*MenuLocators.mainMenuItem2)).perform()
        return self.driver.find_elements(*MenuLocators.subItems)

    def selectMenuItem2Button(self, items):
        for item in items:
            time.sleep(1)
            if "n/a" in item.text:
                print("opción vacía " + item.text)
            else:
                action = ActionChains(self.driver)
                action.move_to_element(item).perform()
                time.sleep(1)
                #print("opción habilitada " + item.text)
                if item.text == "SUB SUB LIST »":
                    print("Se encontró la opción: "+item.text)
                    print("Estos son los subitems de Sub Sub List")
                    subItems = self.driver.find_elements(*MenuLocators.subListItems)
                    for subitem in subItems:
                        action = ActionChains(self.driver)
                        action.move_to_element(subitem).perform()
                        print(subitem.text)















