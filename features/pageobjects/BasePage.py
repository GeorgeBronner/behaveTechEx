from selenium.webdriver.common.by import By

from Tools import configReader
import logging

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def select(self, locator):
        self.driver.find_element(By.CLASS_NAME, configReader.readConfig("locators", locator))

    def click(self, locator):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH, configReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_CSS"):
            self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_ID"):
            self.driver.find_element(By.ID, configReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_CLASS"):
            self.driver.find_element(By.CLASS_NAME, configReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_NAME"):
            self.driver.find_element(By.NAME, configReader.readConfig("locators", locator)).click()

    def type(self, locator, value):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH, configReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_CSS"):
            self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_ID"):
            self.driver.find_element(By.ID, configReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_CLASS"):
            self.driver.find_element(By.CLASS_NAME, configReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_NAME"):
            self.driver.find_element(By.NAME, configReader.readConfig("locators", locator)).click()
