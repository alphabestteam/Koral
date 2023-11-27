import { Component } from '@angular/core';
import { products } from '../mock_db';
import { ShoppingCartService } from '../shopping-cart.service';

@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.css']
})

export class ProductComponent {
  
  products_list : Product[] = products;

  constructor(private shoppingCartService: ShoppingCartService) {}

  addToBag(product: Product): void {
    // Call the addToCart method from the shopping cart service
    this.shoppingCartService.addToCart(product);
    alert(`Added ${product.name} to the shopping bag!`);
  }
}

export interface Product{
  id : number;
  name : string;
  price : number;
  description: string;
  image : string;
  category: string;
}
