const output = document.querySelector('.output');
const output1 = document.createElement('div');
const ul = document.createElement('ul');

output.append(output1);
output.append(ul);
fetch('http://localhost:5000/projects')
    .then(function (response) {
        return response.json();
    }).then((data) => {
        addtoPage(data);
    });

function addtoPage(arr) {
    arr.forEach(element => {
        createCard(element.name, element.technology, element.short, element.status, element.urlGit);
    });
}

const projects = document.querySelector(".projectHolder")
function createCard(projectName, projectTechnology, projectDescription, projectStatus, projectGit) {
    let code = `
        <div class="card transition">
            <h2 class="name">${projectName}</h2>
            <p class="technology">${projectTechnology}</p>
            <p class="description">${projectDescription}</p>
            <p class="status">${projectStatus}</p>
            <div class="cta-container transition"><a href="#" class="cta">Demo</a></div>
            <div class="ctb-container transition"><a href="${projectGit}" class="ctb">GitHub</a></div>
            <div class="card_circle transition"></div>
        </div>
        `;
    projects.innerHTML += code;
}