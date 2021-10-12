<template>
  <v-main class="grey lighten-3">
    <v-container>
      <v-row class="animate__animated animate__fadeInDown">
        <v-col class="white text-h3 text-center text--darken-5 elevation-10"
          >Sube una imágen
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" sm="2" class="animate__animated animate__fadeInLeft">
          <v-sheet rounded="lg" min-height="268">
            <!--  -->
          </v-sheet>
        </v-col>

        <v-col cols="12" sm="8" class="animate__animated animate__fadeInUp">
          <v-sheet min-height="70vh" rounded="lg" class="text-center">
            <v-file-input
              class="ma-5"
              truncate-length="15"
              @change="selected"
            ></v-file-input>
            <v-btn @click="uploadImage" v-show="select" class="ma-4"
              >Subir</v-btn
            >

            <span class="pa-4"
              ><v-img
                class="elevation-5"
                :src="`${url}img/${res_path}/0_${res_image}`"
                v-show="res_path"
                contain
              ></v-img
            ></span>
            <span class="pa-4"
              ><v-img
                class="elevation-5"
                :src="`${url}img/${res_path}/1_${res_image}`"
                v-show="res_path"
                contain
              ></v-img></span
          ></v-sheet>
        </v-col>

        <v-col cols="12" sm="2" class="animate__animated animate__fadeInRight">
          <v-sheet rounded="lg" min-height="268">
            <!--  -->
          </v-sheet>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>

<script>
import { UPLOAD_IMAGE } from "../store/actions.type";
import { API_URL } from "../common/config";

export default {
  data: () => ({
    select: false,
    url: API_URL,
    image: null,
    res_image: "",
    res_path: "",
  }),
  methods: {
    uploadImage() {
      let file = new FormData();
      file.append("image", this.image, this.image.name);
      this.$store.dispatch(UPLOAD_IMAGE, file).then((data) => {
        this.res_path = data.key;
        this.res_image = data.img;
      });
    },
    selected(event) {
      // console.log(event);
      this.select = true;
      this.image = event;
    },
  },
};
</script>

<style>
</style>