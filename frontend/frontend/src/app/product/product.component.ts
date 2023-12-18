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
}