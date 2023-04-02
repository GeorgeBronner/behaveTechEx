# A Python Behave based gherkin testing example.

## Organization:

### PageObjects

* BasePage.py - The base class for the page objects
* LoginPage.py - Builds on BasePage to allow login attempts
* TimePage.py - Builds on LoginPage to allow test time sheet page

### Features

* orangehrm.feature - tests the driver and loads the orangehrm webpage
* orangelogin.feature - tests successful logins and unsuccessful logins
* timesheets.feature - tests that a logged in user can access timesheets from the Nav Menu

### Other Notes

* Hardcoded information such as Xpaths, website url pulled from conf.ini.
* environment.py - handles webdriver and creates screenshots for failed tests (view in Allure) 


## How to Use Allure to view reports

* Run to create json reports:

behave -f allure_behave.formatter:AllureFormatter -o reports/ features

* Run for Allure to serve report is web browser:

allure serve reports
