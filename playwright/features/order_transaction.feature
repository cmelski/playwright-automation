Feature: Order Transaction
  Tests related to order transactions

  Scenario Outline: Verify order success message shown in order details page
    Given order is placed using a <user_email> and <password>
    And the user is on landing page
    When I log into portal with <user_email> and <password>
    And navigate to orders page
    And select the order ID
    Then order message is successfully displayed
    Examples:
      | user_email            | password    |
      | c_melski@yahoo.com    | bestDAY2011 |