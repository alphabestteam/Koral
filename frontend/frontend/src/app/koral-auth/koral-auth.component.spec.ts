import { ComponentFixture, TestBed } from '@angular/core/testing';

import { KoralAuthComponent } from './koral-auth.component';

describe('KoralAuthComponent', () => {
  let component: KoralAuthComponent;
  let fixture: ComponentFixture<KoralAuthComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [KoralAuthComponent]
    });
    fixture = TestBed.createComponent(KoralAuthComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
