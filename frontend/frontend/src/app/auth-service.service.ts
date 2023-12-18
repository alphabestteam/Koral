import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthServiceService {

  constructor(private http: HttpClient) {}

  login(loginData: any): Observable<any> {
    return this.http.post<any>('http://127.0.0.1:8000/users/api/users/login/', loginData);
  }

  register(userData: any): Observable<any> {
    return this.http.post<any>('http://127.0.0.1:8000/users/api/users/', userData);
  }

}
