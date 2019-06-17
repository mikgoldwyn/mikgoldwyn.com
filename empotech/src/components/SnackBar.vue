<template>
  <div class="snackbar">
    <v-snackbar
      v-model="snackbar.show"
      top
      :timeout="5000"
    >
      {{ snackbar.message }}
      <v-btn
        color="pink"
        flat
        @click="hideSnackbar()"
      >
        Close
      </v-btn>
    </v-snackbar>
  </div>
</template>
<script>
import { mapState, mapActions } from "vuex";

export default {
  name: 'HelloWorld',
  computed: {
    ...mapState(['snackbar'])
  },
  methods: {
    ...mapActions(['hideSnackbar'])
  }
};
</script>
