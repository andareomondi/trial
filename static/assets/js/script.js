        AOS.init({
            duration: 1000,
            once: true
        });
                    // Theme toggling
        const themeToggle = document.querySelector('.theme-toggle');
        const html = document.documentElement;
        const themeIcon = themeToggle.querySelector('i');

        themeToggle.addEventListener('click', () => {
            const currentTheme = html.getAttribute('data-bs-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            html.setAttribute('data-bs-theme', newTheme);

            // Update icon
            themeIcon.className = newTheme === 'dark' ? 'bi bi-moon-fill' : 'bi bi-sun-fill';

            // Save preference
            localStorage.setItem('theme', newTheme);
        });

        // Check for saved theme preference
        const savedTheme = localStorage.getItem('theme');
        if (savedTheme) {
            html.setAttribute('data-bs-theme', savedTheme);
            themeIcon.className = savedTheme === 'dark' ? 'bi bi-moon-fill' : 'bi bi-sun-fill';
        };
        const toastTrigger = document.getElementById('liveToastBtn')
const toastLiveExample = document.getElementById('liveToast')

if (toastTrigger) {
  const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample)
  toastTrigger.addEventListener('click', () => {
    toastBootstrap.show()
  })
}
    document.addEventListener('DOMContentLoaded', function () {
        const signupForm = document.getElementById('signupForm');
        const loginForm = document.getElementById('loginForm');
        const showLoginForm = document.getElementById('showLoginForm');
        const showSignupForm = document.getElementById('showSignupForm');
        const modalSteps = document.querySelectorAll('.modal-step');
        const stepContents = document.querySelectorAll('.step-content');
        const nextStepButtons = document.querySelectorAll('.next-step');
        const prevStepButtons = document.querySelectorAll('.prev-step');
        const signupStepForm = document.getElementById('signupStepForm');

        showLoginForm.addEventListener('click', function (e) {
            e.preventDefault();
            signupForm.classList.remove('active');
            loginForm.classList.add('active');
        });

        showSignupForm.addEventListener('click', function (e) {
            e.preventDefault();
            loginForm.classList.remove('active');
            signupForm.classList.add('active');
        });

        function setActiveStep(step) {
            modalSteps.forEach(s => s.classList.remove('active'));
            stepContents.forEach(c => c.classList.remove('active'));
            modalSteps[step - 1].classList.add('active');
            stepContents[step - 1].classList.add('active');
        }

        modalSteps.forEach(step => {
            step.addEventListener('click', function () {
                setActiveStep(parseInt(this.dataset.step));
            });
        });

        nextStepButtons.forEach(button => {
            button.addEventListener('click', function () {
                const currentStep = parseInt(this.closest('.step-content').dataset.step);
                setActiveStep(currentStep + 1);
            });
        });

        prevStepButtons.forEach(button => {
            button.addEventListener('click', function () {
                const currentStep = parseInt(this.closest('.step-content').dataset.step);
                setActiveStep(currentStep - 1);
            });
        });
        //i will use ajax here for authenticaiton
        signupStepForm.addEventListener('submit', function (e) {
            e.preventDefault();
            // Here you would typically send the form data to your server
            alert('Signup successful!');
        });
    });
        