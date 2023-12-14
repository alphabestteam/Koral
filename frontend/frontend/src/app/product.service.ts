import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProductService {
  private apiUrl = 'http://localhost:8000/products/api/Product';

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
}