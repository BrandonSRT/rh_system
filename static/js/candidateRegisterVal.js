const form = document.getElementById('needs-validation');
const name_cand = document.getElementById('name');
const identification = document.getElementById("identification");
const Nationality = document.getElementById("Nationality");
const Direction = document.getElementById("Direction");
const Phone = document.getElementById("Phone");
const email = document.getElementById("email");
const civil_status = document.getElementById("civil_status");
const spouse = document.getElementById("spouse");
const quantity = document.getElementById("quantity");
const peopledependecy = document.getElementById("peopledependecy");
const bloodtype = document.getElementById("bloodtype");
const license = document.getElementById("license");
const profession = document.getElementById("profession");
const salarypretension = document.getElementById("salarypretension");
const date = document.getElementById("date");
const studies = document.getElementById("studies");
const studies_other = document.getElementById("studies_other");
const illness = document.getElementById("illness");
const companyname = document.getElementById("companyname");
const phone2 = document.getElementById("phone2");
const job2 = document.getElementById("job2");
const finalsalary = document.getElementById("finalsalary");
const entrydate = document.getElementById("entrydate");
const departuredate = document.getElementById("departuredate");
const bossname = document.getElementById("bossname");
const reason = document.getElementById("reason");
const who = document.getElementById("who");


var mailformat = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
				

var validations =0;
form.addEventListener('submit', e => {
	
	checkInputs()
    if(validations !=27){
        e.preventDefault();
	
    }
	
	
});

function checkInputs() {
    validations=0;
	// trim to remove the whitespaces
	
	const name_candValue = name_cand.value.trim();
	const identificationValue = identification.value.trim();
	const NationalityValue = Nationality.value.trim();
	const DirectionValue = Direction.value.trim();
	const PhoneValue = Phone.value.trim();
	const emailValue = name_Client.value.trim();
	const civil_statusValue = name_Client.value.trim();
	const spouseValue = name_Client.value.trim();
	const quantityValue = name_Client.value.trim();
	const peopledependecyValue = name_Client.value.trim();
	const bloodtypeValue = name_Client.value.trim();
	const licenseValue = name_Client.value.trim();
	const professionValue = name_Client.value.trim();
	const salarypretensionValue = name_Client.value.trim();
	const dateValue = name_Client.value.trim();
	const studiesValue = name_Client.value.trim();
	const studies_otherValue = name_Client.value.trim();
	const illnessValue = name_Client.value.trim();
	const companynameValue = name_Client.value.trim();
	const phone2Value = name_Client.value.trim();
	const job2Value = name_Client.value.trim();
	const finalsalaryValue = name_Client.value.trim();
	const entrydateValue = name_Client.value.trim();
	const departuredateValue = name_Client.value.trim();
	const bossnameValue = name_Client.value.trim();
	const reasonValue = name_Client.value.trim();
	const whoValue = name_Client.value.trim();

	
	
	
	if(nameValue === '') {
		setErrorFor(name_Client, "Este campo es obligatorio");
	} else {
		setSuccessFor(name_Client);
		validations =validations+1
	}
	if(emailValue === '') {
		setErrorFor(email, "Este campo es obligatorio");
	}
	else {
		setSuccessFor(email);
		validations =validations+1
	}
	if(countryValue === '') {
		setErrorFor(country, "Este campo es obligatorio");
	} else {
		setSuccessFor(country);
		validations =validations+1
	}
	if(client_typeValue === '') {
		setErrorFor(client_type, "Este campo es obligatorio");
	} else {
		setSuccessFor(client_type);
		validations =validations+1
	}
	if(sellerValue === '') {
		setErrorFor(seller, "Este campo es obligatorio");
	} else {
		setSuccessFor(seller);
		validations =validations+1
	}
	
}

function setErrorFor(input, message) {
	const formControl = input.parentElement;
	const small = formControl.querySelector('small');
	formControl.className = 'form-control-validation error';
	small.innerText = message;

}

function setSuccessFor(input) {
	const formControl = input.parentElement;
	formControl.className = 'form-control-validation success';
}
	
