import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { map } from 'rxjs/operators';
import { catchError } from 'rxjs/operators';



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

  getUserIDFromUsername(username: string): Observable<number | null> {
    const url = 'http://127.0.0.1:8000/users/api/users/get_user_id_from_username/';
    const userData = { username };
  
    return this.http.post<{ userId: number }>(url, userData).pipe(
      map((response) => response.userId),
      catchError((error: HttpErrorResponse) => {
        console.error('Error fetching user ID:', error);
        return throwError('Failed to fetch user ID'); // Custom error message or handling
      })
    );
  }
}
