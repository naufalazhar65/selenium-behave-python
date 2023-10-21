Feature: Product Sorting

  @sort
  Scenario: Verify Name Z to A Sorting of Products
    Given the user is logged in
    When the user selects Name Z to A option from the product sort
    Then the products are sorted alphabetically from Z to A
