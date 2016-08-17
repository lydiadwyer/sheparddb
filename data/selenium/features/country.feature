Feature: Signup

  Users's shoud be able to save Countries

Scenario: Country Add failure, empty
  Given I go to "http://127.0.0.1:8080/countries/add"
  When I press "submit"
  Then The element with id of "country_name_msg" contains "Please fill in the country name completely."
   And The element with id of "country_abrev_msg" contains "Please fill in the country abbreviation with 2 characters."
   And I wait "2" seconds

Scenario: Country Add failure, empty
  Given I go to "http://127.0.0.1:8080/countries/add"
  When I fill in "country_name" with "Greece"
   And I press "submit"
  Then The element with id of "country_abrev_msg" contains "Please fill in the country abbreviation with 2 characters."
   And I wait "2" seconds