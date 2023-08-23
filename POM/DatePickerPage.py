import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class DatePickerLocators:
    doubleClickBtn = (By.ID, "doubleClickBtn")
    selectDateField = (By.ID, "datePickerMonthYearInput")
    calendarYear = (By.CSS_SELECTOR, "#datePickerMonthYear div.react-datepicker__year-dropdown-container.react-datepicker__year-dropdown-container--select > select")
    calendarMonth = (By.CSS_SELECTOR, "#datePickerMonthYear div.react-datepicker__month-dropdown-container.react-datepicker__month-dropdown-container--select > select")
    calendarDay = (By.CSS_SELECTOR, "#datePickerMonthYear div>div>div.react-datepicker__month-container")
    calendarAllDays = (By.CSS_SELECTOR, "#datePickerMonthYear div.react-datepicker__day")
    daySelected = (By.CSS_SELECTOR, "#datePickerMonthYear div.react-datepicker__day.react-datepicker__day--")
    selectDateAndTime = (By.ID, "dateAndTimePickerInput")
    calendarDay2 = (By.CSS_SELECTOR, "#dateAndTimePicker div.react-datepicker__year-dropdown-container--scroll>div")
    selectYear2 = (By.CSS_SELECTOR, "#dateAndTimePicker div.react-datepicker__year-dropdown-container> div")
    getListYears2 = (By.CSS_SELECTOR, "#dateAndTimePicker div.react-datepicker__year-dropdown>div")
    getMonthYears = (By.CSS_SELECTOR, "#dateAndTimePicker div.react-datepicker__current-month--hasMonthDropdown")
    nextMonth = (By.XPATH, "//button[contains(text(),'Next Month')]")
    previousMonth = (By.XPATH, "//button[contains(text(),'Previous Month')]")
    increaseYear2 = (By.CSS_SELECTOR, "#dateAndTimePicker div:nth-child(1)>a")
    decreaseYear2 = (By.CSS_SELECTOR, "#dateAndTimePicker div:nth-child(13)>a")

#dateAndTimePicker div.react-datepicker__year-dropdown > div

class DatePickerPage:

    def __init__(self, driver):
        self.driver = driver

    def selectDate(self):
        self.driver.find_element(*DatePickerLocators.selectDateField).click()

    def selectYearMonthAndDay(self, year, month, day):
        select = Select(self.driver.find_element(*DatePickerLocators.calendarYear))
        select.select_by_value(year)
        time.sleep(2)
        select = Select(self.driver.find_element(*DatePickerLocators.calendarMonth))
        select.select_by_visible_text(month)
        time.sleep(2)
        dates = self.driver.find_elements(*DatePickerLocators.calendarAllDays)
        aux = int(day[0:3])
        for date in dates:
            if month in date.get_attribute('aria-label'):
                if aux > 10:
                    self.driver.find_element(By.CSS_SELECTOR,"#datePickerMonthYear div.react-datepicker__day.react-datepicker__day--" + str(day)).click()
                    return 1
                else:
                    self.driver.find_element(By.CSS_SELECTOR,"#datePickerMonthYear div.react-datepicker__day.react-datepicker__day--00" + str(aux)).click()
                    return 1
        return 0


    def showDateSelected(self):
        return self.driver.find_element(*DatePickerLocators.selectDateField).get_attribute('value')


    def selectDateAndTime(self):
        self.driver.find_element(*DatePickerLocators.selectDateAndTime).click()











