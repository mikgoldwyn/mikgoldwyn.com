<template>
  <v-app id="inspire" dark>
    <SnackBar/>
    <v-content>
      <v-container fill-height>
        <v-layout row align-center justify-center>
          <v-flex xs12 sm8 md4>
            <v-card>
              <v-form v-model="valid" @submit.prevent="formSubmit" ref="form">
                <v-card-text>
                    <v-text-field
                      v-model="user_data.username"
                      dark color="pink"
                      prepend-icon="person"
                      label="Username"
                      type="text"
                      :rules="[v => !!v || 'Username cannot be blank']"
                    ></v-text-field>
                    <v-text-field
                      v-model="user_data.password"
                      dark color="pink"
                      prepend-icon="lock"
                      label="Password"
                      type="password"
                      :rules="[v => !!v || 'Password cannot be blank']"
                    ></v-text-field>
                </v-card-text>
                <v-card-actions>
                  <!-- <v-btn block flat color="pink" @click="$router.push({ name: 'registration' })">Register</v-btn> -->
                  <v-btn :loading="loading" block flat color="pink" type="submit">Login</v-btn>
                </v-card-actions>
              </v-form>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import SnackBar from '@/components/SnackBar.vue'

export default {
  components: {
    SnackBar
  },
  computed: {
    ...mapState(['snackbar', 'loading'])
  },
  data () {
    return {
      valid: false,
      user_data: {
        username: null,
        password: null,
      }
    }
  },
  methods: {
    ...mapActions(['login', 'showSnackbar']),
    formSubmit () {
      if (this.$refs.form.validate()) {
        this.login({ username: this.user_data.username, password: this.user_data.password })
          .then(() => {
            this.$router.push({ name: 'home' })
          })
          .catch(() => {
            this.showSnackbar('The username or password is incorrect')
          })
      }
    }
  },
}
</script>
