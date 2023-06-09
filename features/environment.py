import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from Tools import configReader

def before_scenario(context, scenario):
    if configReader.readConfig("basic info","browser") == "chrome":
        context.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    if configReader.readConfig("basic info","browser") == "firefox":
        context.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

def after_scenario(context, scenario):
    context.driver.quit()

def after_step(context, step):
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
