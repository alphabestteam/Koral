import { Component, OnInit } from "@angular/core";
import { FormBuilder, FormGroup, Validators } from "@angular/forms";
import { Router } from "@angular/router";

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {
  public RegisterForm!: FormGroup;
  public submitted = false;

  constructor(private formBuilder: FormBuilder, private router: Router) {}

  ngOnInit(): void {
    this.RegisterForm = this.formBuilder.group({
      email: ["", [Validators.email, Validators.required]],
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
    return this.RegisterForm.controls;
  }

  onRegister(): void {
    this.submitted = true;
    if (this.RegisterForm.valid) {
      console.log(this.RegisterForm.value);
      // Here, you can implement logic to send the Register credentials to the server for validation
      // For now, storing the user data in localStorage and navigating to another route
      localStorage.setItem("user-Data", JSON.stringify(this.RegisterForm.value));
      this.router.navigate(["/"]); // Change the route to the desired path after Register
    }
  }
}
