import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class LoginLocators:
    btnLogin = (By.ID, "login")
    userNameTF = (By.ID, "userName")
    passwordTF = (By.ID, "password")
    lblLoged = (By.ID, "userName-value")


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def tryLogin(self, username, password):
        self.driver.find_element(*LoginLocators.userNameTF).send_keys(username)
        time.sleep(1)
        self.driver.find_element(*LoginLocators.passwordTF).send_keys(password)
        time.sleep(1)
        self.driver.find_element(*LoginLocators.btnLogin).click()

    def checkIfUserItsLogin(self):
        return self.driver.find_element(*LoginLocators.lblLoged).text


