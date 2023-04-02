Feature: OrangeHRM Login

    Scenario Outline: Login to OrangeHRM with good username and password
    Given launch chrome browse
    When open orange hrm homepage 
    And Enter username "<username>" and password "<password>"
    And Click on login button
    Then User is successfully logged into the Dashboard

        Examples:
            | username | password |
            | admin    | admin123 |

    Scenario Outline: Login to OrangeHRM with various bad usernames and passwords
        Given launch chrome browse
        When open orange hrm homepage 
        And Enter username "<username>" and password "<password>"
        And Click on login button
        Then User is not successfully logged into the Dashboard

        Examples:
            | username | password |
            | admin123 | admin    |
            | admin    | badpass  |
            | baduser  | admin123 |
