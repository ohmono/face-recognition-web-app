<template>
  <v-main class="grey lighten-3">
    <v-container>
      <v-row>
        <v-col cols="12" sm="8" class="animate__animated animate__fadeInLeft">
          <v-sheet min-height="50vh" rounded="lg" class="pa-10">
            <h1 style="text-align: center">
              <img src="../assets/logo_small.png" height="100px" alt="" />
            </h1>
            <br />
            <p style="text-align: justify">
              <span style="font-weight: 400">Como </span
              ><b>Proyecto Semestral </b
              ><span style="font-weight: 400">para la materia </span
              ><b>Estructuras de</b> <strong>Datos</strong>, en la
              <strong>Universidad de Antioquia</strong>,&nbsp;<span
                style="font-weight: 400"
                >se nos requiri&oacute;, a los estudiantes, proponer una
                aplicaci&oacute;n web o android que estuviese compuesta de un </span
              ><b>Backend</b><span style="font-weight: 400"> y un </span
              ><b>Frontend</b><span style="font-weight: 400">.</span>
            </p>
            <p style="text-align: justify">
              <span style="font-weight: 400"
                >Nuestro equipo propuso el desarrollo de una </span
              ><b>aplicaci&oacute;n web</b
              ><span style="font-weight: 400"> para la </span
              ><b>identificaci&oacute;n de g&eacute;nero</b
              ><span style="font-weight: 400">
                (masculino o femenino) con base en </span
              ><b>fotograf&iacute;as de rostros humanos</b
              ><span style="font-weight: 400">. </span>
            </p>
            <p style="text-align: justify">
              <span style="font-weight: 400"
                >En esta aplicaci&oacute;n se uso un modelo de </span
              ><b>Machine Learning</b
              ><span style="font-weight: 400">
                para la identificaci&oacute;n de g&eacute;nero en
                una&nbsp;</span
              ><b>API RESTful</b
              ><span style="font-weight: 400">, por parte del </span
              ><b>Backend </b><span style="font-weight: 400">y una </span
              ><b>P&aacute;gina Web</b
              ><span style="font-weight: 400">
                interactiva para la interacci&oacute;n de los usuarios con el
                modelo, por parte del </span
              ><b>Frontend</b><span style="font-weight: 400">.</span>
            </p>
          </v-sheet>
        </v-col>
        <v-col cols="12" sm="4" class="animate__animated animate__fadeInRight">
          <v-sheet min-height="50vh pa-5" rounded="lg">
            <Udea></Udea>
          </v-sheet>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>
<script>
import Udea from "../components/Udea.vue";
export default {
  components: { Udea },
};
</script>
