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
    // simulate loading delay before showing main content
    setTimeout(() => {
      this.showLoader = false;
      setTimeout(() => {
        this.showMainContent = true; 
      }, );
    }, 3000); // show main content after 3 seconds
  }
}
