"use strict";

// javascript form verification for countries
// function to check for alphabetic letters
function isAlpha(xStr){
    var regEx = /^[a-zA-Z ]+$/;
    return xStr.match(regEx);
}

function isNum(xStr){
    var regEx = /^[0-9 ]+$/;
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


    // clear out the error messages
    ceramic_type_msg.innerHTML = "";
    ceramic_ware_msg.innerHTML = "";
    ceramic_form_msg.innerHTML = "";
    ceramic_reg_id_msg.innerHTML = "";
    date_period_msg.innerHTML = "";
    excavated_from_msg.innerHTML = "";

    // Check all to make sure they are filled in
    // ensure ceramic_type is not null
    if(!ceramic_type || "" == ceramic_type) {
        ceramic_type_msg.innerHTML = "Please fill in the ceramic type.";
        form_is_valid = false;
    }
    // ensure ceramic_ware is not null
    if(!ceramic_ware || "" == ceramic_ware) {
        ceramic_ware_msg.innerHTML = "Please fill in the ceramic ware.";
        form_is_valid = false;
    }
    // ensure ceramic_form is not null
    if(!ceramic_form || "" == ceramic_form) {
        ceramic_form_msg.innerHTML = "Please fill in the ceramic form.";
        form_is_valid = false;
    }
    // ensure ceramic_reg_id is not null
    if(!ceramic_reg_id || "" == ceramic_reg_id) {
        ceramic_reg_id_msg.innerHTML = "Please fill in the ceramic registration id.";
        form_is_valid = false;
    }
    // ensure date_period is not null
    if(!date_period || "" == date_period) {
        date_period_msg.innerHTML = "Please fill in the era.";
        form_is_valid = false;
    }
    // ensure excavated_from is not null
    if(!excavated_from || "" == excavated_from) {
        excavated_from_msg.innerHTML = "Please fill in the excavation site.";
        form_is_valid = false;
    }

    // Check all to make sure they are not too long (less than 128 chars), and >0
    // Check that the right data are being input, strings or numbers

    // ensure ceramic_type is longer than 1 character
    if(!ceramic_type.innerHTML && ceramic_type.length < 2) {
        ceramic_type_msg.innerHTML = "Please fill in the ceramic type completely.";
        form_is_valid = false;
    }
    // ensure ceramic_type is less than 128 characters
    if(!ceramic_type_msg.innerHTML && ceramic_type.length > 128) {
        ceramic_type_msg.innerHTML = "Please fill in a shorter ceramic type name.";
        form_is_valid = false;
    }


    // character check for country_name
    if(!ceramic_type_msg.innerHTML && !isAlpha(ceramic_type)) {
        ceramic_type_msg.innerHTML = "Please fill in a ceramic type only with English letters.";
        form_is_valid = false;
    }


    return form_is_valid;
}