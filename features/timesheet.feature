Feature: OrangeHRM TimeSheet

    Scenario: Open a timesheet
    Given A logged in user at the orange hrm Dashboard
    When clicks on Time in the NavMenu
    And clicks on view in the first Timesheets Pending Action
    Then the timesheet is displayed

