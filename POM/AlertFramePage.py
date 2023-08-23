import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class AlertFrameLocators:
    newTabBtn = (By.ID, "tabButton")
    newWindowBtn = (By.ID, "windowButton")
    newWindowMsgBtn = (By.ID, "messageWindowButton")
    titleNewPage = (By.CSS_SELECTOR, "#sampleHeading")
    titlePage = (By.CSS_SELECTOR, "#app div.pattern-backgound.playgound-header>div")


class AlertFramePage:

    def __init__(self, driver):
        self.driver = driver

    def selectNewTabBtn(self):
        self.driver.find_element(*AlertFrameLocators.newTabBtn).click()

    def getTitleNewPage(self):
        return self.driver.find_element(*AlertFrameLocators.titleNewPage).text

    def getTitleOldPage(self):
        return self.driver.find_element(*AlertFrameLocators.titlePage).text

    def handleWindows(self):
        windows = self.driver.window_handles
        print("Los Id's de las ventanas abiertas son: " + str(windows))
        long = len(windows)
        print("La cantidad de ventanas abiertas es: " + str(long))
        aux = long - 1
        n = 2
        while aux >= 1:
            self.driver.switch_to.window(self.driver.window_handles[aux])
            print("La url de la tab " + str(aux+1) + " es: " + self.driver.current_url)
            print("El título de tab " + str(aux+1) + " es: " + self.getTitleNewPage())
            aux = aux - 1
            time.sleep(2)
            self.driver.close()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[aux])
        print("La url de la tab " + str(aux+1) + " es: " + self.driver.current_url)
        print("El título de tab " + str(aux+1) + " es: " + self.getTitleOldPage())

    def selectNewWindowBtn(self):
        self.driver.find_element(*AlertFrameLocators.newWindowBtn).click()

    def selectNewWidowsMsgBtn(self):
        self.driver.find_element(*AlertFrameLocators.newWindowMsgBtn).click()


