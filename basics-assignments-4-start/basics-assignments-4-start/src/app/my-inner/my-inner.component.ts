import { Component, EventEmitter, Input, Output } from '@angular/core';

@Component({
  selector: 'app-my-inner',
  templateUrl: './my-inner.component.html',
  styleUrls: ['./my-inner.component.css']
})
export class MyInnerComponent {

  innerTotal: number = 5;
  @Output() incrementOuter = new EventEmitter<number>();

  upByOne(): void{
    this.innerTotal += 1;
    if(this.innerTotal >= 9){
      this.innerTotal = 0;
      this.incrementOuter.emit(10)
    }
  }

  downByOne(): void{
    this.innerTotal -= 1;
    if (this.innerTotal <= -9) {
      this.innerTotal = 0;
      this.incrementOuter.emit(-10);
    }
  }
}
