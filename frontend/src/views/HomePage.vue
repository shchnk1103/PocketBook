<template>
  <div class="main-page">
    <!-- Header -->
    <NavBar style="z-index: 100" />
    <!-- Main -->
    <MainPart />
  </div>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import MainPart from "@/components/MainPart.vue";

export default {
  name: "HomePage",
  components: {
    NavBar,
    MainPart,
  },
};
</script>

<style scoped>
body {
  background-color: rgb(245, 245, 245);
}
</style>
