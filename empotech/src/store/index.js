import Vue from 'vue';
import Vuex from 'vuex';
import VuexPersistence from 'vuex-persist'

import state from './state'
import mutations from './mutations'
import actions from './actions'


Vue.use(Vuex);

const vuexLocal = new VuexPersistence({
  storage: window.localStorage,
  reducer: state => ({ user: state.user })
})

export default new Vuex.Store({
  state: {
    ...state
  },
  mutations: {
    ...mutations
  },
  actions: {
    ...actions
  },
  plugins: [vuexLocal.plugin]
});
