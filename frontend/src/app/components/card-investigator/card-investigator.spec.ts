import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CardInvestigator } from './card-investigator';

describe('CardInvestigator', () => {
  let component: CardInvestigator;
  let fixture: ComponentFixture<CardInvestigator>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CardInvestigator],
    }).compileComponents();

    fixture = TestBed.createComponent(CardInvestigator);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
