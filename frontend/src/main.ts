import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import './assets/main.css';

// Set up CSRF token when calling Django API
import axios from 'axios';
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

const app = createApp(App);
app.use(router);
app.mount('#app');