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

  getUserDataRequest(state) {
    state.loading = true;
  },
  getUserDataSuccess(state, data) {
    state.loading = false;
    state.user = data;
  },
  getUserDataFailure(state) {
    state.loading = false;
    state.user = {};
  },

  getGradesRequest(state) {
    state.loading = true;
  },
  getGradesSuccess(state, data) {
    state.loading = false;
    state.grades = data;
  },
  getGradesFailure(state) {
    state.loading = false;
    state.grades = [];
  },

  getAttendancesRequest(state) {
    state.loading = true;
  },
  getAttendancesSuccess(state, data) {
    state.loading = false;
    state.attendances = data;
  },
  getAttendancesFailure(state) {
    state.loading = false;
    state.attendances = [];
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
