export default {
  snackbar: {
    show: false,
    message: null,
  },
  loading: false,
  user: {},
  grades: [],
  attendances: [],
  apiURL: () => {
    const urlFragments = window.location.host.split('.');
    urlFragments[0] = 'api';
    return `${window.location.protocol}//${urlFragments.join('.')}`;
  },
};
