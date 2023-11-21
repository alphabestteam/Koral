import { Component, EventEmitter, Input, Output } from '@angular/core';

@Component({
  selector: 'app-my-inner',
  templateUrl: './my-inner.component.html',
  styleUrls: ['./my-inner.component.css']
})
export class MyInnerComponent {

  @Input() innerTotal: number = 5;
  @Output() incrementOuter = new EventEmitter<number>();

  upByOne(){
    this.innerTotal += 1;
    if(this.innerTotal > 10){
      this.innerTotal = 0;
      this.incrementOuter.emit(10)

    }
  }

  downByOne(){
    this.innerTotal -= 1;
    if (this.innerTotal < -10) {
      this.innerTotal = 0;
      this.incrementOuter.emit(-10);
  }
}
}
