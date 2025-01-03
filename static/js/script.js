AOS.init({
  duration: 1000,
  once: true,
});
// Custom cursor
const cursor = document.querySelector(".custom-cursor");
document.addEventListener("mousemove", (e) => {
  cursor.style.left = e.clientX + "px";
  cursor.style.top = e.clientY + "px";
});
const backToTopButton = document.querySelector(".back-to-top");
window.addEventListener("scroll", () => {
  if (window.pageYOffset > 100) {
    backToTopButton.classList.add("show");
  } else {
    backToTopButton.classList.remove("show");
  }
});

backToTopButton.addEventListener("click", (e) => {
  e.preventDefault();
  window.scrollTo({ top: 0, behavior: "smooth" });
});
document.addEventListener("DOMContentLoaded", function () {
  const signupForm = document.getElementById("signupForm");
  const loginForm = document.getElementById("loginForm");
  const showLoginForm = document.getElementById("showLoginForm");
  const showSignupForm = document.getElementById("showSignupForm");
  const modalSteps = document.querySelectorAll(".modal-step");
  const stepContents = document.querySelectorAll(".step-content");
  const nextStepButtons = document.querySelectorAll(".next-step");
  const prevStepButtons = document.querySelectorAll(".prev-step");
  var signupStepForm = document.getElementById("signupStepForm");
  const actualLoginForm = document.getElementById("actual-login-form");

  showLoginForm.addEventListener("click", function (e) {
    e.preventDefault();
    signupForm.classList.remove("active");
    loginForm.classList.add("active");
  });

  showSignupForm.addEventListener("click", function (e) {
    e.preventDefault();
    loginForm.classList.remove("active");
    signupForm.classList.add("active");
  });

  function setActiveStep(step) {
    modalSteps.forEach((s) => s.classList.remove("active"));
    stepContents.forEach((c) => c.classList.remove("active"));
    modalSteps[step - 1].classList.add("active");
    stepContents[step - 1].classList.add("active");
  }

  modalSteps.forEach((step) => {
    step.addEventListener("click", function () {
      setActiveStep(parseInt(this.dataset.step));
    });
  });

  nextStepButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const currentStep = parseInt(this.closest(".step-content").dataset.step);
      setActiveStep(currentStep + 1);
    });
  });

  prevStepButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const currentStep = parseInt(this.closest(".step-content").dataset.step);
      setActiveStep(currentStep - 1);
    });
  });
  //i will use ajax here for authenticaiton
  signupStepForm.addEventListener("submit", function (e) {
    e.preventDefault();
    var email = signupStepForm.elements["signupEmail"].value;
    var password = signupStepForm.elements["signupPassword"].value;
    var password2 = signupStepForm.elements["signupPassword2"].value;
    var firstname = signupStepForm.elements["firstName"].value;
    var lastname = signupStepForm.elements["lastName"].value;
    var phone = signupStepForm.elements["phone"].value;
    $.ajax({
      url: "register/", // Replace with your Django view URL
      type: "POST",
      data: {
        password: password,
        password2: password2,
        email: email,
        firstname: firstname,
        lastname: lastname,
        phone: phone,
        csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(), // Include CSRF token
      },
      success: function (response) {
        if (response.redirect) {
          alert(response.message);
          window.location.href = response.redirect;
        } else {
          alert("User creation failed. Try again");
        }
      },
      error: function (xhr, status, error) {
        console.log("Error:", error); // Handle any errors
      },
    });
  });
  //i will use ajax here for authenticaiton
  actualLoginForm.addEventListener("submit", function (e) {
    e.preventDefault();
    // Here you would typically send the form data to your server
    var email = actualLoginForm.elements["email"].value;
    var password = actualLoginForm.elements["password"].value;
    $.ajax({
      url: "/", // Replace with your Django view URL
      type: "POST",
      data: {
        password: password,
        email: email,
        csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(), // Include CSRF token
      },
      success: function (response) {
        if (response.redirect) {
          alert(response.message);
          window.location.href = response.redirect;
        } else {
          alert("Invalid credentials");
        }
      },
      error: function (xhr, status, error) {
        console.log("Error:", error); // Handle any errors
      },
    });
  });
});
