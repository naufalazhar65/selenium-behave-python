Feature: Product Sorting

  @sort
  Scenario: Verify Name Z to A Sorting of Products
    Given user is logged in
    When user selects Name Z to A option from the product sort
    Then products are sorted alphabetically from Z to A
