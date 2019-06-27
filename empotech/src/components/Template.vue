<template>
  <v-app id="inspire" dark>
    <SnackBar/>
    <Navigation/>
    <v-content>
      <v-container fill-height align-content-center>
        <v-layout justify-center column>

        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import axios from 'axios';
import { mapState, mapActions } from 'vuex';

import SnackBar from '@/components/SnackBar.vue'
import Navigation from '@/components/Navigation.vue'

export default {
  components: {
    SnackBar,
    Navigation,
  },
  watch: {

  },
  computed: {
    ...mapState(['user']),

  },
  data: () => ({

  }),
  methods: {
    ...mapActions(['showSnackbar']),

    }
  },
  created () {

  },
}
</script>
