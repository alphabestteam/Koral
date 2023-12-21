import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { map } from 'rxjs/operators';
import { catchError } from 'rxjs/operators';


@Injectable({
  providedIn: 'root'
})
export class AuthServiceService {
  private isAuthenticated: boolean = false;
  
  constructor(private http: HttpClient) {this.isAuthenticated = this.checkStoredSession();}
    

    login(loginData: any): Observable<any> {
      return this.http.post<any>('http://127.0.0.1:8000/users/api/users/login/', loginData).pipe(
        map(response => {
          // Upon successful login, store session data in local storage
          localStorage.setItem('sessionData', JSON.stringify(response)); // Adjust this as per your received data
          
          // Update isAuthenticated
          this.isAuthenticated = true;
          return response; // Return the response from the API
        }),
        catchError(error => {
          console.error('Login failed:', error);
          this.isAuthenticated = false; // Set isAuthenticated to false on login failure
          return throwError('Failed to log in'); // Custom error message or handling
        })
      );
    }

    register(userData: any): Observable<any> {
      return this.http.post<any>('http://127.0.0.1:8000/users/api/users/', userData).pipe(
        map(response => {
          // Upon successful registration, store session data in local storage
          localStorage.setItem('sessionData', JSON.stringify(response)); // Adjust this as per your received data
          
          // Update isAuthenticated
          this.isAuthenticated = true;
          return response; // Return the response from the API
        }),
        catchError(error => {
          console.error('Registration failed:', error);
          this.isAuthenticated = false; // Set isAuthenticated to false on registration failure
          return throwError('Failed to register'); // Custom error message or handling
        })
      );
    }

    logout(){
      this.isAuthenticated = false;
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

    // Method to check if the user is logged in
    isLoggedIn(): boolean {
      console.log(this.isAuthenticated)
      return this.isAuthenticated; // Return the authentication status
    }

    checkStoredSession(): boolean {
      const storedSessionData = localStorage.getItem('sessionData');
      if (storedSessionData) {
        // Validate the session data (e.g., token validity, expiration, etc.)
        // If valid, set isAuthenticated to true
        this.isAuthenticated = true;
      }
      return this.isAuthenticated;
    }
}
