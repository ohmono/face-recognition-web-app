<template>
  <v-card class="mx-auto elevation-5 ma-1" max-width="344">
    <v-img src="../assets/img/carlos.png" height="200px"></v-img>

    <v-card-title> Carlos Zapata </v-card-title>

    <v-card-actions>
      <v-btn
        color="red darken-4"
        text
        href="https://github.com/ozapata2019"
        target="_blank"
        ><v-icon>mdi-github</v-icon> GITHUB
      </v-btn>

      <v-spacer></v-spacer>

      <v-btn icon @click="show = !show">
        <v-icon>{{ show ? "mdi-chevron-up" : "mdi-chevron-down" }}</v-icon>
      </v-btn>
    </v-card-actions>

    <v-expand-transition>
      <div v-show="show">
        <v-divider></v-divider>

        <v-card-text>
          Carlos Zapata Arango, estudiante de Ingenieria de sistemas,
          Universidad de Antioquia, vivo enla ciudad de Medellin me gustan los
          deportes extremos y practico Ciclomontañismo.
        </v-card-text>
      </div>
    </v-expand-transition>
  </v-card>
</template>
<script>
export default {
  data: () => ({
    show: false,
  }),
};
</script>