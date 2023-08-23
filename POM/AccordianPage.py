import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class AccordianLocators:
    allTitles = (By.CSS_SELECTOR, ".card-header")
    firstParagraph = (By.CSS_SELECTOR, "#section1Content>p")
    secondTitle = (By.ID, "section2Heading")
    secondParagraph = (By.CSS_SELECTOR, "#section2Content>p")
    thirdTitle = (By.ID, "section3Heading")
    thirdParagraph = (By.CSS_SELECTOR, "#section3Content>p")
    firstTitle = (By.ID, "section1Heading")



class AccordianPage:

    def __init__(self, driver):
        self.driver = driver

    def getParagraphs(self):
        aux = len(self.driver.find_elements(*AccordianLocators.allTitles))
        aux1 = self.driver.find_elements(*AccordianLocators.allTitles)
        titles = []
        cont = 1
        while aux >= 1:
            if cont == 1:
                titles.append(self.driver.find_element(*AccordianLocators.firstParagraph).text)
                aux = aux-1
                cont = cont+1
            elif cont == 2:
                self.driver.find_element(*AccordianLocators.firstTitle).click()
                time.sleep(2)
                self.driver.find_element(*AccordianLocators.secondTitle).click()
                time.sleep(2)
                titles.append(self.driver.find_element(*AccordianLocators.secondParagraph).text)
                aux = aux - 1
                cont = cont + 1
            else:
                self.driver.find_element(*AccordianLocators.secondTitle).click()
                time.sleep(2)
                self.driver.find_element(*AccordianLocators.thirdTitle).click()
                time.sleep(2)
                titles.append(self.driver.find_element(*AccordianLocators.thirdParagraph).text)
                aux = aux - 1
        return titles



