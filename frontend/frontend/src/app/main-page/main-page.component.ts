import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-main-page',
  templateUrl: './main-page.component.html',
  styleUrls: ['./main-page.component.css']
})
export class MainPageComponent implements OnInit {
  showNavbar = true; // By default, show the navbar

  constructor(private router: Router) {}

  ngOnInit(): void {
    this.checkUrl();
  }

  // Method to check the URL and toggle showNavbar
  checkUrl() {
    this.showNavbar = !this.router.url.includes('products/');
  }
}


