Feature: OrangeHRM Login

    Scenario: Login to OrangeHRM with valid parameters
        Given launch chrome browse
        When open orange hrm homepage 
        And Enter username "admin" and password "admin123"
        And Click on login button
        Then User is successfully logged into the Dashboard