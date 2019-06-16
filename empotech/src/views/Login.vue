<template>
  <v-app id="inspire" dark>
    <v-content>
      <v-container fill-height>
        <v-layout row align-center justify-center>
          <v-flex xs12 sm8 md4>
            <v-card>
              <v-form v-model="valid" @submit.prevent="formSubmit" ref="form">
                <v-card-text>
                    <v-text-field
                      v-model="user.username"
                      dark color="pink"
                      prepend-icon="person"
                      label="Username"
                      type="text"
                      :rules="[v => !!v || 'Username cannot be blank']"
                    ></v-text-field>
                    <v-text-field
                      v-model="user.password"
                      dark color="pink"
                      prepend-icon="lock"
                      label="Password"
                      type="password"
                      :rules="[v => !!v || 'Password cannot be blank']"
                    ></v-text-field>
                </v-card-text>
                <v-card-actions>
                  <v-btn block flat color="pink" @click="$router.push('registration')">Register</v-btn>
                  <v-btn block flat color="pink" type="submit">Login</v-btn>
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
  export default {
    data () {
      return {
        valid: false,
        user: {
          username: null,
          password: null,
        }
      }
    },
    methods: {
      formSubmit () {
        this.$refs.form.validate()
      }
    },
  }
</script>
