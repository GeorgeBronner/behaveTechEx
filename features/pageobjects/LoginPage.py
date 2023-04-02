from features.pageobjects.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)


    def open(self,url):
        self.driver.get(url)

    def setUsername(self,username):
        self.type("username_NAME",username)

    def setPassword(self,password):
        self.type("password_NAME",password)

    def loginClick(self):
        self.click("login_button_CLASS")

