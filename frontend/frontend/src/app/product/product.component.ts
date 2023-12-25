import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ProductService } from '../product.service';
import { Router } from '@angular/router';
import { AuthServiceService } from '../auth-service.service';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.css']
})
export class ProductComponent implements OnInit {
  products: any[] = [];
  showNavbar = true;

  constructor(
    private productService: ProductService,
    private route: ActivatedRoute,
    private router: Router,
    private authService: AuthServiceService,
    private snackBar: MatSnackBar
  ) {}

  ngOnInit(): void {
    this.checkUrl();
    this.route.params.subscribe(params => {
      const gender = params['gender'];
      if (gender) {
        this.fetchProductsByGender(gender);
      } else {
        // Handle scenario when no gender parameter is present
        // For instance, fetch all products or display a message
        this.fetchAllProducts();
      }
    });
  }

  // Method to check the URL and toggle showNavbar
  checkUrl() {
    this.showNavbar = this.router.url.includes('products/');
  }


  get(){
    return sessionStorage.getItem('username');
  }

  fetchProductsByGender(gender: string): void {
    this.productService.getProductsByGender(gender).subscribe(
      (data: any[]) => {
        this.products = this.adjustPictureUrls(data);
      },
      (error) => {
        console.error(error);
      }
    );
  }
  
  // Helper function to adjust picture URLs
  adjustPictureUrls(products: any[]): any[] {
    return products.map(product => ({
      ...product,
      picture: this.adjustPictureUrl(product.picture)
    }));
  }
  
  // Helper function to adjust the picture URL
  adjustPictureUrl(url: string): string {
    if (!url.startsWith('http')) {
      return `http://127.0.0.1:8000${url}`;
    }
    return url;
  }
  

fetchAllProducts(): void {
  this.productService.getProducts().subscribe(
    (data: any[]) => {
      this.products = data;
    },
    (error) => {
      console.error(error);
    }
  );
  }
  async addToBasket(product_name: string, product_id: number): Promise<void> {
    const username = this.get();
  
    if (username !== null) {
      try {
        const userId = await this.authService.getUserIDFromUsername(username).toPromise();
  
        if (userId !== null && typeof userId === 'number') {
          const response = await this.productService.addToBasket(userId, product_id).toPromise();
          console.log('Product added to the basket:', response);
  
          // Check the modified response from the service
          if (response) {
            // Display Snackbar upon successful addition
            this.snackBar.open(`Product ${product_name} added successfully to the basket!`, 'Close', {
              duration: 3000,
              horizontalPosition: 'center',
              verticalPosition: 'bottom',
              panelClass: ['success-snackbar']
            });
  
            // Other logic after successful addition, if needed
          } else {
            console.error('Failed to add product to the basket');
          }
        } else {
          console.error('User ID not found or invalid');
        }
      } catch (error) {
        console.error('Error:', error);
      }
    } else {
      console.error('Username not found in session storage or invalid');
    }
  }
  
  
}