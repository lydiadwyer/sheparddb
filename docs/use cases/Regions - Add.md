# Regions - Add

## User Story

As an Archeologist, I want to have a list of regions within countries and
select them when saving an artifact, so that I can search for artifacts
based on their region of excavation.

## Pre Conditions

- The database is reset
- Country "Cyprus" must exist
- (Must be a registered user, as an admin, and logged in.)

## Scenario, Alternative Paths, Failure

1. I go to the homepage, at "/"
	- I see a link with the text "Regions", in the menu
2. I click on the "Regions" link, in the menu
3. I go to the url: "/artifacts/regions"
4. I click the "Add" link
5. I go to the url: "/artifacts/regions/new"
    - I see the dropdown called "country_id"
    - I see the option "Cyprus" in the dropdown "country_id"
	- I see the input called "region_name"
	- I see the button called "Submit"
6. I fill in the dropdown "country_id"
    a. I select "Cyprus"
    b. I select nothing (use cookie default settings)
7. I fill in the input "region_name"
	a. I fill in "Dali"
	b. I fill in ""
	c. I fill in -1
    d. I fill in "Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" (33 chars)
    e. I fill in "a"
    f. I fill in "a!@#$%^&*()-=☺" (weird chars)
8. I click "Submit"
  6a7a. I am forwarded
    7b. I see an error message, for "region_name"
    7c. I see an error message, for "region_name"
    7d. I am forwarded, the region name is truncated to 64 chars
    7e. I see an error message, for "region_name"
    7f. I see an error message, for "region_name"
  6b7a. I see an error message, for "country_id"
    7b. I see an error message, for "country_id", for "region_name"
    7c. I see an error message, for "country_id", for "region_name"
    7d. I see an error message, for "country_id"
    7e. I see an error message, for "country_id", for "region_name"
    7f. I see an error message, for "country_id", for "region_name"
9. I am forwarded to the new country page, at "/artifacts/regions/view/15"
    6a7a, 6a7d
    - I see the page title set to "Dali"
    - I see the country set to "Cyprus"
    - I see the "edit" link
    - I see the "delete" link

## Post Conditions

1. I can see the new region listed on the "All Regions" page
2. I can choose the new region from the "regions" drop-down on the
    "Add Artifact" page
