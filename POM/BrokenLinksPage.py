import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class BrokenLinksLocators:
    validLink = (By.XPATH, "//a[contains(text(),'Click Here for Valid Link')]")
    invalidLink = (By.XPATH, "//a[contains(text(),'Click Here for Broken Link')]")
    titleBrokenLink = (By.CSS_SELECTOR, "#content>div>p")


class BrokenLinksPage:

    def __init__(self, driver):
        self.driver = driver

    def selectValidLink(self):
        self.driver.find_element(*BrokenLinksLocators.validLink).click()
        aux = self.driver.current_url
        self.driver.back()
        return aux

    def selectInvalidLink(self):
        self.driver.find_element(*BrokenLinksLocators.invalidLink).click()
        time.sleep(2)
        aux = self.driver.find_element(*BrokenLinksLocators.titleBrokenLink).text
        return aux





