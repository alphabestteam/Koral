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
        // Call the service method to change the password
        this.authService.changeUserPassword(this.getUserName(), newPassword).subscribe(
          response => {
            // Show a success snackbar
            this.snackBar.open('Password changed successfully!', 'Close', {
              duration: 3000, // Duration the snackbar is shown (in milliseconds)
              horizontalPosition: 'center', // Position of the snackbar
              verticalPosition: 'bottom',
              panelClass: ['success-snackbar'] // CSS class for styling the snackbar
            });
            // Additional code, if needed
          },
          error => {
            // Handle error, e.g., display an error message
            console.error('Error changing password:', error);
            // Show an error message or handle appropriately
          }
        );
      }
    }
  }
}
