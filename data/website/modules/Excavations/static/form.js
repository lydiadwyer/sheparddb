"use strict";

// function to check for alphabetic letters
function isAlpha(xStr){
    var regEx = /^[a-zA-Z ]+$/;
    return xStr.match(regEx);
}
function verify_city() {

    // flag for any value errors
    var form_is_valid = true;

    // retrieve the form values
    var city_name = document.getElementById('city_name').value;
    var city_name_msg = document.getElementById("city_name_msg");

    // clear out the error message
    city_name_msg.innerHTML = "";

    // ensure country_name is not null
    if(!city_name || "" == city_name) {
        city_name_msg.innerHTML = "Please fill in the city name.";
        form_is_valid = false;
    }

    // ensure city_name is longer than 3 characters
    if(!city_name_msg.innerHTML && city_name.length < 3) {
        city_name_msg.innerHTML = "Please fill in the city name completely.";
        form_is_valid = false;
    }

    // ensure city_name is less than 128 characters
    if(!city_name_msg.innerHTML && city_name.length > 128) {
        city_name_msg.innerHTML = "Please fill in a shorter city name.";
        form_is_valid = false;
    }

    // character check for city_name
    if(!city_name_msg.innerHTML && !isAlpha(city_name)) {
        city_name_msg.innerHTML = "Please fill in a city name only with English letters.";
        form_is_valid = false;
    }


    return form_is_valid;
}