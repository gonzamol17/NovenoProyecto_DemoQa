import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class LinksLocators:
    simpleLink = (By.CSS_SELECTOR, "#simpleLink")
    unauthorizedLink = (By.ID, "unauthorized")
    messageUnauthorized = (By.ID, "linkResponse")


class LinksPage:

    def __init__(self, driver):
        self.driver = driver

    def selectSimpleLink(self):
        self.driver.find_element(*LinksLocators.simpleLink).click()

    def switchBetweenMoreThanOneTabs(self):
        windows = self.driver.window_handles
        print("\nLos Id's de las ventanas abiertas son: " + str(windows))
        long = len(windows)
        print("La cantidad de ventanas abiertas son: " + str(long))
        aux = long - 1
        n = 1
        urls = []
        while aux != 0:
            self.driver.switch_to.window(self.driver.window_handles[n])
            print("La url de la tab " + str(n + 1) + " es: " + self.driver.current_url)
            print("El título de tab " + str(n + 1) + " es: " + self.driver.title)
            n = n - 1
            aux = aux - 1
            time.sleep(2)
            urls.append(self.driver.current_url)
            self.driver.close()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[n])
        print("Ahora La url de la tab " + str(n + 1) + " es: " + self.driver.current_url)
        print("Y el título de tab " + str(n + 1) + " es: " + self.driver.title)
        urls.append(self.driver.current_url)
        return urls


    def verifyBrokenLink(self):
        self.driver.find_element(*LinksLocators.unauthorizedLink).click()
        return self.driver.find_element(*LinksLocators.messageUnauthorized).text

