import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class SliderLocators:
    slider = (By.CSS_SELECTOR, "#sliderContainer>div.col-9>span>input")
    labelSlider = (By.CSS_SELECTOR, "#sliderContainer div.range-slider__tooltip__label")
    sliderValue = (By.ID, "sliderValue")



class SliderPage:

    def __init__(self, driver):
        self.driver = driver

    def moveSlider(self, value):
        action = ActionChains(self.driver)
        action.click_and_hold(self.driver.find_element(*SliderLocators.slider)).move_by_offset(-250, 0).perform()
        time.sleep(2)
        action.click_and_hold(self.driver.find_element(*SliderLocators.slider)).move_by_offset(value, 0).perform()


    def getNumberOfSlider(self):
        return self.driver.find_element(*SliderLocators.labelSlider).text

    def getSliderValue(self):
        return self.driver.find_element(*SliderLocators.sliderValue).get_attribute('value')








