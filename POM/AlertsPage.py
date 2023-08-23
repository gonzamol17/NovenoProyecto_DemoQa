import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import wait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class AlertsLocators:
    singleAlertBtn = (By.ID, "alertButton")
    waitAlertBtn = (By.ID, "timerAlertButton")
    confirmBtn = (By.ID, "confirmButton")
    resultConfirmMsg = (By.ID, "confirmResult")
    promtBtn = (By.ID, "promtButton")
    promtConfirmMsg = (By.ID, "promptResult")


class AlertsPage:

    def __init__(self, driver):
        self.driver = driver

    def selectSimpleAlertBtn(self):
        self.driver.find_element(*AlertsLocators.singleAlertBtn).click()

    def handleSimpleAlert(self):
        alert = Alert(self.driver)
        aux = alert.text
        alert.accept()
        return aux

    def selectWaitAlertBtn(self):
        self.driver.find_element(*AlertsLocators.waitAlertBtn).click()

    def handleWaitAlert(self):
        time.sleep(10)
        alert = Alert(self.driver)
        alert.accept()
        print("Alert found")

    def selectConfirmAlertBtn(self):
        self.driver.find_element(*AlertsLocators.confirmBtn).click()

    def getConfirmAlertMsg(self):
        return self.driver.find_element(*AlertsLocators.resultConfirmMsg).text

    def handleConfirmAlert(self):
        alert = Alert(self.driver)
        alert.dismiss()

    def selectPromtAlertBtn(self):
        self.driver.find_element(*AlertsLocators.promtBtn).click()

    def handlePromtAlert(self, name):
        alert = Alert(self.driver)
        alert.send_keys(name)
        alert.accept()

    def getConfirmPromtAlertMsg(self):
        return self.driver.find_element(*AlertsLocators.promtConfirmMsg).text


