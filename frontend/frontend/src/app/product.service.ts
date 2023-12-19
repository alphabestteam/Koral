import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, catchError, throwError } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProductService {
  private apiUrl = 'http://127.0.0.1:8000/products/api/products/';
  private apiUrlGender = 'http://127.0.0.1:8000/products/'
  private baseUrl = 'http://127.0.0.1:8000'; 

  
  constructor(private http: HttpClient) {}

  getProducts(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl);
  }

  addProduct(productData: any): Observable<any> {
    return this.http.post<any>(this.apiUrl, productData);
  }

  updateProduct(productId: number, productData: any): Observable<any> {
    const url = `${this.apiUrl}${productId}/`;
    return this.http.put<any>(url, productData);
  }

  deleteProduct(productId: number): Observable<any> {
    const url = `${this.apiUrl}${productId}/`;
    return this.http.delete<any>(url);
  }

  getProductsByGender(gender: string): Observable<any[]> {
    const url = `${this.apiUrlGender}${gender}`;
    return this.http.get<any[]>(url);
  }


  
  getProductsInBasket(userId: number): Observable<any[]> {
    const url = `${this.baseUrl}/users/api/users/${userId}/get_products_in_basket/`;
    return this.http.get<any[]>(url);
  }
  
  addToBasket(userId: number, productId: number): Observable<any> {
    const url = `${this.baseUrl}/basket/api/Basket/add_to_basket/`; 
    const data = { user_id: userId, product_id: productId };
    return this.http.post<any>(url, data);
  }

  updateProductStatus(productId: number): Observable<any> {
    const url = `${this.baseUrl}/products/update_product_status/${productId}/`;
    return this.http.post<any>(url, {});
  }

  checkout(userId: number): Observable<any> {
    const checkoutUrl = `${this.baseUrl}/basket/checkout/${userId}`; // Update with your checkout endpoint

    // Perform the checkout logic, possibly making an HTTP request
    // Here, an HTTP POST request is made to trigger the checkout
    return this.http.post(checkoutUrl, null);
  }
}