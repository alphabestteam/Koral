import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ProductService } from '../product.service';

@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.css']
})
export class ProductComponent implements OnInit {
  products: any[] = [];

  constructor(
    private productService: ProductService,
    private route: ActivatedRoute
  ) {}

  ngOnInit(): void {
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