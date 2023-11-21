import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { StarWarsMoviesComponent } from './star-wars-movies/star-wars-movies.component';

const routes: Routes = [
  { path: 'movies', component: StarWarsMoviesComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }