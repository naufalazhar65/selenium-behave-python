Feature: Testing Login Functionality

@logincase
@sanity
  Scenario Outline: User login with credentials
    Given user is on the login page
    When user enters <username> and <password>
    Then user is <expected_result>

    Examples:
      | username         | password        | expected_result         |
      | standard_user    | secret_sauce    | redirected to product page |
      | invalid_username | invalid_password | sees an error message  |


