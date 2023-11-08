/*
List of endpoints:
  GET - http://localhost:8000/hello -> {'Hello': 'World'} Here as an example
  GET - http://localhost:8000/menu -> {'items': menu} A dict of the menu
  POST - http://localhost:8000/latest-order -> A dict of the latest order
  POST - http://localhost:8000/orders -> An endpoint to handle an order. The order is in the http body as so: { 'items': items }

*/

menu = document.getElementById("menu");
productName = document.getElementById("name_price");
productDescription = document.createElement("description")
productQuantity = document.createElement("quantity")

menu.style.display = 'none';





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

          menu.style.display = 'block';
          const dataJson = JSON.parse(data);

          for (const key in dataJson.items) {
            if (dataJson.items.hasOwnProperty(key)) {
              const item = dataJson.items[key];
              const name = item.name;
              const price = item.price;
              const description = item.description;

              document.getElementById("name_price").innerHTML = name + " ($" + price + ")";
              document.getElementById("description").innerHTML = description;
              document.getElementById("quantity").innerHTML = "Quantity:"
            }}
      })
      .catch(error => {
          console.error("Fetch error:", error);
      });
}

setTimeout(fetchMenu, 1000); //////// CHANGE TO 5000




