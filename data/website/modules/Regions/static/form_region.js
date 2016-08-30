"use strict";

// javascript form verification for regions
// function to check for alphabetic letters
function isAlpha(xStr){
    var regEx = /^[a-zA-Z ]+$/;
    return xStr.match(regEx);
}
function verify_region() {

    // flag for any value errors
    var form_is_valid = true;

    // retrieve the form values
    var region_name = document.getElementById('region_name').value;
    var country_id = document.getElementById('country_id').value;
    var region_name_msg = document.getElementById("region_name_msg");
    var country_id_msg = document.getElementById("country_id_msg");

    // clear out the error message
    region_name_msg.innerHTML = "";
    country_id_msg.innerHTML = "";

    // ensure region_name is not null
    if(!region_name || "" == region_name) {
        region_name_msg.innerHTML = "Please fill in the region name.";
        form_is_valid = false;
    }

    // ensure region_name is longer than 3 characters
    if(!region_name_msg.innerHTML && region_name.length < 4) {
        region_name_msg.innerHTML = "Please fill in the region name completely.";
        form_is_valid = false;
    }

    // ensure region_name is less than 128 characters
    if(!region_name_msg.innerHTML && region_name.length > 127) {
        region_name_msg.innerHTML = "Please fill in a shorter region name.";
        form_is_valid = false;
    }

    // character check for region_name
    if(!region_name_msg.innerHTML && !isAlpha(region_name)) {
        region_name_msg.innerHTML = "Please fill in a region name only with English letters.";
        form_is_valid = false;
    }

    // ensure country_id is not null
    if(!country_id || "" == country_id) {
        country_id_msg.innerHTML = "Please choose the country.";
        form_is_valid = false;
    }


    return form_is_valid;
}