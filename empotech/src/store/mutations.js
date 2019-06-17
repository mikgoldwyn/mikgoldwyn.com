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

  logoutRequest(state) {
    state.loading = true;
  },
  logoutSuccess(state, data) {
    state.loading = false;
    state.user = {};
  },
  logoutFailure(state) {
    state.loading = false;
    state.user = {};
  },

  registerRequest(state) {
    state.loading = true;
  },
  registerSuccess(state, data) {
    state.loading = false;
  },
  registerFailure(state) {
    state.loading = false;
  },

  showSnackbarSuccess(state, message) {
    state.snackbar.message = message;
    state.snackbar.show = true;
  },
  hideSnackbarSuccess(state) {
    state.snackbar.message = null;
    state.snackbar.show = false;
  }
};
