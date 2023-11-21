import { Component } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { count } from 'rxjs';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  counter: number = 0;
  details: boolean = true;
  counterArray: number[] = [];

  displayDetails() : void {
      this.counter++;
      this.counterArray.push(this.counter);
      this.details = !this.details;
  };

  getHidden() {
      return this.details ? 'visible' : 'hidden';
  }
}


