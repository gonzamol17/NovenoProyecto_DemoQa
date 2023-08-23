import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class HomePageLocators:
    elementsButton = (By.CSS_SELECTOR, "div.card.mt-4.top-card:nth-child(1)")
    bookStoreButton = (By.CSS_SELECTOR, "div.card.mt-4.top-card:nth-child(6)")

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def clickElementsButton(self):
        self.driver.find_element(*HomePageLocators.elementsButton).click()

    def clickbookStoreButton(self):
        self.driver.find_element(*HomePageLocators.bookStoreButton).click()




