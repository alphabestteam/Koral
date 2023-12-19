import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProductService {
  private apiUrl = 'http://127.0.0.1:8000/products/api/products/';
  private apiUrlGender = 'http://127.0.0.1:8000/products/'
  
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
    const url = `http://127.0.0.1:8000/users/api/users/${userId}/get_queryset/`;
    return this.http.get<any[]>(url);
  }

  addToBasket(userId: number, productIds: number[]): Observable<any> {
    const url = 'http://127.0.0.1:8000/basket/add_to_basket/'; 
    const data = { user_id: userId, product_ids: productIds };
    return this.http.post<any>(url, data);
  }

  updateProductStatus(productId: number): Observable<any> {
    const url = `http://127.0.0.1:8000/products/update_product_status/${productId}/`;
    return this.http.post<any>(url, {});
  }

  checkout(userId: number): Observable<any> {
    const checkoutUrl = `http://127.0.0.1:8000/basket/checkout/${userId}`; // Update with your checkout endpoint

    // Perform the checkout logic, possibly making an HTTP request
    // Here, an HTTP POST request is made to trigger the checkout
    return this.http.post(checkoutUrl, null);
  }
}