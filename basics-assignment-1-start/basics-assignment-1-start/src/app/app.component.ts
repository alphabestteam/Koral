import { Component } from '@angular/core';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  showSuccess : boolean = true;

  // responsible for changing the value of the showComponentA boolean variable,flips the value of showSuccess when clicking on a button
  toggleComponent() {
    this.showSuccess = !this.showSuccess;
  }

  selectedTimes: number = 1;
  options: number[] = [1, 2, 3, 4, 5]; // Example options

  getTimes(times: number): any[] {
    return Array(times).fill(0);
  }
}
