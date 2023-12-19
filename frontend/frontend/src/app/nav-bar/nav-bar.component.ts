import { Component } from '@angular/core';
import { ProductService } from '../product.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-nav-bar',
  templateUrl: './nav-bar.component.html',
  styleUrls: ['./nav-bar.component.css']
})
export class NavBarComponent {
  products: any[] = [];

  constructor(
    private productService: ProductService,
    private router: Router
  ) {}

  fetchProductsByGender(gender: string): void {
    this.productService.getProductsByGender(gender)
      .subscribe((data: any[]) => {
        this.products = data;
        // Update the URL based on the selected gender
        this.router.navigateByUrl(`/products/${gender}`);
      });
  }

  navToMain(): void{
    this.router.navigateByUrl(`/main`);
  }

  get(){
    return sessionStorage.getItem('username');
  }

}

