fetch('http://localhost:5000/contact')
    .then(function (response) {
        return response.json();
    }).then(function (text) {
        document.getElementById("first_name").innerText = text.first_name;
        document.getElementById("last_name").innerText = text.last_name;
        document.getElementById("field").innerText = text.field;
        document.getElementById("description").innerText = text.description;
    });

const inputs = document.querySelectorAll(".input");

function focusFunc() {
    let parent = this.parentNode;
    parent.classList.add("focus");
}

function blurFunc() {
    let parent = this.parentNode;
    if (this.value == "") {
        parent.classList.remove("focus");
    }
}

inputs.forEach((input) => {
    input.addEventListener("focus", focusFunc);
    input.addEventListener("blur", blurFunc);
});