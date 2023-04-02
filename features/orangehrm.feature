Feature: OrangeHRM Logo

    Scenario: Title and Logo presence on Orange Home Page
        Given launch chrome browse
        When open orange hrm homepage 
        Then verify that the logo is present on Page
        Then verify Orange is in the Title

