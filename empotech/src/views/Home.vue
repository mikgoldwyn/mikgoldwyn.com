<template>
  <v-app
    id="inspire"
    dark
  >
  <SnackBar
  />
    <v-navigation-drawer
      v-model="drawer"
      fixed
      clipped
      app
    >
      <v-list >
        <v-list-tile  @click="">
          <v-list-tile-action>
            <v-icon>playlist_add</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>
              Attendance
            </v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar
      color="#4DBA87"
      dense
      fixed
      clipped-left
      app
    >
      <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title class="mr-5 align-center">
        <span class="title">EmpoTech GinGerGrace</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-menu offset-y nudge-bottom="6">
        <template v-slot:activator="{ on }">
          <v-btn
            dark
            icon
            v-on="on"
          >
            <v-icon>more_vert</v-icon>
          </v-btn>
        </template>

        <v-list>
          <v-list-tile @click="performLogout()">
            <v-list-tile-title>Logout</v-list-tile-title>
          </v-list-tile>
        </v-list>
      </v-menu>
    </v-toolbar>
    <v-content>
      <v-container fill-height>
        <v-layout justify-center align-center>
          <qr-code
              v-if="! user.is_superuser"
              :text="studentEndpoint"
              :size="200"
              error-level="L">
          </qr-code>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import { mapState, mapActions } from "vuex";
import VueQRCodeComponent from 'vue-qrcode-component'
import SnackBar from '@/components/SnackBar.vue'

export default {
  components: {
    qrCode: VueQRCodeComponent,
    SnackBar
  },
  computed: {
    ...mapState(['user', 'apiURL']),
    studentEndpoint () {
      return `${this.apiURL()}/empotech/user/${this.user.id}/add-attendance/`
    }
  },
  data: () => ({
    drawer: null,
  }),
  methods: {
    ...mapActions(['logout', 'getUserData', 'showSnackbar']),
    performLogout () {
      this.logout()
        .then(() => {
          this.$router.push({ name: 'login' })
        })
        .catch(() => {
          this.$router.push({ name: 'login' })
        })
    }
  },
  mounted () {
    if (this.user.id) {
      this.getUserData()
    }
  },
}
</script>
