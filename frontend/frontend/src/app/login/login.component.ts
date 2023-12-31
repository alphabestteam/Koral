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
          this.dataSave();
          
          setTimeout(() => {
            this.success = '';
          }, 2000);
          
          this.loginForm.reset();
        }
      } catch (error:any) { 
          if (error.status === 401){
            this.error = 'Password is wrong';
          } else if(error.status === 404){
            this.error = 'Username is not found';
          }else{

            this.error = 'Login failed';
          }  
    }
  }
} 

redirectToRegister(): void {
  this.router.navigate(['/register']); 
  }  

  dataSave(){
    let username = this.loginForm.value.username;
    sessionStorage.setItem('username', username);
    let password = this.loginForm.value.password
    sessionStorage.setItem('password', password);
  }
}