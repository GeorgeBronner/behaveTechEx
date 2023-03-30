from behave import *
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

@when('Enter username "{user}" and password "{password}"')
def step_impl(context,user,password):
    context.driver.find_element(By.NAME,"username").send_keys(user)
    context.driver.find_element(By.NAME,"password").send_keys(password)


@when('Click on login button')
def step_impl(context):
    context.driver.find_element(By.CLASS_NAME,"orangehrm-login-button").click()


@then('User is successfully logged into the Dashboard')
def step_impl(context):
    try:
        text = context.driver.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[1]/div[1]/span/h6").text
    except NoSuchElementException:
        context.driver.close()
        assert False, "Test Failed"
    if text == 'Dashboard':
        context.driver.close()
        assert True, "Test Passed"