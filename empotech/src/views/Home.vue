<template>
  <v-app id="inspire" dark>
    <SnackBar/>
    <Navigation/>
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
import axios from 'axios';
import { mapState, mapActions } from "vuex";
import VueQRCodeComponent from 'vue-qrcode-component'
import { BrowserQRCodeReader } from '@zxing/library';

import SnackBar from '@/components/SnackBar.vue'
import Navigation from '@/components/Navigation.vue'

export default {
  components: {
    qrCode: VueQRCodeComponent,
    SnackBar,
    Navigation,
  },
  watch: {
    selectedVideoDevice (selectedVideoDevice) {

      if (selectedVideoDevice.deviceID) {
        this.codeReader
          .decodeFromInputVideoDeviceContinuously(selectedVideoDevice.deviceID, 'video', (result, err) => {
            if (result) {
              axios.post(`${this.apiURL()}/empotech/user/${result}/add-attendance/`)
                .then((response) => {
                  const data = response.data
                  if (data.created) {
                    this.showSnackbar(`Attendance for ${data.user_full_name} successfully created`)
                    window.navigator.vibrate(200)
                  } else {
                    this.showSnackbar(`Attendance for ${data.user_full_name} already exists`)
                    window.navigator.vibrate(200)
                  }
                })
            }
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
    ...mapActions(['logout', 'showSnackbar']),
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
  },
}
</script>
