import { Component, OnInit} from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  showLoader: boolean = true;
  showMainContent: boolean = false;


  ngOnInit() {
    // Simulate loading delay before showing main content
    setTimeout(() => {
      this.showLoader = false;
      this.showMainContent = true;
    }, 3000); // Show main content after 3 seconds
  }
  
}
