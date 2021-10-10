<template>
  <v-card class="mx-auto elevation-5 ma-1" max-width="344">
    <v-img src="../assets/img/udea.png" height="200px" contain> </v-img>

    <v-caard-text>
      <div style="text-align: center">
        <h3>Facultad de Ingenier&iacute;a</h3>
        <br />
        <p>Departamento de Ingenier&iacute;a de Sistemas</p>
        <p>Estructuras de Datos y Laboratorio&nbsp;</p>
        <p>2021-1</p>
      </div>
    </v-caard-text>

    <v-card-actions>
      <v-btn
        color="teal darken-4"
        text
        href="https://www.udea.edu.co"
        target="_blank"
      >
        <v-icon class="ma-1">mdi-school</v-icon>UdeA
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
          <p><strong>Proyecto creado por los estudiantes:</strong></p>
          <p>Juan Cardona</p>
          <p>Carlos Zapata</p>
          <p><strong>Presentado al profesor:&nbsp;</strong></p>
          <p>Luis Hernando Silva Florez</p>
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