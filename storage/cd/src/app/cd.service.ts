import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { CD } from 'src/cd';

@Injectable({
  providedIn: 'root'
})
export class CdService {

  private cds: CD[] = [
    { title: 'Toxicity', artist: 'System Of A Down', genre: 'Metal', price: 100 },
    { title: 'Mezmerize', artist: 'System Of A Down', genre: 'Metal', price: 90 },
    { title: 'Hypnotize', artist: 'System Of A Down', genre: 'Metal', price: 90 },
    { title: 'Steal The Album!', artist: 'System Of A Down', genre: 'Metal', price: 85 },
  ];

  constructor() {
    localStorage.setItem('cds', JSON.stringify(this.cds));
  }

  getAllCds(): Observable<any[]> {
    return of(this.cds);
  }
}
