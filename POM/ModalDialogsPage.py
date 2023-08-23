import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class ModalDialogsLocators:
    smallModal = (By.ID, "showSmallModal")
    largeModal = (By.ID, "showLargeModal")
    titleSmallModal = (By.CSS_SELECTOR, "body div>div.modal-body")
    closeSmallModal = (By.ID, "closeSmallModal")
    titleLargeModal = (By.CSS_SELECTOR, "body div>div.modal-body>p")
    closeLargeModal = (By.ID, "closeLargeModal")


class ModalDialogsPage:

    def __init__(self, driver):
        self.driver = driver

    def selectSmallModalBtn(self):
        self.driver.find_element(*ModalDialogsLocators.smallModal).click()

    def selectLargeModalBtn(self):
        self.driver.find_element(*ModalDialogsLocators.largeModal).click()

    def getTitlePopUpSmallModal(self):
        return self.driver.find_element(*ModalDialogsLocators.titleSmallModal).text

    def selectCloseSmallModalBtn(self):
        self.driver.find_element(*ModalDialogsLocators.closeSmallModal).click()

    def getTitlePopUpLargeModal(self):
        return self.driver.find_element(*ModalDialogsLocators.titleSmallModal).text

    def selectCloseLargeModalBtn(self):
        self.driver.find_element(*ModalDialogsLocators.closeLargeModal).click()

