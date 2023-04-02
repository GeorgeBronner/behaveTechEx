from behave import *
from selenium.common.exceptions import NoSuchElementException

@when('Enter username "{username}" and password "{password}"')
def step_impl(context,username,password):
    context.reg.setUsername(username)
    context.reg.setPassword(password)

@when('Click on login button')
def step_impl(context):
    context.reg.loginClick()

@then('User is successfully logged into the Dashboard')
def step_impl(context):
    try:
        text = context.reg.selectText("dashboard_XPATH")
    except NoSuchElementException:
        assert False, "Test Failed"
    if text == 'Dashboard':
        assert True, "Test Passed"

@then('User is not successfully logged into the Dashboard')
def step_impl(context):
    try:
        text = context.reg.selectText("login_fail_XPATH")
    except NoSuchElementException:
        assert False, "Test Failed"
    if text == 'Invalid credentials':
        assert True, "Test Passed"
    else:
        assert False, "Test Failed"