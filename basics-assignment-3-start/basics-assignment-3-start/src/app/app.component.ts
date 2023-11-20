import { Component } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { count } from 'rxjs';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {


  // for bootstrap : 
  constructor(private modalService: NgbModal) {
  }

  public open(modal: any): void {
    this.modalService.open(modal);
  }


  counter: number = 0;
    details: boolean = true;
    counterArray: number[] = [];

    displayDetails() {
      this.counter++;
      this.counterArray.push(this.counter);
      this.details = !this.details;
    };

    getHidden() {
      return this.details ? 'visible' : 'hidden';
    }
  }


