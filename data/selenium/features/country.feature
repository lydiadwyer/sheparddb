Feature: Country, Add

  Users's shoud be able to add Countries

Scenario: 6a7b, Country Add failure, "Cyprus" country_name, "" country_abrev
  Given I go to "http://127.0.0.1:8080/countries/add"
  When I fill in "country_name" with "Cyprus"
   And I press "submit"
  Then The element with id of "country_abrev_msg" contains "Please fill in the country abbreviation."

Scenario: 6a7c, Country Add failure, "Cyprus" country_name, -1 country_abrev
  Given I go to "http://127.0.0.1:8080/countries/add"
  When I fill in "country_name" with "Cyprus"
   And I fill in "country_abrev" with "-1"
   And I press "submit"
  Then The element with id of "country_abrev_msg" contains "Please fill in the country abbreviation using only uppercase letters."

Scenario: 6a7d, Country Add failure, "Cyprus" country_name, "aaz" country_abrev
  Given I go to "http://127.0.0.1:8080/countries/add"
  When I fill in "country_name" with "Cyprus"
   And I fill in "country_abrev" with "aaz"
   And I press "submit"
  Then The element with id of "country_abrev_msg" contains "Please fill in the country abbreviation with 2 characters."

Scenario: 6a7e, Country Add failure, "Cyprus" country_name, "a" country_abrev
  Given I go to "http://127.0.0.1:8080/countries/add"
  When I fill in "country_name" with "Cyprus"
   And I fill in "country_abrev" with "a"
   And I press "submit"
  Then The element with id of "country_abrev_msg" contains "Please fill in the country abbreviation with 2 characters."

Scenario: 6a7f, Country Add failure, "Cyprus" country_name, "a!@#$%^&*()-=☺" country_abrev
  Given I go to "http://127.0.0.1:8080/countries/add"
  When I fill in "country_name" with "Cyprus"
   And I fill in "country_abrev" with "a!@#$%^&*()-=☺"
   And I press "submit"
  Then The element with id of "country_abrev_msg" contains "Please fill in the country abbreviation with 2 characters."



Scenario: 6b7a, Country Add failure, "" country_name, "CY" country_abrev
  Given I go to "http://127.0.0.1:8080/countries/add"
  When I fill in "country_name" with ""
   And I fill in "country_abrev" with "CY"
   And I press "submit"
  Then The element with id of "country_name_msg" contains "Please fill in the country name."

Scenario: 6b7b, Country Add failure, "" country_name, "" country_abrev
  Given I go to "http://127.0.0.1:8080/countries/add"
  When I fill in "country_name" with ""
   And I fill in "country_abrev" with ""
   And I press "submit"
  Then The element with id of "country_name_msg" contains "Please fill in the country name."
   And The element with id of "country_abrev_msg" contains "Please fill in the country abbreviation."

Scenario: 6b7c, Country Add failure, "" country_name, -1 country_abrev
  Given I go to "http://127.0.0.1:8080/countries/add"
  When I fill in "country_name" with ""
   And I fill in "country_abrev" with "-1"
   And I press "submit"
  Then The element with id of "country_name_msg" contains "Please fill in the country name."
   And The element with id of "country_abrev_msg" contains "Please fill in the country abbreviation using only uppercase letters."

Scenario: 6b7d, Country Add failure, "" country_name, "aaz" country_abrev
  Given I go to "http://127.0.0.1:8080/countries/add"
  When I fill in "country_name" with ""
   And I fill in "country_abrev" with "aaz"
   And I press "submit"
  Then The element with id of "country_name_msg" contains "Please fill in the country name."
   And The element with id of "country_abrev_msg" contains "Please fill in the country abbreviation with 2 characters."

Scenario: 6b7e, Country Add failure, "" country_name, "a" country_abrev
  Given I go to "http://127.0.0.1:8080/countries/add"
  When I fill in "country_name" with ""
   And I fill in "country_abrev" with "a"
   And I press "submit"
  Then The element with id of "country_name_msg" contains "Please fill in the country name."
   And The element with id of "country_abrev_msg" contains "Please fill in the country abbreviation with 2 characters."

Scenario: 6b7f, Country Add failure, "" country_name, "a!@#$%^&*()-=☺" country_abrev
  Given I go to "http://127.0.0.1:8080/countries/add"
  When I fill in "country_name" with ""
   And I fill in "country_abrev" with "a!@#$%^&*()-=☺"
   And I press "submit"
  Then The element with id of "country_name_msg" contains "Please fill in the country name."
   And The element with id of "country_abrev_msg" contains "Please fill in the country abbreviation with 2 characters."



Scenario: Country Add failure, (null) country_name, (null) country_abrev
  Given I go to "http://127.0.0.1:8080/countries/add"
  When I press "submit"
  Then The element with id of "country_name_msg" contains "Please fill in the country name."
   And The element with id of "country_abrev_msg" contains "Please fill in the country abbreviation."
