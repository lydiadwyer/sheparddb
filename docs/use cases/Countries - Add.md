# Countries - Add

## User Story

As an Archeologist, I want to have a list of countries and select them when saving an artifact, so that I can search for artifacts based on their country of excavation.

## Pre Conditions

- The database is reset
- (Must be a registered user, as an admin, and logged in.)

## Scenario, Alternative Paths, Failure

1. I go to the homepage, at "/"
	- I see a link with the text "Countries", in the menu
2. I click on the "Countries" link, in the menu
3. I go to the url: "/artifacts/countries"
4. I click the "Add" link
5. I go to the url: "/artifacts/countries/new"
	- I see the input called "country_name"
	- I see the button called "Submit"
6. I fill in the input "country_name"
  a. I fill in "Cyprus" (expected)
  b. I fill in "" (null)
  c. I fill in -1 (type mismatch)
  d. I fill in "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaz" (overflow)
  e. I fill in "a" (underflow)
  f. I fill in "This    is a multispace test" (excess internal whitespace)
  g. I fill in "a!@#$%^&*()-=☺" (weird chars)
  h. I fill in "<script>alert("hello!")</script>" (XSS)
  i. I fill in " onhover="alert('hello!')" " (XSS inline)
7. I fill in the input "country_abrev"
    a. I fill in "CY"
    b. I fill in "" (null)
    c. I fill in -1 (type mismatch)
    d. I fill in "aaz" (overflow)
    e. I fill in "a" (underflow)
    f. I fill in "a!@#$%^&*()-=☺" (weird chars)
8. I click "Submit"
    6a7a. I am forwarded
      7b. I see an error message, for "country_abrev"
      7c. I see an error message, for "country_abrev"
      7d. I see an error message, for "country_abrev"
      7e. I see an error message, for "country_abrev"
      7f. I see an error message, for "country_abrev"
    6b7a. I see an error message, for "country_name"
      7b. I see an error message, for "country_name", for "country_abrev"
      7c. I see an error message, for "country_name", for "country_abrev"
      7d. I see an error message, for "country_name", for "country_abrev"
      7e. I see an error message, for "country_name", for "country_abrev"
      7f. I see an error message, for "country_name", for "country_abrev"
    6c7a. I see an error message, for "country_name"
      7b. I see an error message, for "country_name", for "country_abrev"
      7c. I see an error message, for "country_name", for "country_abrev"
      7d. I see an error message, for "country_name", for "country_abrev"
      7e. I see an error message, for "country_name", for "country_abrev"
      7f. I see an error message, for "country_name", for "country_abrev"
    6d7a. I see an error message, for "country_name"
      7b. I see an error message, for "country_name", for "country_abrev"
      7c. I see an error message, for "country_name", for "country_abrev"
      7d. I see an error message, for "country_name", for "country_abrev"
      7e. I see an error message, for "country_name", for "country_abrev"
      7f. I see an error message, for "country_name", for "country_abrev"
    6e7a. I see an error message, for "country_name"
      7b. I see an error message, for "country_name", for "country_abrev"
      7c. I see an error message, for "country_name", for "country_abrev"
      7d. I see an error message, for "country_name", for "country_abrev"
      7e. I see an error message, for "country_name", for "country_abrev"
      7f. I see an error message, for "country_name", for "country_abrev"
    6f7a. I see an error message, for "country_name"
      7b. I see an error message, for "country_name", for "country_abrev"
      7c. I see an error message, for "country_name", for "country_abrev"
      7d. I see an error message, for "country_name", for "country_abrev"
      7e. I see an error message, for "country_name", for "country_abrev"
      7f. I see an error message, for "country_name", for "country_abrev"
9. I am forwarded to the new country page, at "/artifacts/countries/view/15"
    - 6a7a
    - I see the country name set to "Cyprus"
    - I see the country abbreviation set to "CY"
    - I see the "edit" link, with url "/countries/edit/4"
    - I see the "delete" link, with url "/countries/delete/4"

## Post Conditions

1. I can see the new country listed on the "All Countries" page
2. I can choose the new country from a drop-down on the "Add Artifact" page
