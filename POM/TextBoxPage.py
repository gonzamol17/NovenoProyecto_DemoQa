import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class TextBoxLocators:
    name = (By.ID, "userName")
    email = (By.ID, "userEmail")
    currAdd = (By.ID, "currentAddress")
    perAdd = (By.ID, "permanentAddress")
    btnSubmit = (By.ID, "submit")
    dataSubmited = (By.CSS_SELECTOR, "#output>div")


class TextBoxPage:

    def __init__(self, driver):
        self.driver = driver


    def completeAllTheForm(self, name, email, currAdd, perAdd):
        self.driver.find_element(*TextBoxLocators.name).send_keys(name)
        self.driver.find_element(*TextBoxLocators.email).send_keys(email)
        self.driver.find_element(*TextBoxLocators.currAdd).send_keys(currAdd)
        self.driver.find_element(*TextBoxLocators.perAdd).send_keys(perAdd)
        time.sleep(2)
        self.driver.find_element(*TextBoxLocators.btnSubmit).click()

    def getAllDataSumbited(self):
        return self.driver.find_element(*TextBoxLocators.dataSubmited).text





