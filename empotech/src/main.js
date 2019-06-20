import Vue from 'vue';
import Vuetify from 'vuetify';
import axios from 'axios';
import App from './App.vue';

import router from './router';
import store from './store';
import './registerServiceWorker';

import 'material-design-icons-iconfont/dist/material-design-icons.css';
import 'vuetify/dist/vuetify.min.css';
import 'vue-qrcode-reader/dist/vue-qrcode-reader.css';
import 'vue-qrcode-reader/dist/vue-qrcode-reader.browser.js';


Vue.config.productionTip = false;

Vue.use(Vuetify);

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.headers.post['Content-Type'] = 'application/json';

axios.interceptors.request.use(
  function (config) {
    if (store.state.user.token) {
      config.headers['Authorization'] = `Token ${store.state.user.token}`
    }
    return config;
  },
  function (error) {
    return Promise.reject(error);
  }
);



new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');
