import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { MyOuterComponent } from './my-outer/my-outer.component';
import { MyInnerComponent } from './my-inner/my-inner.component';

@NgModule({
  declarations: [
    AppComponent,
    MyOuterComponent,
    MyInnerComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
