import { Component } from '@angular/core';
import { StarWarsMovie } from '../starWarsMovie';
import { FILMS } from '../star-wars-fake-db/film-data';

@Component({
  selector: 'app-star-wars-movies',
  templateUrl: './star-wars-movies.component.html',
  styleUrls: ['./star-wars-movies.component.scss']
})
export class StarWarsMoviesComponent {
  movies: StarWarsMovie[] = FILMS;
    
  }
  