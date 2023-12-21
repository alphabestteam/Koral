import { Component, OnInit, OnDestroy  } from '@angular/core';
import { ProductService } from '../product.service';
import { AuthServiceService } from '../auth-service.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-basket',
  templateUrl: './basket.component.html',
  styleUrls: ['./basket.component.css']
})


export class BasketComponent implements OnInit {
    productsInBasket: any[] = [];
    totalPrice: number = 0;
    numberOfProducts: number = 0;
    productAddedSubscription: Subscription | undefined;


    constructor(
      private productService: ProductService,
      private authService: AuthServiceService
      ) {}
  
    ngOnInit(): void {
        // Fetch initial products in the basket
        this.fetchProductsInBasket();
    
        // Subscribe to product added events to update the product list when a product is added
        this.productAddedSubscription = this.productService.onProductAdded().subscribe(() => {
          this.fetchProductsInBasket();
        });
    }

    ngOnDestroy(): void {
      // Unsubscribe to avoid memory leaks
      if (this.productAddedSubscription) {
        this.productAddedSubscription.unsubscribe();
      }
    }

    getUserId(): number | null {
      const userIdString = sessionStorage.getItem('user_id');
      return userIdString ? +userIdString : null; // Convert string to number or return null
    }
    
    get(): string {
      const username = sessionStorage.getItem('username');
      return username !== null ? username : 'default'; // Provide a default value or handle null explicitly
    }    

    

    calculateNumberOfProducts(products: any[]): number {
      return products.reduce((total, product) => total + (product.quantity || 0), 0);
    }
    
    // Assuming this is in your component file
  fetchProductsInBasket(): void {
    
    this.authService.getUserIDFromUsername(this.get()).subscribe(
      userId => {
        if (userId !== null) {
          this.productService.getCurrentBasketId(userId).subscribe(
            (basketId: any) => {
              if (basketId !== null) {
                this.productService.getProductsInBasket(basketId.basket_id).subscribe(
                  (products: any[]) => {
                    this.productsInBasket = products;
                    this.numberOfProducts = this.calculateNumberOfProducts(products);

                    this.productService.getTotalPrice(userId).subscribe(
                      (response: any) => {
                        let totalPrice = response.total_price;
                        this.totalPrice = Number(totalPrice);
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
                console.error('Basket ID not found for the user');
              }
            },
            error => {
              console.error('Error fetching basket ID:', error);
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

