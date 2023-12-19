import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ProductService } from '../product.service';
import { Router } from '@angular/router';

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
    private router: Router
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

  getUserId(): number | null {
    const userIdString = sessionStorage.getItem('user_id');
    return userIdString ? +userIdString : null; // Convert string to number or return null
  }

  addToBasket(product_name: string, product_id: number): void {
    alert(`Product: ${product_name} added successfully to the basket!`);
    const userId = this.getUserId();
    if (userId !== null) {
      this.productService.addToBasket(userId, [product_id]) // Wrap the ID in an array
        .subscribe(response => {
          console.log('Product added to the basket:', response);
        }, error => {
          console.error('Error adding product to the basket:', error);
        });
    } else {
      console.error('User ID not found in session storage or invalid');
    }
  }
}