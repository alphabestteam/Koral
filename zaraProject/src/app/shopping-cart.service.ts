
import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';
import { Product } from './product/product.component'; 

@Injectable({
  providedIn: 'root',
})
export class ShoppingCartService {
  private cartItems: Product[] = [];
  private cartSubject: BehaviorSubject<Product[]> = new BehaviorSubject<Product[]>([]);

  constructor() {}

  addToCart(product: Product): void {
    this.cartItems.push(product);
    this.cartSubject.next(this.cartItems);
  }

  getCartItems(): Observable<Product[]> {
    return this.cartSubject.asObservable();
  }

  clearCart(): void {
    this.cartItems = [];
    this.cartSubject.next(this.cartItems);
  }
}
