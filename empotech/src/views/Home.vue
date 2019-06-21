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
      <v-container fill-height align-content-center>
        <v-layout justify-center align-center>
          <v-flex
            v-if="! user.is_superuser"
            sm12
          >
            <qr-code
                style="display: block;margin-left: auto;margin-right: auto;width: 200px;"
                :text="qrCodeValue"
                :size="200"
                error-level="L">
            </qr-code>
          </v-flex>
          <v-flex
            sm12
            v-if="user.is_superuser"
          >
            <video
              v-if="selectedVideoDevice.deviceID"
              id="video"
              width="300"
              height="200"
              style="border: 1px solid gray"
            ></video>
            <v-select
              v-model="selectedVideoDevice"
              :items="videoDevices"
              item-text="label"
              return-object
            >
            </v-select>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import { mapState, mapActions } from "vuex";
import VueQRCodeComponent from 'vue-qrcode-component'
import { BrowserQRCodeReader } from '@zxing/library';
import SnackBar from '@/components/SnackBar.vue'

export default {
  components: {
    qrCode: VueQRCodeComponent,
    SnackBar
  },
  watch: {
    selectedVideoDevice (selectedVideoDevice) {

      if (selectedVideoDevice.deviceID) {
        this.codeReader
          .decodeFromInputVideoDevice(selectedVideoDevice.deviceID, 'video')
          .then((result) => {
            alert(result.text)
          })
      } else {
        this.codeReader.reset()
      }

    },
  },
  computed: {
    ...mapState(['user', 'apiURL']),
    qrCodeValue () {
      const userID = this.user.id
      return userID.toString()
    }
  },
  data: () => ({
    drawer: null,
    videoDevices: [{ label: 'Select a camera' }],
    codeReader: new BrowserQRCodeReader(),
    selectedVideoDevice: { label: 'Select a camera' },
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
    this.codeReader
      .listVideoInputDevices()
      .then((videoInputDevices) => {
        videoInputDevices.forEach((device) => {
          this.videoDevices.push({ label: device.label, deviceID: device.deviceId })
        })
      })

    if (this.user.id) {
      this.getUserData()
    }
  },
}
</script>
