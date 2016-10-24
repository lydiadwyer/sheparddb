Feature: Region, Add

  Users's shoud be able to add Regions

Scenario: 6a7b, Region Add failure, "Burgundy" region_name, "" country_id
  Given I go to "http://127.0.0.1:8080/regions/add"
  When I fill in "region_name" with "Burgundy"
   And I fill in "country_id" with ""
   And I press "submit"
  Then The element with id of "country_id_msg" contains "Please choose the country."

Scenario: 6a7c, Region Add failure, "Burgundy" region_name, -1 country_id
  Given I go to "http://127.0.0.1:8080/regions/add"
  When I fill in "region_name" with "Burgundy"
   And I fill in "country_id" with "-1"
   And I press "submit"
  Then The element with id of "country_id_msg" contains "Please choose a valid country id."

Scenario: 6a7d, Region Add failure, "Burgundy" region_name, "aaz" country_id
  Given I go to "http://127.0.0.1:8080/regions/add"
  When I fill in "region_name" with "Burgundy"
   And I fill in "country_id" with "aaz"
   And I press "submit"
  Then The element with id of "country_id_msg" contains "Please choose a valid country id."

Scenario: 6a7e, Region Add failure, "Burgundy" region_name, "a" country_id
  Given I go to "http://127.0.0.1:8080/regions/add"
  When I fill in "region_name" with "Burgundy"
   And I fill in "country_id" with "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
   And I press "submit"
  Then The element with id of "country_id_msg" contains "Please choose a valid country id."

Scenario: 6a7f, Region Add failure, "Burgundy" region_name, "a!@#$%^&*()-=☺" country_id
  Given I go to "http://127.0.0.1:8080/regions/add"
  When I fill in "region_name" with "Burgundy"
   And I fill in "country_id" with "a!@#$%^&*()-=☺"
   And I press "submit"
  Then The element with id of "country_id_msg" contains "Please choose a valid country id."



Scenario: 6b7a, Region Add failure, "El" region_name, "4" country_id
  Given I go to "http://127.0.0.1:8080/regions/add"
  When I fill in "region_name" with "El"
   And I fill in "country_id" with "4"
   And I press "submit"
  Then The element with id of "region_name_msg" contains "Please fill in the region name completely."

Scenario: 6b7b, Region Add failure, 128+ letter region_name, "" country_id
  Given I go to "http://127.0.0.1:8080/regions/add"
  When I fill in "region_name" with "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"
   And I fill in "country_id" with ""
   And I press "submit"
  Then The element with id of "region_name_msg" contains "Please fill in a shorter region name."
   And The element with id of "country_id_msg" contains "Please choose the country."

Scenario: 6b7c, Region Add failure, 128+ number region_name, 1 country_id
  Given I go to "http://127.0.0.1:8080/regions/add"
  When I fill in "region_name" with "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
   And I fill in "country_id" with "1"
   And I press "submit"
  Then The element with id of "region_name_msg" contains "Please fill in a region name only with English letters."
  

Scenario: 6b7d, Region Add failure, "2345678" region_name, "aaz" country_id
  Given I go to "http://127.0.0.1:8080/regions/add"
  When I fill in "region_name" with "2345678"
   And I fill in "country_id" with "aaz"
   And I press "submit"
  Then The element with id of "region_name_msg" contains "Please fill in a region name only with English letters."
   And The element with id of "country_id_msg" contains "Please choose a valid country id."

Scenario: 6b7e, Region Add failure, "12" region_name, "a" country_id
  Given I go to "http://127.0.0.1:8080/regions/add"
  When I fill in "region_name" with "12"
   And I fill in "country_id" with "a"
   And I press "submit"
  Then The element with id of "region_name_msg" contains "Please fill in a region name only with English letters."
   And The element with id of "country_id_msg" contains "Please choose a valid country id."

Scenario: 6b7f, Region Add failure, "" region_name, "a!@#$%^&*()-=☺" country_id
  Given I go to "http://127.0.0.1:8080/regions/add"
  When I fill in "region_name" with ""
   And I fill in "country_id" with "a!@#$%^&*()-=☺"
   And I press "submit"
  Then The element with id of "region_name_msg" contains "Please fill in the region name."
   And The element with id of "country_id_msg" contains "Please choose a valid country id."



Scenario: Region Add failure, (null) region_name, (null) country_id
  Given I go to "http://127.0.0.1:8080/regions/add"
  When I press "submit"
  Then The element with id of "region_name_msg" contains "Please fill in the region name."
   And The element with id of "country_id_msg" contains "Please choose a country."
