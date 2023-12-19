import { Component, OnInit } from '@angular/core';
import { ProductService } from '../product.service';
import { AuthServiceService } from '../auth-service.service';
import { switchMap } from 'rxjs';

@Component({
  selector: 'app-basket',
  templateUrl: './basket.component.html',
  styleUrls: ['./basket.component.css']
})
export class BasketComponent implements OnInit {
    productsInBasket: any[] = [];
    totalPrice: number = 0;
  
    constructor(
      private productService: ProductService,
      private authService: AuthServiceService

      ) {}
  
    ngOnInit(): void {
      this.fetchProductsInBasket();
    }

    getUserId(): number | null {
      const userIdString = sessionStorage.getItem('user_id');
      return userIdString ? +userIdString : null; // Convert string to number or return null
    }
    
    get(){
      return sessionStorage.getItem('username');
    }

    fetchProductsInBasket(): void {
      this.authService.getUserIDFromUsername(this.get())
        .pipe(
          switchMap(userId => {
            if (userId !== null) {
              return this.productService.getProductsInBasket(userId);
            } else {
              console.error('User ID not found in session storage or invalid');
              return EMPTY; // Or any appropriate observable in case of an error
            }
          })
        )
        .subscribe(
          products => {
            this.productsInBasket = products;
            this.calculateTotalPrice();
          },
          error => {
            console.error('Error fetching products in the basket:', error);
          }
        );
    }
    
  
    calculateTotalPrice(): void {
      // Calculate the total price from productsInBasket
      this.totalPrice = this.productsInBasket.reduce((total, product) => total + product.price, 0);
    }
  
    checkout(): void {
      // Call the service method to update product status and reset the basket
      const userId = this.getUserId();
    
      if (userId !== null) {
        this.productService.checkout(userId)
          .subscribe(response => {
            console.log('Checkout successful:', response);
            // Reset basket data and UI if needed
            this.updateProductStatusForCheckout(); // Call the function to update product status
            this.productsInBasket = [];
            this.totalPrice = 0;
          }, (error: any) => {
            console.error('Error during checkout:', error);
            // Handle error or display error message
          });
      } else {
        console.error('User ID not found in session storage or invalid');
      }
    }
    
    updateProductStatusForCheckout(): void {
      // Loop through products in the basket and update their status
      this.productsInBasket.forEach(product => {
        this.productService.updateProductStatus(product.id)
          .subscribe(response => {
            console.log('Product status updated:', response);
            // Handle success or update UI accordingly
          }, error => {
            console.error('Error updating product status:', error);
            // Handle error or display error message
          });
      });
    }
    
}

