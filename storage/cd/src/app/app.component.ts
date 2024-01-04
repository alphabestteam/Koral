import { Component, OnInit } from '@angular/core';
import { CdService } from './cd.service';
import { CD } from 'src/cd';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  cds: CD[] = [];
  cartItems: CD[] = [];

  constructor(private cdService: CdService) {}

  ngOnInit() {
    this.getAllCds();
    this.getCartItems();
  }

  getAllCds() {
    this.cdService.getAllCds().subscribe(
      (data: CD[]) => {
        this.cds = data;
      },
      (error: any) => {
        console.error('Error fetching CDs:', error);
      }
    );
  }

  getCartItems() {
    const storedCart = localStorage.getItem('cart');
    if (storedCart) {
      this.cartItems = JSON.parse(storedCart);
    }
  }

  addToCart(cd: CD) {
    this.cartItems.push(cd);
    localStorage.setItem('cart', JSON.stringify(this.cartItems));
  }

  purchaseItems() {
    console.log('Items Purchased:', this.cartItems);
    // Clearing the cart is optional, remove if you want to retain the items after purchase
    this.cartItems = [];
    localStorage.removeItem('cart');
  }
}