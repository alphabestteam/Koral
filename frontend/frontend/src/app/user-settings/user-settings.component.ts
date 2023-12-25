import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthServiceService } from '../auth-service.service';
import { FormBuilder, FormGroup, Validators } from "@angular/forms";
import { MatSnackBar } from '@angular/material/snack-bar'; // Import MatSnackBar


@Component({
  selector: 'app-user-settings',
  templateUrl: './user-settings.component.html',
  styleUrls: ['./user-settings.component.css']
})
export class UserSettingsComponent implements OnInit {

  passwordError: boolean = false;
  public changePasswordForm!: FormGroup;
  public submitted = false;


  constructor(
    private formBuilder: FormBuilder,
    private authService: AuthServiceService,
    private router: Router,
    private snackBar: MatSnackBar 
  ){}

  getUserName(){
    return sessionStorage.getItem('username');
  }

  getPassword(){
    return sessionStorage.getItem('password');
  }
  
  dataRemove(){
    sessionStorage.removeItem('username');
    sessionStorage.removeItem('password');
    this.router.navigateByUrl(`/login`);
    this.authService.logout()
  }

  ngOnInit(): void {
    this.changePasswordForm = this.formBuilder.group({
      current_password: ["", Validators.required],
      new_password: ["", [Validators.required, Validators.pattern(/^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*#?&]{8,}$/)]],
      confirm_new_password: ["", Validators.required],
    });
  }


  onChangePassword(): void {
    this.submitted = true;
  
    if (this.changePasswordForm.valid) {
      const currentPassword = this.changePasswordForm.get('current_password')?.value;
      const newPassword = this.changePasswordForm.get('new_password')?.value;
      const confirmNewPassword = this.changePasswordForm.get('confirm_new_password')?.value;
  
      if (newPassword !== confirmNewPassword) {
        this.changePasswordForm.get('confirm_new_password')?.setErrors({ unmatchedPassword: true });
        return;
      } else {
        const storedPassword = this.getPassword(); // Retrieve the stored password
        console.log(storedPassword)
        console.log(newPassword)
        if (currentPassword !== storedPassword) {
          this.changePasswordForm.get('current_password')?.setErrors({ invalidPassword: true });
          return;
        } else {
          const storedPassword = this.getPassword(); // Retrieve the stored password
  
        const username = this.getUserName();
  
        if (username) {
          this.authService.getUserIDFromUsername(username).subscribe(
            userID => {
              if (userID !== null) {
                // Call the service method to change the password with retrieved userID
                this.authService.changeUserPassword(userID, newPassword).subscribe(
                  response => {
                    // Show a success snackbar
                    this.router.navigateByUrl('/login')
                    this.snackBar.open('Password changed successfully!', 'Close', {
                      duration: 3000,
                      horizontalPosition: 'center',
                      verticalPosition: 'bottom',
                      panelClass: ['success-snackbar']
                    });
                  },
                  error => {
                    console.error('Error changing password:', error);
                    // Show an error message or handle appropriately
                  }
                );
              } else {
                console.error('User ID not found for the provided username');
                // Handle the case where the user ID is not found
              }
            },
            error => {
              console.error('Error fetching user ID:', error);
              // Show an error message or handle appropriately
            }
          );
        } else {
          console.error('Username not available');
          // Handle the case where the username is not available
        }
      }
    }
  }
}
  
}
