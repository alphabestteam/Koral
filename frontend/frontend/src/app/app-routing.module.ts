import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { ProductComponent } from './product/product.component';
import { MainPageComponent } from './main-page/main-page.component';
import { BasketComponent } from './basket/basket.component';
import { AboutComponent } from './about/about.component';
import { ContactComponent } from './contact/contact.component';
import { KoralAuthComponent } from './koral-auth/koral-auth.component';
import { KoralAuthGuard } from './koral-auth.guard';
import { AuthGuard } from './auth.guard';


const routes: Routes = [
  { path: '', redirectTo: '/login', pathMatch: 'full' },
  { path: 'cant-come-inside', component: KoralAuthComponent, canActivate: [AuthGuard, KoralAuthGuard] },
  { path: 'main', component: MainPageComponent, canActivate: [AuthGuard] },
  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'contact', component: ContactComponent, canActivate: [AuthGuard]},
  { path: 'about', component: AboutComponent, canActivate: [AuthGuard] },
  { path: 'basket', component: BasketComponent, canActivate: [AuthGuard] },

  { path: 'basket', component: BasketComponent, canActivate: [AuthGuard] },
  {
    path: 'products/:gender', // Dynamic segment for gender
    component: ProductComponent, // Component to display products
    canActivate: [AuthGuard]
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
