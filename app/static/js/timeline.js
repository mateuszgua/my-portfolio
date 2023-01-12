const output = document.querySelector('.output');
const output1 = document.createElement('div');
const ul = document.createElement('ul');

output.append(output1);
output.append(ul);
fetch('http://localhost:5000/timeline/load')
    .then(function (response) {
        return response.json();
    }).then((data) => {
        addtoPage(data);
    });

function addtoPage(arr) {
    arr.forEach(element => {
        createCard(element.year, element.title, element.content);
    });
}

const projects = document.querySelector(".timeline")
function createCard(timelineYear, timelineTitle, timelineContent) {
    let code = `
        <div class="square-timeline">
            <div class="year">${timelineYear}</div>
            <div class="title">${timelineTitle}</div>
            <div class="content">${timelineContent}</div>
        </div>
        `;
    projects.innerHTML += code;
}