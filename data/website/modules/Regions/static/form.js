"use strict";

// function to check for alphabetic letters
function isAlpha(xStr){
    var regEx = /^[a-zA-Z ]+$/;
    return xStr.match(regEx);
}
function verify_country() {

    // flag for any value errors
    var form_is_valid = true;

    // retrieve the form values
    var country_name = document.getElementById('country_name').value;
    var country_name_msg = document.getElementById("country_name_msg");

    // clear out the error message
    country_name_msg.innerHTML = "";

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


    // retrieve the value
    var country_abrev = document.getElementById('country_abrev').value;
    var country_abrev_msg = document.getElementById("country_abrev_msg");

    // clear out the error message
    country_abrev_msg.innerHTML = "";

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
    if(!country_abrev_msg.innerHTML && !isAlpha(country_abrev)) {
        country_abrev_msg.innerHTML = "Please fill in a country abbreviation with only English letters.";
        form_is_valid = false;
    }



    return form_is_valid;
}