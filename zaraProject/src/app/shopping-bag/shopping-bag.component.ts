import { Component, OnInit } from '@angular/core';
import { ShoppingCartService } from '../shopping-cart.service';
import { Product } from '../product/product.component';
import { products } from '../mock_db';


@Component({
  selector: 'app-shopping-bag',
  templateUrl: './shopping-bag.component.html',
  styleUrls: ['./shopping-bag.component.css']
})
export class ShoppingBagComponent implements OnInit {

  allProducts: Product[] = [];
  cartItems: Product[] = [];
  showAllProducts: boolean = false; // Flag to toggle the display of all products

  constructor(private shoppingCartService: ShoppingCartService) {}
  
  ngOnInit(): void {
    this.shoppingCartService.getCartItems().subscribe(items => {
      this.cartItems = items;
      // Update the list of all products after fetching the cart items
      this.allProducts = this.retrieveAllProducts();
    });
  }

  addProductToCart(product: Product): void {
    this.shoppingCartService.addToCart(product);
  }

  toggleProductList(): void {
    this.showAllProducts = !this.showAllProducts;
  }

  retrieveAllProducts(): Product[] {
    // Fetch all products (for example, from a service or predefined list)
    // This should include both added products and existing products
    const addedProducts = this.cartItems; // Retrieve added products
    // Example: Fetch other products from a service or define them

    // Concatenate added products and other products to create the full list
    return [...addedProducts];
  }

  isProductInCart(product: Product): boolean {
    return this.cartItems.some(item => item.id === product.id);
  }
}
