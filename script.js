button = document.getElementById("my-button");
counter = document.getElementById("counter-display");

button.setAttribute("type", "button")
var count = 0


function addEvent() {
    count++
    counter.innerHTML = count
};

button.addEventListener("click", addEvent);