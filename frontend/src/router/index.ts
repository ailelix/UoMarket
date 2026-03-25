import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import Login from '../views/Login.vue';
import MarketPlace from '../views/Marketplace.vue';
import ProfileView from '../views/ProfileView.vue';
import ItemView from '../views/ItemView.vue';
import PostItem from '../views/PostItem.vue';
import EditItem from '../views/EditItem.vue';

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path : '/login', name: 'Login', component: Login },
  { path : '/marketplace', name: 'MarketPlace', component: MarketPlace },
  { path : '/profile', name: 'ProfileView', component: ProfileView },
  { path : '/item/', name: 'ItemView', component: ItemView },
  { path : '/listings/create', name: 'PostItem', component: PostItem },
  { path : '/edit-item', name: 'EditItem', component: EditItem },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;