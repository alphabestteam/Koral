import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StarWarsMoviesComponent } from './star-wars-movies.component';

describe('StarWarsMoviesComponent', () => {
  let component: StarWarsMoviesComponent;
  let fixture: ComponentFixture<StarWarsMoviesComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [StarWarsMoviesComponent]
    });
    fixture = TestBed.createComponent(StarWarsMoviesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
