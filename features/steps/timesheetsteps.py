from behave import *
from features.pageobjects.TimePage import TimePage
from selenium.common.exceptions import NoSuchElementException
from Tools import configReader

@given(u'A logged in user at the orange hrm Dashboard')
def step_impl(context):
    context.reg = TimePage(context.driver)
    context.driver.implicitly_wait(5)
    context.reg.open(configReader.readConfig("basic info", "testsiteurl"))
    context.reg.setUsername("admin")
    context.reg.setPassword("admin123")
    context.reg.loginClick()

@when(u'clicks on Time in the NavMenu')
def step_impl(context):
    context.reg.timeClick()


@when(u'clicks on view in the first Timesheets Pending Action')
def step_impl(context):
    context.reg.timeButtonClick()

@then(u'the timesheet is displayed')
def step_impl(context):
    try:
        text = context.reg.selectText("timesheet_display_XPATH")
    except NoSuchElementException:
        assert False, "Test Failed"
    if text[:9] == 'Timesheet':
        assert True, "Test Passed"
    else:
        assert False, "Test Failed"