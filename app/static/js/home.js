fetch('http://localhost:5000/user')
    .then(function (response) {
        return response.json();
    }).then(function (text) {
        document.getElementById("first_name").innerText = text.first_name;
        document.getElementById("last_name").innerText = text.last_name;
        document.getElementById("field").innerText = text.field;
        document.getElementById("description").innerText = text.description;
    });