import { Component, OnInit } from '@angular/core';
import { ProductService } from '../product.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-main-page',
  templateUrl: './main-page.component.html',
  styleUrls: ['./main-page.component.css']
})
export class MainPageComponent implements OnInit {
  products: any[] = [];

  constructor(
    private productService: ProductService,
    private router: Router
  ) {}

  ngOnInit(): void {
    // Fetch products for kids on component initialization
    this.fetchProductsByGender('kids');
  }

  fetchProductsByGender(gender: string): void {
    this.productService.getProductsByGender(gender)
      .subscribe((data: any[]) => {
        this.products = data;
        // Update the URL based on the selected gender
        this.router.navigateByUrl(`/products/${gender}`);
      });
  }

}

