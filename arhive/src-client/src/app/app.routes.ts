import { Routes } from '@angular/router';
import { AuthGuard } from './guards/auth.guard';

export const routes: Routes = [
    {
        path: "",
        loadComponent: () => import("./pages/layout/layout.component").then(c => c.LayoutComponent),
        canActivate: [AuthGuard],
        children: []
    },
    {
        path: "guard",
        loadComponent: () => import("./pages/guard/guard.component").then(c => c.GuardComponent),
    },
    {
        path: "callback",
        loadComponent: () => import("./pages/callback/callback.component").then(c => c.CallbackComponent),
    }
];
