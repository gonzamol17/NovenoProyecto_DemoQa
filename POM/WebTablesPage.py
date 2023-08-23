import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class WebTablesLocators:
    searchBox = (By.ID, "searchBox")
    resultNoRows = (By.CSS_SELECTOR, "#app div.-striped.-highlight>div.rt-noData")
    addButton = (By.ID, "addNewRecordButton")
    firstnameLabel = (By.ID, "firstName")
    lastnameLabel = (By.ID, "lastName")
    emailLabel = (By.ID, "userEmail")
    ageLabel = (By.ID, "age")
    salaryLabel = (By.ID, "salary")
    departmentLabel = (By.ID, "department")
    submitButton = (By.ID, "submit")
    allEmployee = (By.CSS_SELECTOR, "div.body-height div.rt-td:nth-child(1)")
    glassIcon = (By.ID, "basic-addon2")


class WebTablesPage:

    def __init__(self, driver):
        self.driver = driver

    def makeASearch(self, name):
        self.driver.find_element(*WebTablesLocators.searchBox).clear()
        self.driver.find_element(*WebTablesLocators.searchBox).send_keys(name)

    def getZeroResult(self):
        return self.driver.find_element(*WebTablesLocators.resultNoRows).text

    def selectAddButton(self):
        self.driver.find_element(*WebTablesLocators.addButton).click()

    def completeForm(self, fname, lname, email, age, salary, department):
        self.driver.find_element(*WebTablesLocators.firstnameLabel).send_keys(fname)
        self.driver.find_element(*WebTablesLocators.lastnameLabel).send_keys(lname)
        self.driver.find_element(*WebTablesLocators.emailLabel).send_keys(email)
        self.driver.find_element(*WebTablesLocators.ageLabel).send_keys(age)
        self.driver.find_element(*WebTablesLocators.salaryLabel).send_keys(salary)
        self.driver.find_element(*WebTablesLocators.departmentLabel).send_keys(department)
        time.sleep(2)
        self.driver.find_element(*WebTablesLocators.submitButton).click()

    def getAllEmployees(self):
        self.driver.find_element(*WebTablesLocators.searchBox).click()
        time.sleep(2)
        self.driver.find_element(*WebTablesLocators.searchBox).clear()
        time.sleep(2)
        self.driver.find_element(*WebTablesLocators.searchBox).send_keys("a")
        time.sleep(2)
        employees = self.driver.find_elements(*WebTablesLocators.allEmployee)
        employeesList = []
        for employee in employees:
            if employee.text != " ":
                employeesList.append(employee.text)
        return employeesList

    def editUserFromTable(self, name):
        employees = self.driver.find_elements(*WebTablesLocators.allEmployee)
        n = 1
        for employee in employees:
            if employee.text != " " and employee.text == name:
                print(employee.text)
                self.driver.find_element(By.ID, "edit-record-"+str(n)+"").click()
                n = n+1
            else:
                n = n+1

    def updateAgeField(self, age):
        self.driver.find_element(*WebTablesLocators.ageLabel).clear()
        time.sleep(2)
        self.driver.find_element(*WebTablesLocators.ageLabel).send_keys(age)
        time.sleep(2)
        self.driver.find_element(*WebTablesLocators.submitButton).click()

    def verifyTheAgeWasUpdated(self, name):
        employees = self.driver.find_elements(*WebTablesLocators.allEmployee)
        n = 1
        for employee in employees:
            if employee.text != " " and employee.text == name:
                return self.driver.find_element(By.CSS_SELECTOR, "div.rt-tbody>div:nth-child(" + str(n) + ")>div>div:nth-child(3)").text

            else:
                n = n + 1
