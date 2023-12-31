import { Component, OnInit } from "@angular/core";
import { FormBuilder, FormGroup, Validators } from "@angular/forms";
import { AuthServiceService } from "../auth-service.service";
import { Router } from "@angular/router";

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  public registerForm!: FormGroup;
  public submitted = false;
  public error = '';
  public successMessage  = '';

  constructor(
    private authService: AuthServiceService,
    private formBuilder: FormBuilder,
    private router: Router
  ) { }

  ngOnInit(): void {
    this.registerForm = this.formBuilder.group({
      username: ['', Validators.required],
      password: [
        '',
        [
          Validators.required,
          Validators.pattern(/^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*#?&]{8,}$/)
        ]
      ]
    });
  }

  get formControl() {
    return this.registerForm.controls;
  }

  async onSubmit(): Promise<void> {
    this.submitted = true;
  
    if (this.registerForm.valid) {
      const username = this.registerForm.get('username')?.value;

      try {
        const registerData = {
          username: this.registerForm.get('username')?.value,
          password: this.registerForm.get('password')?.value 
        };

        await this.authService.register(registerData).toPromise(); // register the user

        this.successMessage = 'Registration successful!';
        this.dataSave()
        this.router.navigate(['/main']);
        setTimeout(() => {
          this.successMessage = '';
        }, 2000);

        this.registerForm.reset();
      } catch (error:any) {
        if (error.status == 400){
        this.error = 'Username is already taken';
        }
        else{
          this.error = 'Registration failed';
        }
      }
    }
  }

  redirectToLogin(): void {
    this.router.navigate(['/login']); 
  }

  dataSave(){
    let username = this.registerForm.value.username;
    sessionStorage.setItem('username', username);
    let password = this.registerForm.value.password
    sessionStorage.setItem('password', password);
  }

}
