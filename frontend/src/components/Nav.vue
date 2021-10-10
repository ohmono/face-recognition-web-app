<template>
  <v-app-bar app color="white" flat>
    <v-avatar color="transparent" size="50">
      <v-img
        src="../assets/logo.png"
        contain
        v-show="$vuetify.breakpoint.smAndDown"
      ></v-img>
    </v-avatar>

    <v-tabs centered class="ml-n9" color="grey darken-1">
      <v-tab v-for="(link, index) in links" :key="index" :to="link.path">
        <v-icon class="ma-2">{{ link.icon }}</v-icon
        >{{ link.name }}
      </v-tab>
    </v-tabs>

    <v-avatar class="hidden-sm-and-down" color="transparent" size="256" tile>
      <v-img src="../assets/logo_large.png" contain></v-img
    ></v-avatar>
  </v-app-bar>
</template>

<script>
export default {
  data: () => ({
    links: [
      {
        name: "Aplication",
        path: "/app",
        icon: "mdi-account-reactivate",
      },
      { name: "About", path: "/about", icon: "mdi-information" },
      { name: "Home", path: "/", icon: "mdi-home" },
    ],
  }),
};
</script>

<style>
</style>