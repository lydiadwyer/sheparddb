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
	a. I see the input called "country_name"
	b. I see the button called "Submit"
6. I fill in the input "country_name"
	a. I fill in "Greece"
	b. I fill in ""
	c. I fill in -1
  d. I fill in "Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" (33 chars)
  e. I fill in "a"
  f. I fill in "a!@#$%^&*()-=☺" (weird chars)
7. I click "Submit"
  a. I am forwarded
  b. I see an error message, for "country_name"
  c. I see an error message, for "country_name"
  d. I am forwarded, the country name is truncated to 32 chars
  e. I see an error message, for "country_name"
  f. I see an error message, for "country_name"
8. I am forwarded to the new country page, at "/artifacts/country/view/15"
  a. I see the page title set to "Greece"
  b. I see the "edit" link
  c. I see the "delete" link

## Post Conditions

1. I can see the new country listed on the "All Countries" page
2. I can choose the new country from a drop-down on the "Add Artifact" page
