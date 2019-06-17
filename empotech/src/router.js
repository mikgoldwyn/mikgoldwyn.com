import Vue from 'vue';
import Router from 'vue-router';

import Home from './views/Home.vue';
import Login from './views/Login.vue';
import Register from './views/Register.vue';

import store from './store/'

Vue.use(Router);

const router = new Router({
  routes: [
    {
      path: '/home',
      name: 'home',
      component: Home,
    },
    {
      path: '/',
      name: 'login',
      component: Login,
    },
    {
      path: '/registration',
      name: 'register',
      component: Register,
    },
  ],
});

router.beforeEach((to, from, next) => {
  if ((to.name === 'login' || to.name === 'registration') && store.state.user.id) {
    return next({ name: 'home' });
  }

  return next();
});

export default router
