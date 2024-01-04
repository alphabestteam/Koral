import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-cd',
  templateUrl: './cd.component.html',
  styleUrls: ['./cd.component.css']
})
export class CdComponent {
  @Input() cd: any;
}
