<template>
  <v-card class="mx-auto elevation-5 ma-1" max-width="344">
    <v-img src="../assets/img/carlos.png" height="200px"></v-img>

    <v-card-title> Carlos Zapata </v-card-title>

    <v-card-subtitle> Lorem </v-card-subtitle>

    <v-card-actions>
      <v-btn color="red darken-4" text
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
          I'm a thing. But, like most politicians, he promised more than he
          could deliver. You won't have time for sleeping, soldier, not with all
          the bed making you'll be doing. Then we'll go with that data file!
          Hey, you add a one and two zeros to that or we walk! You're going to
          do his laundry? I've got to find a way to escape.
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