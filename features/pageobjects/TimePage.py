from features.pageobjects.LoginPage import LoginPage

class TimePage(LoginPage):

    def __init__(self,driver):
        super().__init__(driver)

    def timeClick(self):
        self.click("time_XPATH")

    def timeButtonClick(self):
        self.click("first_time_button_XPATH")

