import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import Login from '../views/Login.vue';
import MarketPlace from '../views/Marketplace.vue';

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path : '/login', name: 'Login', component: Login },
  { path : '/marketplace', name: 'MarketPlace', component: MarketPlace },
  
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;