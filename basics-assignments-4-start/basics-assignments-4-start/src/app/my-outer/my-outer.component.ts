import { Component } from '@angular/core';

@Component({
  selector: 'app-my-outer',
  templateUrl: './my-outer.component.html',
  styleUrls: ['./my-outer.component.css']
})
export class MyOuterComponent {
  outerTotal: number = 0;

  OuterTotal(value: number) {
    this.outerTotal += value;
  }
}
