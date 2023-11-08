/*
List of endpoints:
  GET - http://localhost:8000/hello -> {'Hello': 'World'} Here as an example
  GET - http://localhost:8000/menu -> {'items': menu} A dict of the menu
  POST - http://localhost:8000/latest-order -> A dict of the latest order
  POST - http://localhost:8000/orders -> An endpoint to handle an order. The order is in the http body as so: { 'items': items }

*/

menu = document.getElementById("menu");

menu.style.display = 'none';

submitOrderButton = document.getElementById("submit-button");
submitOrderButton.getAttribute("type", "button")

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

          i = 0;
          for (const key in dataJson.items) {
            if (dataJson.items.hasOwnProperty(key)) {
              const item = dataJson.items[key];
              const name = item.name;
              const price = item.price;
              const description = item.description;
              document.getElementById("name_price" + i).innerHTML = name + " (" + new Intl.NumberFormat('en-DE', {
                style: 'currency',
                currency: 'USD'}).format(price).replace(/US/g, '') + ")";
              document.getElementById("description" + i).innerHTML = description;
              i ++;
            }
          }
      }).then(data => {
        for (let i = 0; i < 4; i++)
        {
          quantity = document.getElementById("Quantity" + i);
          orderSumUp = document.getElementById("orderSumUp")
          if (i ==0){
            quantity.addEventListener("input", (e) =>{
              document.getElementById("orderSumUp").innerHTML += `\nChum Burger (${quantity.value} X\n` ;})
          }

          else if (i == 1){
            quantity.addEventListener("input", (e) =>{
              document.getElementById("orderSumUp").innerHTML += `\nKelp Fries (${quantity.value} X\n` ;})
          }

          else if (i == 2){
            quantity.addEventListener("input", (e) =>{
              document.getElementById("orderSumUp").innerHTML += `\nKrabby Patty (${quantity.value} X\n` ;})
          }

          else if (i == 3){
            quantity.addEventListener("input", (e) =>{
              document.getElementById("orderSumUp").innerHTML +=`\nKrusty Krab Pizza (${quantity.value} X\n` ;})
          }
        }
        

        submitOrderButton.addEventListener("click", myFunction);

      })
      .catch(error => {
          console.error("Fetch error:", error);
      });
}

setTimeout(fetchMenu, 5000); 




