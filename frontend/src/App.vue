<template>
  <v-app id="inspire" class="animate__animated animate__zoomIn">
    <Nav></Nav>
    <!-- Routes -->
    <v-main class="grey lighten-3">
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
import Nav from "./components/Nav.vue";
export default {
  components: { Nav },
};
</script>
<!--  -->


