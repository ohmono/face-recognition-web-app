<template>
  <v-card class="mx-auto elevation-5 ma-1" max-width="344">
    <v-img src="../assets/img/juan.png" height="200px"></v-img>

    <v-card-title> Juan Cardona </v-card-title>

    <v-card-subtitle> El Mono </v-card-subtitle>

    <v-card-actions>
      <v-btn
        color="red darken-4"
        text
        href="https://github.com/ohmono"
        target="_blank"
      >
        <v-icon>mdi-github</v-icon>GITHUB
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
          Soy estudiante de ingeniería de sistemas en la Udea, trabajo
          actualmente como desarrollador Frontend, me gusta salir a caminar con
          mi perro Freezer, leer y comer fruta luego de fumar en ella. <br />
          <strong>Pdt:</strong> El de la foto no es Freezer :p
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