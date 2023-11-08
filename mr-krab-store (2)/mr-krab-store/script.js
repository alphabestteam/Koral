/*
List of endpoints:
  GET - http://localhost:8000/hello -> {'Hello': 'World'} Here as an example
  GET - http://localhost:8000/menu -> {'items': menu} A dict of the menu
  POST - http://localhost:8000/latest-order -> A dict of the latest order
  POST - http://localhost:8000/orders -> An endpoint to handle an order. The order is in the http body as so: { 'items': items }

*/

menu = document.getElementById("menu");
productName = document.createElement("p")
// productName = 
//to show the gif : 









function fetchMenu() {
  document.getElementById("loader").style.display = "block";

  fetch("http://localhost:8000/menu")
      .then(response => {
          if (!response.ok) {
              throw new Error("Couldn't Fetch");
          }
          return response.text();
      })
      .then(data => {
          document.getElementById("loader").style.display = "none";

          document.getElementById("menu").innerHTML = data;
      })
      .catch(error => {
          console.error("Fetch error:", error);
      });
}

setTimeout(fetchMenu, 5000);



