Feature: Region, Add

  Users's shoud be able to add Regions

Scenario: 6a7b, Region Add failure, "Burgundy" region_name, "" country_id
  Given I go to "http://127.0.0.1:8080/regions/add"
  When I fill in "region_name" with "Burgundy"
   And I press "submit"
  Then The element with id of "country_id_msg" contains "Please choose the country."

Scenario: 6a7c, Region Add failure, "Burgundy" region_name, -1 country_id
  Given I go to "http://127.0.0.1:8080/regions/add"
  When I fill in "region_name" with "Cyprus"
   And I fill in "country_id" with "-1"
   And I press "submit"
  Then The element with id of "country_id_msg" contains "Please choose the country."

Scenario: 6a7d, Region Add failure, "Burgundy" region_name, "aaz" country_id
  Given I go to "http://127.0.0.1:8080/regions/add"
  When I fill in "region_name" with "Cyprus"
   And I fill in "country_id" with "aaz"
   And I press "submit"
  Then The element with id of "country_id_msg" contains "Please choose the country."

Scenario: 6a7e, Region Add failure, "Burgundy" country_name, "a" country_abrev
  Given I go to "http://127.0.0.1:8080/regions/add"
  When I fill in "region_name" with "Cyprus"
   And I fill in "country_id" with "a"
   And I press "submit"
  Then The element with id of "country_abrev_msg" contains "Please choose the country abbreviation with 2 characters."

Scenario: 6a7f, Region Add failure, "Burgundy" country_name, "a!@#$%^&*()-=☺" country_abrev
  Given I go to "http://127.0.0.1:8080/regions/add"
  When I fill in "region_name" with "Cyprus"
   And I fill in "country_id" with "a!@#$%^&*()-=☺"
   And I press "submit"
  Then The element with id of "country_abrev_msg" contains "Please choose the country abbreviation with 2 characters."



Scenario: 6b7a, Region Add failure, "" country_name, "CY" country_abrev
  Given I go to "http://127.0.0.1:8080/regions/add"
  When I fill in "region_name" with ""
   And I fill in "country_id" with "CY"
   And I press "submit"
  Then The element with id of "country_name_msg" contains "Please choose the country name."

Scenario: 6b7b, Region Add failure, "" country_name, "" country_abrev
  Given I go to "http://127.0.0.1:8080/regions/add"
  When I fill in "region_name" with ""
   And I fill in "country_id" with ""
   And I press "submit"
  Then The element with id of "country_name_msg" contains "Please choose the country name."
   And The element with id of "country_abrev_msg" contains "Please fill in the country abbreviation."

Scenario: 6b7c, Region Add failure, "" country_name, -1 country_abrev
  Given I go to "http://127.0.0.1:8080/regions/add"
  When I fill in "country_name" with ""
   And I fill in "country_abrev" with "-1"
   And I press "submit"
  Then The element with id of "country_name_msg" contains "Please fill in the country name."
   And The element with id of "country_abrev_msg" contains "Please fill in the country abbreviation using only uppercase letters."

Scenario: 6b7d, Region Add failure, "" country_name, "aaz" country_abrev
  Given I go to "http://127.0.0.1:8080/regions/add"
  When I fill in "country_name" with ""
   And I fill in "country_abrev" with "aaz"
   And I press "submit"
  Then The element with id of "country_name_msg" contains "Please fill in the country name."
   And The element with id of "country_abrev_msg" contains "Please fill in the country abbreviation with 2 characters."

Scenario: 6b7e, Region Add failure, "" country_name, "a" country_abrev
  Given I go to "http://127.0.0.1:8080/regions/add"
  When I fill in "country_name" with ""
   And I fill in "country_abrev" with "a"
   And I press "submit"
  Then The element with id of "country_name_msg" contains "Please fill in the country name."
   And The element with id of "country_abrev_msg" contains "Please fill in the country abbreviation with 2 characters."

Scenario: 6b7f, Region Add failure, "" country_name, "a!@#$%^&*()-=☺" country_abrev
  Given I go to "http://127.0.0.1:8080/regions/add"
  When I fill in "country_name" with ""
   And I fill in "country_abrev" with "a!@#$%^&*()-=☺"
   And I press "submit"
  Then The element with id of "country_name_msg" contains "Please fill in the country name."
   And The element with id of "country_abrev_msg" contains "Please fill in the country abbreviation with 2 characters."



Scenario: Region Add failure, (null) country_name, (null) country_abrev
  Given I go to "http://127.0.0.1:8080/regions/add"
  When I press "submit"
  Then The element with id of "country_name_msg" contains "Please fill in the country name."
   And The element with id of "country_abrev_msg" contains "Please fill in the country abbreviation."
