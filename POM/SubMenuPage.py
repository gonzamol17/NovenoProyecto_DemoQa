import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class SubMenuLocators:
    elementsItem = (By.CSS_SELECTOR, "#app div:nth-child(1)>div:nth-child(1) div.header-right")
    formsItem = (By.CSS_SELECTOR, "#app div:nth-child(1)>div:nth-child(2)>span div.header-right")
    alertsFrame = (By.CSS_SELECTOR, "#app div:nth-child(1)>div:nth-child(3)>span div.header-right")
    browserWindowLink = (By.XPATH, "//span[contains(text(),'Browser Windows')]")
    alertsLink = (By.XPATH, "//span[contains(text(), 'Alerts')]")
    framesLink = (By.XPATH, "//span[contains(text(), 'Frames')]")
    modalDialogsLink = (By.XPATH, "//span[contains(text(), 'Modal Dialogs')]")
    widgetsItem = (By.CSS_SELECTOR, "#app > div > div > div.row > div:nth-child(1) > div > div > div:nth-child(4) > span > div > div.header-right")
    accordianLink = (By.XPATH, "//span[contains(text(), 'Accordian')]")
    autocompleteLink = (By.XPATH, "//span[contains(text(), 'Auto Complete')]")
    datePickerLink = (By.XPATH, "//span[contains(text(), 'Date Picker')]")
    sliderLink = (By.XPATH, "//span[contains(text(), 'Slider')]")
    progressBarLink = (By.XPATH, "//span[contains(text(), 'Progress Bar')]")
    tabsLink = (By.XPATH, "//span[contains(text(), 'Tabs')]")
    toolTipsLink = (By.XPATH, "//span[contains(text(), 'Tool Tips')]")
    menuLink = (By.XPATH, "//span[contains(text(), 'Menu')]")
    selectMenuLink = (By.XPATH, "//span[contains(text(), 'Select Menu')]")
    interactionsItem = (By.CSS_SELECTOR, "#app div.row div:nth-child(5) > span > div")
    selectSortableLink = (By.XPATH, "//span[contains(text(), 'Sortable')]")
    selectSelectableLink = (By.XPATH, "//span[contains(text(), 'Selectable')]")
    selectResizableLink = (By.XPATH, "//span[contains(text(), 'Resizable')]")
    selectDroppableLink = (By.XPATH, "//span[contains(text(), 'Droppable')]")
    selectLoginLink = (By.XPATH, "//span[contains(text(), 'Login')]")


class SubMenuPage:

    def __init__(self, driver):
        self.driver = driver

    def collapseElementsItem(self):
        self.driver.find_element(*SubMenuLocators.elementsItem).click()

    def expandFormsItem(self):
        self.driver.find_element(*SubMenuLocators.formsItem).click()

    def expandAlertsFrameItem(self):
        self.driver.find_element(*SubMenuLocators.alertsFrame).click()

    def selectBrowserWindowLink(self):
        self.driver.find_element(*SubMenuLocators.browserWindowLink).click()

    def selectAlertsLink(self):
        self.driver.find_element(*SubMenuLocators.alertsLink).click()

    def selectFramesLink(self):
        self.driver.find_element(*SubMenuLocators.framesLink).click()

    def selectModalDialogsLink(self):
        self.driver.find_element(*SubMenuLocators.modalDialogsLink).click()

    def expandWidgetsItem(self):
        self.driver.find_element(*SubMenuLocators.widgetsItem).click()

    def selectAccordianLink(self):
        self.driver.find_element(*SubMenuLocators.accordianLink).click()

    def selectAutoCompleteLink(self):
        self.driver.find_element(*SubMenuLocators.autocompleteLink).click()

    def selectDatePickerLink(self):
        self.driver.find_element(*SubMenuLocators.datePickerLink).click()

    def selectSliderLink(self):
        self.driver.find_element(*SubMenuLocators.sliderLink).click()

    def selectProgressBarLink(self):
        self.driver.find_element(*SubMenuLocators.progressBarLink).click()

    def selectTabsLink(self):
        self.driver.find_element(*SubMenuLocators.tabsLink).click()

    def selectToolTipsLink(self):
        self.driver.find_element(*SubMenuLocators.toolTipsLink).click()

    def selectMenuLink(self):
        self.driver.find_element(*SubMenuLocators.menuLink).click()

    def selectSelectMenuLink(self):
        self.driver.find_element(*SubMenuLocators.selectMenuLink).click()

    def expandInteractionsItem(self):
        self.driver.find_element(*SubMenuLocators.interactionsItem).click()

    def selectSortableLink(self):
        self.driver.find_element(*SubMenuLocators.selectSortableLink).click()

    def selectSelectableLink(self):
        self.driver.find_element(*SubMenuLocators.selectSelectableLink).click()

    def selectResizableLink(self):
        self.driver.find_element(*SubMenuLocators.selectResizableLink).click()

    def selectDroppableLink(self):
        self.driver.find_element(*SubMenuLocators.selectDroppableLink).click()

    def selectLoginLink(self):
        self.driver.find_element(*SubMenuLocators.selectLoginLink).click()

