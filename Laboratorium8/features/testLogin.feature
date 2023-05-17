Feature: Test login

  Scenario: Testing login error messages
    Given launch firefox browser
    When open saucedemo homepage
    Then test 1 - logging without login and password
    Then test 2 - logging with wrong username
    Then test 3 - logging with incorrect username and password
    Then test 4 - logging without username and incorrect password
    Then test 5 - logging with correct username and without password
    Then test 6 - logging with correct username and wrong password
    Then test 7 - logging with incorrect username and correct password
    Then test 8 - logging with correct username and correct password
    Then logout back to homepage
    And close firefox browser