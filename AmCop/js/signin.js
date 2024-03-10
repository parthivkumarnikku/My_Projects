var loginForm = document.getElementById("login-form");
var ccioLoginForm = document.getElementById("CCIO-login-form");
var toggleBtn = document.getElementById("btn");

function CCIO_login() {
  loginForm.style.left = "-400px";
  ccioLoginForm.style.left = "50px";
  toggleBtn.style.left = "110px";
}

function login() {
  loginForm.style.left = "50px";
  ccioLoginForm.style.left = "450px";
  toggleBtn.style.left = "0";
}