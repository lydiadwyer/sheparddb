"use strict";

// function to check name is alphanumeric
function isAlphanumeric(xStr){
    var regEx = /^[a-zA-Z0-9 ]+$/;
    return xStr.match(regEx);
}
// function to check numbers
function isNumeric(n){
    return 0 === n % (!isNaN(parseInt(n, 10)) && 0 <= ~~n);
}
function verify_excavation() {

    // flag for any value errors
    var form_is_valid = true;

    // retrieve the form values
    var excavation_name = document.getElementById('excavation_name').value;
    var country_id = document.getElementById('country_id').value;
    var region_id = document.getElementById('region_id').value;
    var city_id = document.getElementById('city_id').value;
    var excavation_name_msg = document.getElementById("excavation_name_msg");
    var country_id_msg = document.getElementById("country_id_msg");
    var region_id_msg = document.getElementById("region_id_msg");
    var city_id_msg = document.getElementById("city_id_msg");


    // clear out the error message
    excavation_name_msg.innerHTML = "";
    country_id_msg.innerHTML = "";
    region_id_msg.innerHTML = "";
    city_id_msg.innerHTML = "";



    // ensure excavation_name is not null
    if(!excavation_name || "" == excavation_name) {
        excavation_name_msg.innerHTML = "Please fill in the excavation name.";
        form_is_valid = false;
    }

    // ensure excavation_name is longer than 1 characters
    if(!excavation_name_msg.innerHTML && excavation_name.length < 2) {
        excavation_name_msg.innerHTML = "Please fill in the excavation name completely.";
        form_is_valid = false;
    }

    // ensure excavation_name is less than 128 characters
    if(!excavation_name_msg.innerHTML && excavation_name.length > 128) {
        excavation_name_msg.innerHTML = "Please fill in a shorter excavation name.";
        form_is_valid = false;
    }

    // character check for excavation_name
    if(!excavation_name_msg.innerHTML && !isAlphanumeric(excavation_name)) {
        excavation_name_msg.innerHTML = "Please fill in an excavation name only with English letters and numbers.";
        form_is_valid = false;
    }

    // Ensure ids are not null, valid numbers, and positive

    // number check for countryid
    if(!country_id_msg.innerHTML && !isNumeric(country_id)) {
        country_id_msg.innerHTML = "Please choose a valid country.";
        form_is_valid = false;
    }

    // number check for region_id
    if(!region_id_msg.innerHTML && !isNumeric(region_id)) {
        region_id_msg.innerHTML = "Please choose a valid region.";
        form_is_valid = false;
    }

    // number check for city_id
    if(!city_id_msg.innerHTML && !isNumeric(city_id)) {
        city_id_msg.innerHTML = "Please choose a valid city.";
        form_is_valid = false;
    }




    return form_is_valid;
}