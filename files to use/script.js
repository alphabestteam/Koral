const button = document.getElementById('the-button');
const main = document.querySelector("main");
const bobGif = document.getElementById("bob");

button.setAttribute("type", "button")

button.textContent = "Hide Bob ;)"


let isClicked = true

const toggleBob = function(){
if (isClicked == true){
    console.log("iujesdf")
    bobGif.setAttribute("src", " ")
    button.textContent = "Show Me bob;)"
    isClicked = false
    }
else{
        bobGif.setAttribute("src", "./assets/sbdance.gif")
        button.textContent = "Hide Bob ;)"
        isClicked = true

    }
};

button.addEventListener("click", toggleBob);