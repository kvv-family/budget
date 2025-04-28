import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AnalysItemComponent } from './analys-item.component';

describe('AnalysItemComponent', () => {
  let component: AnalysItemComponent;
  let fixture: ComponentFixture<AnalysItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AnalysItemComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AnalysItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
