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
              <template v-slot:expanded-item="{ headers, item }" class="pa-4">
                <td :colspan="headers.length" class="ma-4">
                  {{ item.info }}
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
              <template v-slot:expanded-item="{ headers, item }" class="pa-4">
                <td :colspan="headers.length">
                  {{ item.info }}
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
          info: "Vue JS como su nombre indica es un framework javascript, es decir, es un conjunto de herramientas y funciones que permiten desarrollar páginas web de una manera más cómoda. Vue nace con la necesidad de no tener que escribir tanto código javascript y sobre todo con la idea de ahorrar tiempo al programador.Vue fue creado por Evan You, ex-trabajador de Google, que decidió crear su propio framework en el año 2014. Desde entonces, Vue ha subido muchísimo de popularidad, gracias a su sencillez y a todo lo que puede ofrecer, que lo vamos a ver a continuación.",
        },
        {
          name: "JavaScript",
          logo: "js.svg",
          type: "Lenguaje de programación",
          info: "JavaScript es el lenguaje de programación que debes usar para añadir características interactivas a tu sitio web, (por ejemplo, juegos, eventos que ocurren cuando los botones son presionados o los datos son introducidos en los formularios, efectos de estilo dinámicos, animación, y mucho más). Este artículo te ayudará a comenzar con este lenguaje extraordinario y te dará una idea de qué es posible hacer con él.",
        },
        {
          name: "HTML",
          logo: "html.svg",
          type: "Lenguaje de marcado",
          info: "HTML (Lenguaje de Marcas de Hipertexto, del inglés HyperText Markup Language) es el componente más básico de la Web. Define el significado y la estructura del contenido web. Además de HTML, generalmente se utilizan otras tecnologías para describir la apariencia/presentación de una página web (CSS) o la funcionalidad/comportamiento (JavaScript). Hipertexto hace referencia a los enlaces que conectan páginas web entre sí, ya sea dentro de un único sitio web o entre sitios web. Los enlaces son un aspecto fundamental de la Web. Al subir contenido a Internet y vincularlo a las páginas creadas por otras personas, te conviertes en un participante activo en la «World Wide Web» (Red Informática Mundial).",
        },

        {
          name: "CSS",
          logo: "css.svg",
          type: "Lenguaje de diseño gráfico",
          info: "CSS (en inglés Cascading Style Sheets) es lo que se denomina lenguaje de hojas de estilo en cascada y se usa para estilizar elementos escritos en un lenguaje de marcado como HTML. CSS separa el contenido de la representación visual del sitio.",
        },
        {
          name: "Vuetify",
          logo: "vuetify.svg",
          type: "Librería UI para Vue.js",
          info: "Vuetify es un framework que combina la potencia del popular VueJs con la estética de Material Design. Permite acelerar el desarrollo de aplicaciones web complejas, incorporando una gran cantidad de componentes listos para usar. Vuetify se basa en el habitual sistema tipo grid para la ordenación del layout de la página. Dispone de una enorme librería de componentes que incluye desde elementos de formulario sencillos como botones, combobox, inputs, sliders, a componentes más avanzados típicos en aplicaciones Android como cards o snackbars.",
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
          name: "FastAPI",
          logo: "fastapi.svg",
          type: "Framework de Python",
          info: "FastAPI es un marco web moderno y rápido (de alto rendimiento) para crear API con Python 3.6+ basado en sugerencias de tipo Python estándar",
        },
        {
          name: "Python",
          logo: "python.png",
          type: "Lenguaje de programación",
          info: "Python es un lenguaje de programación de alto nivel que se utiliza para desarrollar aplicaciones de todo tipo. A diferencia de otros lenguajes como Java o .NET, se trata de un lenguaje interpretado, es decir, que no es necesario compilarlo para ejecutar las aplicaciones escritas en Python, sino que se ejecutan directamente por el ordenador utilizando un programa denominado interpretador, por lo que no es necesario “traducirlo” a lenguaje máquina. ",
        },
        {
          name: "Matplotlib",
          logo: "matplotlib.png",
          type: "Librería para generación de gráficos",
          info: "Matplotlib es una biblioteca para la generación de gráficos a partir de datos contenidos en listas o arrays en el lenguaje de programación Python y su extensión matemática NumPy.Proporciona una API, pylab, diseñada para recordar a la de MATLAB.",
        },

        {
          name: "NumPy",
          logo: "numpy.png",
          type: "Librería de operaciones matemáticas y estadísticas",
          info: "NumPy es una librería de Python especializada en el cálculo numérico y el análisis de datos, especialmente para un gran volumen de datos. Incorpora una nueva clase de objetos llamados arrays que permite representar colecciones de datos de un mismo tipo en varias dimensiones, y funciones muy eficientes para su manipulación.",
        },
        {
          name: "Pandas",
          logo: "pandas.png",
          type: "Librería para manipulación y análisis de datos",
          info: "En Computación y Ciencia de datos, pandas es una biblioteca de software escrita como extensión de NumPy para manipulación y análisis de datos para el lenguaje de programación Python. En particular, ofrece estructuras de datos y operaciones para manipular tablas numéricas y series temporales.",
        },
        {
          name: "OpenCV",
          logo: "opencv.png",
          type: "Librería de visión artificial",
          info: "OpenCV es una biblioteca libre de visión artificial originalmente desarrollada por Intel. OpenCV significa Open Computer Vision (Visión Artificial Abierta). Desde que apareció su primera versión alfa en el mes de enero de 1999, se ha utilizado en una gran cantidad de aplicaciones, y hasta 2020 se la sigue mencionando como la biblioteca más popular de visión artificial.1​ Detección de movimiento, reconocimiento de objetos, reconstrucción 3D a partir de imágenes, son sólo algunos ejemplos de aplicaciones de OpenCV.",
        },
        {
          name: "ScikitLearn",
          logo: "scikitlearn.png",
          type: "Librería de ML para aprendizaje automático",
          info: "Scikit-learn (anteriormente scikits.learn) es una biblioteca para aprendizaje automático de software libre para el lenguaje de programación Python. ​Incluye varios algoritmos de clasificación, regresión y análisis de grupos entre los cuales están máquinas de vectores de soporte, bosques aleatorios, Gradient boosting, K-means y DBSCAN. Está diseñada para interoperar con las bibliotecas numéricas y científicas NumPy y SciPy.",
        },
      ],
    };
  },
};
</script>
