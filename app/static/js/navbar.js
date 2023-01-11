const hamburger = document.querySelector(".hamburger")
const navUl = document.querySelector(".nav-ul")

hamburger.addEventListener("click", () => {
    navUl.classList.toggle("show");
    hamburger.classList.toggle("active");
});

document.querySelectorAll(".nav-link").forEach(n => n.addEventListener("click", () => {
    hamburger.classList.remove("active");
}));