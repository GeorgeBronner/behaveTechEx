from behave import *
from selenium.webdriver.common.by import By
from features.pageobjects.LoginPage import LoginPage
from Tools import configReader

@given('launch chrome browse')
def step_impl(context):
    context.reg = LoginPage(context.driver)
    context.driver.implicitly_wait(5)

@when('open orange hrm homepage')
def step_impl(context):
    context.reg.open(configReader.readConfig("basic info", "testsiteurl"))

@then('verify that the logo is present on Page')
def step_impl(context):
    status = context.reg.isDisplayed("logo_CLASS")
    assert status

@then(u'verify Orange is in the Title')
def step_impl(context):
    assert 'Orange' in context.reg.title