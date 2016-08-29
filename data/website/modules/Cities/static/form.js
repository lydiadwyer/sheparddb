"use strict";

// function to check for alphabetic letters
function isAlpha(xStr){
    var regEx = /^[a-zA-Z ]+$/;
    return xStr.match(regEx);
}
function verify_excavation() {

    // flag for any value errors
    var form_is_valid = true;

    // retrieve the form values
    var excavation_name = document.getElementById('excavation_name').value;
    var excavation_name_msg = document.getElementById("excavation_name_msg");

    // clear out the error message
    excavation_name_msg.innerHTML = "";

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
    if(!excavation_name_msg.innerHTML && !isAlpha(excavation_name)) {
        excavation_name_msg.innerHTML = "Please fill in an excavation name only with English letters.";
        form_is_valid = false;
    }


    return form_is_valid;
}