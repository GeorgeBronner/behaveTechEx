from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('launch chrome browse')
def step_impl(context):
    context.driver=webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver\chromedriver.exe")
    context.driver.implicitly_wait(5)
    

@when('open orange hrm homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

@then('verify that the logo is present on Page')
def step_impl(context):
    status = context.driver.find_element(By.CLASS_NAME, "orangehrm-login-logo").is_displayed()
    assert status

@then(u'verify Orange is in the Title')
def step_impl(context):
    assert 'Orange' in context.driver.title

@then('close browser')
def step_impl(context):
    context.driver.close()