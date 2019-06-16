import axios from 'axios';


export default {
  login({ commit, state }, { username, password }) {
    console.log(state)
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
};
