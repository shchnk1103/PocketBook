<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <LoginPages />
</template>

<script>
import LoginPages from "@/components/LoginPages";

export default {
  name: 'App',
  components: {
    LoginPages
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
