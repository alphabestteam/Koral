import { Component } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  constructor(private modalService: NgbModal) {
  }

  public open(modal: any): void {
    this.modalService.open(modal);
  }
  
  textInput: string = '';
  textOutput: string = '';
  buttonUser = document.getElementById("buttonUser");


  updatePara(event: Event){
    this.textOutput = this.textInput;
  }
  
  restartPara(){
    this.textInput = "";
    this.textOutput = "";
  }

  checkInputLength(){
    if (this.textInput) {
      if (this.textInput.length === 0) {
        this.buttonUser.style.cursor = "not-allowed";
      } else {
        this.buttonUser.style.cursor = "pointer";
      }
    }
  }
}
