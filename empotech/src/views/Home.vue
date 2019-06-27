<template>
  <v-app id="inspire" dark>
    <SnackBar/>
    <Navigation/>
    <v-content>
      <v-container fill-height>
        <v-layout justify-center column>
          <v-flex
            v-if="! user.is_superuser"
            sm12
          >
            <v-card :color="QRCardProps.backgroundColor" :light="QRCardProps.isLight">
              <v-card-title primary-title>
                <v-layout>
                  <v-flex>
                    <div class="headline">Attendance QR Code</div>
                  </v-flex>
                </v-layout>
              </v-card-title>
              <v-card-text>
                <qr-code
                style="display: block;margin-left: auto;margin-right: auto;width: 200px;"
                :text="qrCodeValue"
                :size="200"
                error-level="L">
              </qr-code>
              </v-card-text>
              <v-card-actions>
                <v-layout>
                  <v-flex>
                    <v-btn flat color="pink" @click="toggleQRBackground">Toggle Background</v-btn>
                  </v-flex>
                </v-layout>
              </v-card-actions>
            </v-card>
          </v-flex>
          <v-flex
            v-if="! user.is_superuser"
            sm12
          >
            <v-card
              max-height="300"
              style="overflow-y: auto;"
            >
              <v-card-title primary-title>
                <v-layout>
                  <v-flex>
                    <div class="headline">Attendance</div>
                  </v-flex>
                </v-layout>
              </v-card-title>
              <v-card-text>
                <v-timeline>
                    <v-timeline-item
                      v-for="attendance in attendances"
                      :key="attendance.id"
                      color="pink"
                      icon="calendar_today"
                      large
                    >
                      <v-card class="elevation-4">
                        <v-card-title class="headline">
                          <v-layout>
                            <v-flex>
                              {{attendance.date_display}}
                            </v-flex>
                          </v-layout>
                        </v-card-title>
                      </v-card>
                    </v-timeline-item>
                  </v-timeline>
              </v-card-text>
              <v-card-actions>

              </v-card-actions>
            </v-card>
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
import { mapState, mapActions } from 'vuex';
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
    ...mapState(['user', 'apiURL', 'grades', 'attendances']),
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
    QRCardProps: {
      backgroundColor: "grey darken-3",
      isLight: false,
    }
  }),
  methods: {
    ...mapActions(['logout', 'showSnackbar', 'getGrades', 'getAttendances']),
    toggleQRBackground () {
      if (this.QRCardProps.backgroundColor == 'grey darken-3') {
        this.QRCardProps.backgroundColor = 'grey lighten-5'
        this.QRCardProps.isLight = true
      } else {
        this.QRCardProps.backgroundColor = 'grey darken-3'
        this.QRCardProps.isLight = false
      }
    },
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
  created () {
    this.codeReader
      .listVideoInputDevices()
      .then((videoInputDevices) => {
        videoInputDevices.forEach((device) => {
          this.videoDevices.push({ label: device.label, deviceID: device.deviceId })
        })
      })

    this.getAttendances()
  },
}
</script>
