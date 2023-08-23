import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class FramesLocators:

    getTitleFirstFrame = (By.CSS_SELECTOR, "#sampleHeading")



class FramesPage:

    def __init__(self, driver):
        self.driver = driver

    def getTitleFirstFrame(self, id):
        self.driver.switch_to.frame(id)
        return self.driver.find_element(*FramesLocators.getTitleFirstFrame).text

    def doSomeActionOnSecondFrame(self, id2):
        self.driver.switch_to.frame(id2)
        time.sleep(2)
        return self.driver.find_element(*FramesLocators.getTitleFirstFrame).text


