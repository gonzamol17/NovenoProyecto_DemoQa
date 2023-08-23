import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class ToolTipsLocators:
    greenButton = (By.ID, "toolTipButton")
    tooltipGreenButton = (By.ID, "buttonToolTopContainer")




class ToolTipsPage:

    def __init__(self, driver):
        self.driver = driver

    def moveHoverGreenButton(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(*ToolTipsLocators.greenButton)).perform()

    def getTitletooltipGreenButton(self):
        return self.driver.find_element(*ToolTipsLocators.greenButton).get_attribute("aria-describedby")









