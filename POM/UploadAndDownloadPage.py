import os
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class UploadAndDownloadLocators:
    btnUpload = (By.ID, "uploadFile")
    messageUploaded = (By.CSS_SELECTOR, "#uploadedFilePath")
    btnDownload = (By.ID, "downloadButton")


class UploadAndDownloadPage:

    def __init__(self, driver):
        self.driver = driver

    def selectBtnUploadFile(self, path):
        self.driver.find_element(*UploadAndDownloadLocators.btnUpload).send_keys(path)

    def getMessageUploadFile(self):
        return self.driver.find_element(*UploadAndDownloadLocators.messageUploaded).text

    def selectBtnDownloadFile(self):
        self.driver.find_element(*UploadAndDownloadLocators.btnDownload).click()

    def verifyDownloadedFile(self):
        while not os.path.exists('C:\\Users\\admin\\Downloads'):
            time.sleep(3)
        # check file
        if os.path.isfile('C:\\Users\\admin\\Downloads\\sampleFile.jpeg'):
            time.sleep(2)
            print("File download is completed")
        else:
            time.sleep(2)
            print("File download is not completed")



