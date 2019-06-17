<template>
  <v-app id="inspire" dark>
    <v-content>
      <v-container fill-height>
        <v-layout row align-center justify-center>
          <v-flex xs12 sm8 md4>
            <v-card>
                <v-card-text>
                  Home
                </v-card-text>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  data () {
    return {

    }
  },
  methods: {
    ...mapActions(['login']),
    formSubmit () {
      if (this.$refs.form.validate()) {
        this.login({ username: this.user_data.username, password: this.user_data.password })
      }
    }
  },
}
</script>
