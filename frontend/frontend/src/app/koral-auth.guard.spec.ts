import { TestBed } from '@angular/core/testing';
import { CanActivateFn } from '@angular/router';

import { koralAuthGuard } from './koral-auth.guard';

describe('koralAuthGuard', () => {
  const executeGuard: CanActivateFn = (...guardParameters) => 
      TestBed.runInInjectionContext(() => koralAuthGuard(...guardParameters));

  beforeEach(() => {
    TestBed.configureTestingModule({});
  });

  it('should be created', () => {
    expect(executeGuard).toBeTruthy();
  });
});
