
const containerDiv = document.getElementById("container");
console.log(containerDiv);


const firstUl = document.querySelectorAll("ul")[0];
firstUl.children[1].textContent = "Richard";


const secondUl = document.querySelectorAll("ul")[1];
secondUl.children[1].remove();


const allUls = document.querySelectorAll("ul");
allUls.forEach(ul => {
    ul.children[0].textContent = "Achraf";
});


allUls.forEach(ul => {
    ul.classList.add("student_list");
});


firstUl.classList.add("university", "attendance");


containerDiv.style.backgroundColor = "lightblue";
containerDiv.style.padding = "10px";


const allLis = document.querySelectorAll("li");
allLis.forEach(li => {
    if (li.textContent === "Dan") {
        li.style.display = "none";
    }
});


allLis.forEach(li => {
    if (li.textContent === "Richard") {
        li.style.border = "1px solid black";
    }
});


document.body.style.fontSize = "18px";
