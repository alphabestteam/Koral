import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

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
