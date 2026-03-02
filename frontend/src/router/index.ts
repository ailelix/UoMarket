import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import Login from '../views/Login.vue';
import Register from '../views/Register.vue';
import MarketPlace from '../views/Marketplace.vue';
import ProfileView from '../views/ProfileView.vue';

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path : '/login', name: 'Login', component: Login },
  { path : '/register', name: 'Register', component: Register },
  { path : '/marketplace', name: 'MarketPlace', component: MarketPlace },
  { path : '/profile', name: 'ProfileView', component: ProfileView },
  
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;