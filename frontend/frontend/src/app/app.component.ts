import { Component, OnInit} from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  showLoader: boolean = true;
  showMainContent: boolean = false;
  showLogin: boolean = false;
  showRegister: boolean = false;



  ngOnInit() {
    // simulate loading delay before showing main content
    setTimeout(() => {
      this.showLoader = false;
      this.showLogin = true;

      setTimeout(() => {
        this.showMainContent = true; 
      }, );
    }, 3000); // show main content after 3 seconds
  }

  onLoginSuccess() {
    this.showLogin = false;
    this.showMainContent = true;
  }

  onRegistrationSuccess(event: any) {
    // Handle registration success here
    this.showRegister = false;
    this.showMainContent = true;
  }

}
