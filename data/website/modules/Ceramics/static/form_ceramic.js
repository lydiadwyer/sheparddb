"use strict";

// javascript form verification for countries
// function to check for alphabetic letters
function isAlpha(xStr){
    var regEx = /^[a-zA-Z ]+$/;
    return xStr.match(regEx);
}
function isUpper(xStr){
    var regEx = /^[A-Z ]+$/;
    return xStr.match(regEx);
}
function verify_ceramic() {

    // flag for any value errors
    var form_is_valid = true;

    // retrieve the form values
    var ceramic_type = document.getElementById('ceramic_type').value;
    var ceramic_type_msg = document.getElementById("ceramic_type_msg");

    var ceramic_ware = document.getElementById('ceramic_ware').value;
    var ceramic_ware_msg = document.getElementById("ceramic_ware_msg");

    var ceramic_form = document.getElementById('ceramic_form').value;
    var ceramic_form_msg = document.getElementById("ceramic_form_msg");

    var ceramic_reg_id = document.getElementById('ceramic_reg_id').value;
    var ceramic_reg_id_msg = document.getElementById("ceramic_reg_id_msg");

    var date_period = document.getElementById('date_period').value;
    var date_period_msg = document.getElementById("date_period_msg");

    var excavated_from = document.getElementById('excavated_from').value;
    var excavated_from_msg = document.getElementById("excavated_from_msg");


    // clear out the error message
    country_name_msg.innerHTML = "";
    // clear out the error message
    country_abrev_msg.innerHTML = "";

    // ensure country_name is not null
    if(!country_name || "" == country_name) {
        country_name_msg.innerHTML = "Please fill in the country name.";
        form_is_valid = false;
    }

    // ensure country_name is longer than 3 characters
    if(!country_name_msg.innerHTML && country_name.length < 4) {
        country_name_msg.innerHTML = "Please fill in the country name completely.";
        form_is_valid = false;
    }

    // ensure country_name is less than 33 characters
    if(!country_name_msg.innerHTML && country_name.length > 32) {
        country_name_msg.innerHTML = "Please fill in a shorter country name.";
        form_is_valid = false;
    }

    // character check for country_name
    if(!country_name_msg.innerHTML && !isAlpha(country_name)) {
        country_name_msg.innerHTML = "Please fill in a country name only with English letters.";
        form_is_valid = false;
    }

    // Country abbreviation validation
    // ensure country_abrev is not null
    if(!country_abrev || "" == country_abrev) {
        country_abrev_msg.innerHTML = "Please fill in the country abbreviation.";
        form_is_valid = false;
    }

    // ensure country_abrev is 2 characters
    if(!country_abrev_msg.innerHTML && 2 !== country_abrev.length) {
        country_abrev_msg.innerHTML = "Please fill in the country abbreviation with 2 characters.";
        form_is_valid = false;
    }

    // character check for country_abrev
    if(!country_abrev_msg.innerHTML && !isUpper(country_abrev)) {
        country_abrev_msg.innerHTML = "Please fill in the country abbreviation using only uppercase letters.";
        form_is_valid = false;
    }


    return form_is_valid;
}