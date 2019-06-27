<template>
  <div>
    <v-navigation-drawer
      v-model="drawer"
      fixed
      clipped
      app
    >
      <v-list >
        <v-list-tile  @click="$router.push({ name: 'home' })">
          <v-list-tile-action>
            <v-icon>playlist_add</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>
              Attendance
            </v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-list-tile  v-if="! user.is_superuser" @click="$router.push({ name: 'grade' })">
          <v-list-tile-action>
            <v-icon>grade</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>
              Grade
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
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
import SnackBar from '@/components/SnackBar.vue'

export default {
  components: {
    SnackBar
  },
  watch: {
    user (oldData, newData) {
      if (! this.user.id) {
        this.$router.push({ name: 'login' })
      }
    }

  },
  computed: {
    ...mapState(['user']),
  },
  data: () => ({
    drawer: false,
  }),
  methods: {
    ...mapActions(['logout', 'getUserData']),
    performLogout () {
      this.logout()
    }
  },
  mounted () {

    if (this.user.id) {
      this.getUserData()
    }

  },
}
</script>
