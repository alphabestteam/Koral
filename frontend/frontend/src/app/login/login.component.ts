import { Component, OnInit, Output, EventEmitter } from "@angular/core";
import { FormBuilder, FormGroup, Validators } from "@angular/forms";
import { Router } from "@angular/router";
import { AuthServiceService } from "../auth-service.service";


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  public loginForm!: FormGroup;
  public submitted = false;
  public error = '';
  public success = '';

  @Output() loginSuccess: EventEmitter<string> = new EventEmitter<string>();
  //  to handle the login process and set the success message
  // set this.success to 'Login Successful!' when login is successful
  
  
  constructor(
    private authService: AuthServiceService,
    private router: Router,
    private formBuilder: FormBuilder
    ) {}

    ngOnInit(): void {
      this.loginForm = this.formBuilder.group({
        username: ["", Validators.required],
      password: [
        "",
        [
          Validators.required,
          Validators.pattern(/^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*#?&]{8,}$/)
        ]
      ]
    });
  }
  
  get formControl() {
    return this.loginForm.controls;
  }
  
  async onSubmit(): Promise<void> {
    this.submitted = true;
  
    if (this.loginForm.valid) {
      const username = this.loginForm.get('username')?.value;
      const password = this.loginForm.get('password')?.value;
      
      const loginData = {
        username,
        password
      };
      
      try {
        const response = await this.authService.login(loginData).toPromise();
        
        if (response.message === 'Login successful') {
          this.router.navigate(['/main']);
          this.success = "Login Successful!"

          setTimeout(() => {
            this.success = '';
          }, 2000);
          
          this.loginForm.reset();
        } else if (response.message === 'Password is wrong') {
          this.error = 'Password is wrong';
        } else if (response.message === 'User not found') {
          this.error = 'Username is not found';
        }
      } catch (error) { /* if the server is disconnected*/ 
      this.error = (error as any).error.message || 'Login failed';
    }
  }
} 

redirectToRegister(): void {
  this.router.navigate(['/register']); 
  }  
}