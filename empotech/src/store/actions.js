import axios from 'axios';


export default {
  login({ commit }, { username, password }) {
    const urlFragments = document.host.split('.');
    urlFragments[0] = 'api';
    const url = urlFragments.join('.');
    commit('loginRequest');
    return axios
      .post(`${url}/login/`, { username, password })
      .then((response) => {
        commit('loginSuccess', response.data);
        return response;
      })
      .catch((error) => {
        commit('loginFailure', error);
        throw error;
      });
  },
};
