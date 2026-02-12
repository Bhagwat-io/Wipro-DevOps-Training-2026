// MOBILE MENU

const hamburger = document.querySelector(".hamburger");
const navLinks = document.querySelector(".nav-links");

hamburger.addEventListener("click", () => {
    navLinks.classList.toggle("active");
});


// CONTACT FORM (Fake submission)

document.getElementById("contactForm")
.addEventListener("submit", function(e){

    e.preventDefault();

    document.getElementById("formMessage")
    .innerText = "✅ Thank you! Our team will contact you shortly.";

});
