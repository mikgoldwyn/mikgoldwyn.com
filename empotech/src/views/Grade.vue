<template>
  <v-app id="inspire" dark>
    <SnackBar/>
    <Navigation/>
    <v-content>
      <v-container fill-height>
        <v-layout justify-center fill-height>
          <v-flex
            sm12
          >
            <v-card>
              <v-card-title primary-text>
                <v-layout>
                  <v-flex>
                    <div class="headline">Grades</div>
                  </v-flex>
                </v-layout>
              </v-card-title>
              <v-card-text>
                <v-data-table
                  :headers="table.headers"
                  :items="table.items"
                >
                  <template v-slot:items="props">
                    <td class="text-xs-center">{{ props.item.score }}</td>
                    <td class="text-xs-center">{{ props.item.total }}</td>
                    <td class="text-xs-center">{{ props.item.type }}</td>
                  </template>
                </v-data-table>
              </v-card-text>
              <v-card-actions>
              </v-card-actions>
            </v-card>
          </v-flex>
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
    ...mapState(['user', 'grades']),

  },
  data: () => ({
    table: {
      headers: [
        { text: 'Score', value: 'score', align: 'center' },
        { text: 'Total', value: 'total', align: 'center' },
        { text: 'Type', value: 'type', align: 'center' },
      ],
      items: []
    }
  }),
  methods: {
    ...mapActions(['showSnackbar', 'logout', 'getGrades']),

  },
  created () {

    if (this.user.is_superuser) {
      this.logout()
    }

    this.getGrades()
      .then(() => {
        this.table.items = this.grades
      })
  },
}
</script>
