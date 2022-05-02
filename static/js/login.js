
const passwordField = document.querySelector('#password');
const showPasswordToggle = document.querySelector('.showPasswordToggle');

function handleToggleInput () {
    console.log("paso")
    if (showPasswordToggle.textContent === 'Mostrar') {
        showPasswordToggle.textContent = 'Ocultar';
        passwordField.setAttribute('type', 'text');

    } else {
        showPasswordToggle.textContent = "Mostrar";
        passwordField.setAttribute('type', 'password');
    }
};