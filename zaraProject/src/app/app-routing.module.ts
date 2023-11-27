import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ProductComponent } from './product/product.component';
import { ShoppingBagComponent } from './shopping-bag/shopping-bag.component';

export const routes: Routes = [
  { path: 'products', component: ProductComponent },
  { path: 'shopping-bag', component: ShoppingBagComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }