import { Component, OnInit } from '@angular/core';
import { ProductService } from '../product.service';
import { AuthServiceService } from '../auth-service.service';
import { switchMap, EMPTY } from 'rxjs';

@Component({
  selector: 'app-basket',
  templateUrl: './basket.component.html',
  styleUrls: ['./basket.component.css']
})


export class BasketComponent implements OnInit {
    productsInBasket: any[] = [];
    totalPrice: number = 0;
    numberOfProducts: number = 0;

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
    
    get(): string {
      const username = sessionStorage.getItem('username');
      return username !== null ? username : 'default'; // Provide a default value or handle null explicitly
    }    

    
    fetchProductsInBasket(): void {
      this.authService.getUserIDFromUsername(this.get()).subscribe(
        userId => {
          if (userId !== null) {
            this.productService.getProductsInBasket(userId).subscribe(
              (products: any[]) => {
                this.productsInBasket = products;
                this.numberOfProducts = this.productsInBasket.length; // Update number of products
                this.productsInBasket = products; // Assign products array to a variable
        
                // Fetch the total price
                this.productService.getTotalPrice(userId).subscribe(
                  (response: any) => {
                    console.log(response)
                    let totalPrice = response.total_price; // Extract total_price value
                    console.log('Total Price:', totalPrice); // Log total price
                    this.totalPrice = Number(totalPrice)
                    
                    // fix the total price showing, console is good but not in front
                  },
                  error => {
                    console.error('Error fetching total price:', error);
                  }
                );
              },
              error => {
                console.error('Error fetching products in the basket:', error);
              }
            );
          } else {
            console.error('User ID not found in session storage or invalid');
          }
        },
        error => {
          console.error('Error fetching user ID:', error);
        }
      );
    }
    
  
    checkout(): void {
      this.authService.getUserIDFromUsername(this.get()).subscribe(
        userId => {
          if (userId !== null) {
          alert(`${this.get()} Checkout-out Successfully!`);
            this.productService.checkout(userId).subscribe(
              response => {
                console.log('Checkout successful:', response);
                // Reset basket data and UI if needed
                this.updateProductStatusForCheckout(); // Update product status
                this.productsInBasket = [];
                this.totalPrice = 0;
              },
              error => {
                console.error('Error during checkout:', error);
                // Handle error or display error message
              }
            );
          } else {
            console.error('User ID not found in session storage or invalid');
          }
        },
        error => {
          console.error('Error fetching user ID:', error);
        }
      );
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

