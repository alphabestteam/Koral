import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { map } from 'rxjs/operators';
import { catchError, tap } from 'rxjs/operators';


@Injectable({
  providedIn: 'root'
})
export class AuthServiceService {
  private isAuthenticated: boolean = false;
  private apiUrl = 'http://127.0.0.1:8000/users/api/users/';

  constructor(private http: HttpClient) {this.isAuthenticated = this.checkStoredSession();}
    

  login(loginData: any): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}login/`, loginData).pipe(
      tap(response => {
        if (response.error === 'Login successful') {
          // Upon successful login, store session data in local storage
          localStorage.setItem('sessionData', JSON.stringify(response)); 
          
          // Update isAuthenticated
          this.isAuthenticated = true;
        }
        return response;
      })
    );
  }

    register(userData: any): Observable<any> {
      return this.http.post<any>(`${this.apiUrl}`, userData).pipe(
        tap(response => {
          // Upon successful registration, store session data in local storage
            if (response.error === 'User registered successfully') {
              localStorage.setItem('sessionData', JSON.stringify(response)); 
              
              // Update isAuthenticated
              this.isAuthenticated = true;
            }
          return response; 
        })
      );
    }

    logout(){
      this.isAuthenticated = false;
    }

    getUserIDFromUsername(username: string): Observable<number | null> {
      const url = `${this.apiUrl}get_user_id_from_username/`;
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
        // If valid, set isAuthenticated to true
        this.isAuthenticated = true;
      }
      return this.isAuthenticated;
    }

    changeUserPassword(userID: any, newPassword: any): Observable<any> {
      const url = `${this.apiUrl}${userID}/change_password/`;
      return this.http.put<any>(url, { new_password: newPassword });
    }
  
}
