import axios from 'axios';


export default {
  login({ commit, state }, { username, password }) {
    commit('loginRequest');
    return axios
      .post(`${state.apiURL()}/empotech/login/`, { username, password })
      .then((response) => {
        commit('loginSuccess', response.data);
        return response;
      })
      .catch((error) => {
        commit('loginFailure', error);
        throw error;
      });
  },
  register({ commit, state }, student_data) {
    commit('registerRequest');
    return axios
      .post(`${state.apiURL()}/empotech/register/`, student_data)
      .then((response) => {
        commit('registerSuccess', response.data);
        return response;
      })
      .catch((error) => {
        commit('registerFailure', error);
        throw error;
      });
  },
  showSnackbar({ commit }, message) {
    commit('showSnackbarSuccess', message)
  },
  hideSnackbar({ commit }) {
    commit('hideSnackbarSuccess')
  }
};
