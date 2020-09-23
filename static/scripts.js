var schoolEmails = [
  "queensu.ca",
  "uottawa.ca",
  "uwo.ca",
  "ivey.ca",
  "edu.uwaterloo.ca"
];

var unsupportedEmails = {
  "cname.carleton.ca" : "Carleton University",
  "mail.utoronto.ca": "the University of Toronto",
  "student.ubc.ca": "the University of British Columbia"
};

function onSubmitForm(emailInputId) {
    return () => {
      let val = document.querySelector(emailInputId).value.split("@")[1].toLowerCase();
      if (schoolEmails.includes(val)) {
        return true;
      }
      else if (Object.keys(unsupportedEmails).includes(val)) {
        formVal = document.querySelector(emailInputId);
        formVal.setCustomValidity(`Sorry, Studyclub isn't open to ${unsupportedEmails[val]} yet!`);
        formVal.reportValidity();
        formVal.oninput = ()=>{
          document.querySelector(emailInputId).setCustomValidity("");
          document.querySelector(emailInputId).reportValidity();
        };
        return false;
      }
      else {
        formVal = document.querySelector(emailInputId);
        formVal.setCustomValidity("Please input your school email! (look below for which schools Studyclub is currently open to)");
        formVal.reportValidity();
        formVal.oninput = ()=>{
          document.querySelector(emailInputId).setCustomValidity("");
          document.querySelector(emailInputId).reportValidity();
        };
        return false;
      }
  }
}


document.addEventListener("DOMContentLoaded", () => {
  updateSize();

  document.querySelector("#email-form").onsubmit = onSubmitForm("#email-form-val");
  document.querySelector("#email-form2").onsubmit = onSubmitForm("#email-form-val2");

  $(window).on('resize', updateSize)

})

function updateSize() {
  if(window.innerWidth < 770) {
      document.querySelector("#wrapper").className = "flex-row";
  } else {
      document.querySelector("#wrapper").className = "row";
  }
}
