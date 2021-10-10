<template>
  <v-main class="grey lighten-3">
    <v-container>
      <v-row class="animate__animated animate__fadeInDown">
        <v-col class="white text-h3 text-center text--darken-5 elevation-10"
          >Información de la Página
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" sm="4" class="animate__animated animate__fadeInLeft">
          <v-sheet rounded="lg" min-height="268">
            <v-col
              ><v-row class="ma-1 red--text text--darken-4 elevation-5">
                Programadores
              </v-row>
              <v-row> <Juan></Juan></v-row>
              <v-row> <Carlos></Carlos></v-row
            ></v-col>
          </v-sheet>
        </v-col>

        <v-col cols="12" sm="8" class="animate__animated animate__fadeInRight">
          <v-sheet min-height="70vh" rounded="lg">
            <!-- frontend Table -->
            <v-data-table
              :headers="headers"
              :items="tools"
              :single-expand="true"
              :expanded.sync="expanded"
              item-key="name"
              show-expand
              class="elevation-5 ma-2"
            >
              <template v-slot:[`item.logo`]="{ item }">
                <div class="pa-2">
                  <img
                    :src="require('../assets/img/icons/' + item.logo)"
                    height="75"
                  />
                </div>
              </template>

              <template v-slot:top>
                <v-toolbar flat>
                  <v-toolbar-title
                    ><strong>Tecnologías Frontend</strong>
                  </v-toolbar-title>
                  <v-spacer></v-spacer>
                </v-toolbar>
              </template>
              <template v-slot:expanded-item="{ headers, item }">
                <td :colspan="headers.length">
                  More info about {{ item.name }}
                </td>
              </template>
            </v-data-table>
            <!-- backend Table -->
            <!-- frontend Table -->
            <v-data-table
              :headers="headers2"
              :items="tools2"
              :single-expand="true"
              :expanded.sync="expanded2"
              item-key="name"
              show-expand
              class="elevation-5 ma-2"
            >
              <template v-slot:[`item.logo`]="{ item }">
                <div class="pa-2">
                  <img
                    :src="require('../assets/img/icons/' + item.logo)"
                    height="75"
                  />
                </div>
              </template>

              <template v-slot:top>
                <v-toolbar flat>
                  <v-toolbar-title
                    ><strong>Tecnologías Backend</strong>
                  </v-toolbar-title>
                  <v-spacer></v-spacer>
                </v-toolbar>
              </template>
              <template v-slot:expanded-item="{ headers, item }">
                <td :colspan="headers.length">
                  More info about {{ item.name }}
                </td>
              </template>
            </v-data-table>
            <!--  -->
          </v-sheet>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>

<script>
import Carlos from "../components/Carlos.vue";
import Juan from "../components/Juan.vue";
export default {
  components: { Juan, Carlos },
  data() {
    return {
      expanded: [],
      headers: [
        {
          text: "Tecnología",
          align: "start",
          sortable: true,
          value: "name",
        },
        { text: "Logo", value: "logo" },
        { text: "Tipo", value: "type" },
        { text: "Detalles", value: "data-table-expand" },
      ],
      tools: [
        {
          name: "Vue.js",
          logo: "vue.svg",
          type: "Famework de JavaScript, HTML y CSS",
        },
        {
          name: "JavaScript",
          logo: "js.svg",
          type: "Lenguaje de programación",
        },
        {
          name: "HTML",
          logo: "html.svg",
          type: "Lenguaje de marcado",
        },

        {
          name: "CSS",
          logo: "css.svg",
          type: "Lenguaje de diseño gráfico",
        },
        {
          name: "Vuetify",
          logo: "vuetify.svg",
          type: "Librería UI para Vue.js",
        },
      ],
      expanded2: [],
      headers2: [
        {
          text: "Tecnologías",
          align: "start",
          sortable: true,
          value: "name",
        },
        { text: "Logo", value: "logo" },
        { text: "Tipo", value: "type" },
        { text: "Detalles", value: "data-table-expand" },
      ],
      tools2: [
        {
          name: "Flask",
          logo: "flask.svg",
          type: "Framework de Python",
        },
        {
          name: "Python",
          logo: "python.png",
          type: "Lenguaje de programación",
        },
        {
          name: "Matplotlib",
          logo: "matplotlib.png",
          type: "Librería para generación de gráficos",
        },

        {
          name: "NumPy",
          logo: "numpy.png",
          type: "Librería de operaciones matemáticas y estadísticas",
        },
        {
          name: "Pandas",
          logo: "pandas.png",
          type: "Librería para manipulación y análisis de datos",
        },
        {
          name: "OpenCV",
          logo: "opencv.png",
          type: "Librería de visión artificial",
        },
        {
          name: "ScikitLearn",
          logo: "scikitlearn.png",
          type: "Librería de ML para aprendizaje automático",
        },
      ],
    };
  },
};
</script>
