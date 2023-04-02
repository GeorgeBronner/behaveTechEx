from selenium.webdriver.common.by import By

from Tools import configReader

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def select(self, locator):
        if str(locator).endswith("_XPATH"):
            return self.driver.find_element(By.XPATH, configReader.readConfig("locators", locator))
        elif str(locator).endswith("_CSS"):
            return self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("locators", locator))
        elif str(locator).endswith("_ID"):
            return self.driver.find_element(By.ID, configReader.readConfig("locators", locator))
        elif str(locator).endswith("_CLASS"):
            return self.driver.find_element(By.CLASS_NAME, configReader.readConfig("locators", locator))
        elif str(locator).endswith("_NAME"):
            return self.driver.find_element(By.NAME, configReader.readConfig("locators", locator))

    def selectText(self, locator):
        return self.select(locator).text

    def click(self, locator):
        return self.select(locator).click()

    def type(self, locator, value):
        return self.select(locator).send_keys(value)

    def isDisplayed(self, locator):
        return self.select(locator).is_displayed()