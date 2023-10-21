Feature: Testing Login Functionality

@logincase
@sanity
  Scenario Outline: User login with credentials
    Given the user is on the login page
    When the user enters <username> and <password>
    Then the user is <expected_result>

    Examples:
      | username         | password        | expected_result         |
      | standard_user    | secret_sauce    | redirected to product page |
      | invalid_username | invalid_password | sees an error message  |


