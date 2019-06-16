import Vue from 'vue';
import Vuetify from 'vuetify';
import App from './App.vue';

import router from './router';
import store from './store/';
import './registerServiceWorker';

import 'material-design-icons-iconfont/dist/material-design-icons.css';
import 'vuetify/dist/vuetify.min.css';

Vue.config.productionTip = false;

Vue.use(Vuetify);

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.headers.post['Content-Type'] = 'application/json';

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');
