import { Component, Input } from '@angular/core';
import { StarWarsMovie } from '../starWarsMovie'; 

@Component({
  selector: 'app-movie-card',
  templateUrl: './movie-card.component.html',
  styleUrls: ['./movie-card.component.scss']
})
export class MovieCardComponent {
  // the ! to make sure that movie will get a value
  @Input() movie!: StarWarsMovie;
}
