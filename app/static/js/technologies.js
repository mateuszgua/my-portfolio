const output = document.querySelector('.output');
const output1 = document.createElement('div');
const projects = document.querySelector(".technologies")
fetch('http://localhost:5000/technologies')
    .then(function (response) {
        return response.json();
    }).then((data) => {
        addtoPage(data);
    });

function addtoPage(arr) {
    arr.forEach(element => {
        createCard(element.technology, element.techImage);
    });
}

function createCard(techName, techImage) {
    let code = `
            <div class="square-tech">
                <div class="tech-image">
                    <center><img src="../static/images/${techImage}.png" class="tech-img" href="home.html"></center>
                </div>    
            </div >
        `;
    projects.innerHTML += code;
}