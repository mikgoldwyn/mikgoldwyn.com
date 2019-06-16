/* eslint-disable */

export default {
  loginRequest(state) {
    state.loading = true;
  },
  loginSuccess(state, data) {
    state.loading = false;
    state.user = data;
  },
  loginFailure(state) {
    state.loading = false;
    state.user = {};
  },
};
