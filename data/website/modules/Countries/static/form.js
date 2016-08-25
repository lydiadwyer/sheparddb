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
    var region_name_msg = document.getElementById("region_name_msg");

    // clear out the error message
    region_name_msg.innerHTML = "";

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


    return form_is_valid;
}