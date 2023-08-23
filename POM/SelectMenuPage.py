import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class SelectMenuLocators:
    item1 = (By.CSS_SELECTOR, "#withOptGroup > div > div.css-1wy0on6")
    item2 = (By.CSS_SELECTOR, "#selectOne > div > div.css-1wy0on6 > div")
    item3 = (By.ID, "oldSelectMenu")
    subitems3 = (By.CSS_SELECTOR, "#oldSelectMenu > option")
    dropdownCars = (By.ID, "cars")



class SelectMenuPage:

    def __init__(self, driver):
        self.driver = driver


    def selectItemDropdown1(self):
        self.driver.find_element(*SelectMenuLocators.item1).click()

    def selectValue1(self, text):
        self.driver.find_element(By.XPATH, "//div[contains(text(),'"+text+"')]").click()

    def selectItemDropdown2(self):
        self.driver.find_element(*SelectMenuLocators.item2).click()

    def selectValue2(self, text):
        self.driver.find_element(By.XPATH, "//div[contains(text(),'"+text+"')]").click()

    def selectItemDropdown3(self):
        self.driver.find_element(*SelectMenuLocators.item3).click()


    def selectColor(self, color):
        items = self.driver.find_elements(*SelectMenuLocators.subitems3)
        #dd = Select(*SelectMenuLocators.item3)
        i = 0
        print("Cantidad de elementos en el dropdrown :"+str(len(items)))
        for item in items:
            time.sleep(1)
            if item.text == color:
                item.click()
                print("Se encontró el color elegido")
                print(item.text)
                i = 1
        if i == 0:
            print("el valor buscado, no estaba en la lista del dropdown")


    def selectCars(self, car1, car2):
        ddc = Select(self.driver.find_element(*SelectMenuLocators.dropdownCars))
        ddc.select_by_visible_text(car1)
        ddc.select_by_visible_text(car2)
        time.sleep(2)
        ddc.deselect_all()












