import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class FormsLocators:
    practiceFormItem = (By.XPATH, "//span[contains(text(),'Practice Form')]")
    firstNameLabel = (By.ID, "firstName")
    lastNameLabel = (By.ID, "lastName")
    emailLabel = (By.ID, "userEmail")
    genderRadioBtn = (By.XPATH, "//input[@type='radio']")
    mobileLabel = (By.ID, "userNumber")
    dateOfBirth = (By.ID, "dateOfBirthInput")
    yearBirdDropdown = (By.CSS_SELECTOR, "#dateOfBirth div.react-datepicker__year-dropdown-container select")
    monthBirdDropdown = (By.CSS_SELECTOR, "#dateOfBirth div.react-datepicker__month-dropdown-container select")
    dayBird = (By.CSS_SELECTOR, "#dateOfBirth div.react-datepicker__month")
    alldays = (By.CSS_SELECTOR, "#dateOfBirth div.react-datepicker__day")
    subjectLabel = (By.CSS_SELECTOR, "#subjectsContainer div.subjects-auto-complete__multi-value__label")
    checkboxesHobbies = (By.XPATH, "//label[contains(text(),'Sports')]")
    dropdownState = (By.CSS_SELECTOR, "#state > div > div.css-1wy0on6")
    stateList = (By.CSS_SELECTOR, "#state > div.css-26l3qy-menu > div")



class FormsPage:

    def __init__(self, driver):
        self.driver = driver

    def clickPracticeFormItem(self):
        self.driver.find_element(*FormsLocators.practiceFormItem).click()

    def completeForm(self, name, lname, email, gender, mobile, hobbie):
        self.driver.find_element(*FormsLocators.firstNameLabel).send_keys(name)
        self.driver.find_element(*FormsLocators.lastNameLabel).send_keys(lname)
        self.driver.find_element(*FormsLocators.emailLabel).send_keys(email)
        self.driver.find_element(By.XPATH, "//label[contains(text(), '" + str(gender) + "')]").click()
        self.driver.find_element(*FormsLocators.mobileLabel).send_keys(mobile)
        self.driver.find_element(By.XPATH, "//label[contains(text(), '" + hobbie + "')]").click()
        #self.driver.find_element(*FormsLocators.dropdownState).click()
        #select = Select(self.driver.find_element(*FormsLocators.stateList))
        #select.select_by_value(state)




