<template>
  <v-app id="inspire" dark>
    <v-content>
      <v-container fill-height>
        <v-layout row align-center justify-center>
          <v-flex xs12 sm8 md4>
            <v-card>
              <v-form v-model="valid" @submit.prevent="formSubmit" ref="form">
                <v-card-text>
                    <v-subheader>Account</v-subheader>
                    <v-text-field :rules="[v => !!v || 'Username cannot be blank']" v-model="user.username" dark color="pink" prepend-icon="person" label="Username" type="text"></v-text-field>
                    <v-text-field :rules="[v => !!v || 'Password cannot be blank']" v-model="user.password" dark color="pink" prepend-icon="lock" label="Password" type="password"></v-text-field>
                    <v-subheader>Personal Information</v-subheader>
                    <v-text-field :rules="[v => !!v || 'First Name cannot be blank']" v-model="user.first_name" dark color="pink" prepend-icon="assignment_ind" label="First Name" type="text"></v-text-field>
                    <v-text-field :rules="[v => !!v || 'Last Name cannot be blank']" v-model="user.last_name" dark color="pink" prepend-icon="assignment_ind" label="Last Name" type="text"></v-text-field>
                    <v-text-field v-model="user.email" dark color="pink" prepend-icon="email" label="Email" type="email"></v-text-field>
                </v-card-text>
                <v-card-actions>
                  <v-btn block flat color="pink" @click="$router.push('login')">Back to Login</v-btn>
                  <v-btn block flat color="pink" type="submit">Register</v-btn>
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
          first_name: null,
          last_name: null,
          email: null,
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
