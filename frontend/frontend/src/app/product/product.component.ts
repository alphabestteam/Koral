import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ProductService } from '../product.service';
import { Router } from '@angular/router';
import { AuthServiceService } from '../auth-service.service';

@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.css']
})
export class ProductComponent implements OnInit {
  products: any[] = [];
  showNavbar = true;
  userId: number | undefined;


  constructor(
    private productService: ProductService,
    private route: ActivatedRoute,
    private router: Router,
    private authService: AuthServiceService
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
        this.products = data;
      },
      (error) => {
        console.error(error);
      }
    );
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
          alert(`Product: ${product_name} added successfully to the basket!`);
          const response = await this.productService.addToBasket(userId, product_id).toPromise();
          console.log('Product added to the basket:', response);
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