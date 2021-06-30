Feature: Buying products

  Scenario: add and delete goods in the cart
    Given open Main page
    And categories: Phones, Laptops, Monitors are displayed
    When click on category Laptops
    And click on notebook Sony vaio i5
    Then Sony vaio i5 is displayed
    When click on Add to cart
    And accept pop up information
    And go to the cart
    Then Sony vaio i5 in the cart
    When go back to the main page
    And click on category Laptops
    And click on notebook Dell i7 8gb
    Then Dell i7 8gb is displayed
    When click on Add to cart
    And accept pop up information
    And go to the cart
    Then notebook Dell i7 8gb and Sony vaio i5 in the cart
    When delete Dell i7 8gb from the cart
    Then Sony vaio i5 in the cart

  Scenario: Checkout the order
    Given Sony vaio i5 in the cart
    When click place Order button
    Then place order is displayed
    When fill in all the fields by random data
    And click Purchase button
    And take screen and log purchase Id and Amount
    Then Amount and price is equal
    When click OK
    Then Main Page is opened
    When go to the cart
    Then cart is empty
