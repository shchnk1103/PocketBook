<template>
  <div class="container-fluid text-center main-page">
    <div class="row justify-content-md-center">
      <div class="col-1"></div>
      <!-- Left -->
      <div class="col-5 left align-items-center">
        <img :src="images" alt="" class="img-fluid login-img" />
      </div>
      <!-- Right -->
      <LoginPageRight />
      <div class="col-1"></div>
    </div>
  </div>
</template>

<script>
import LoginPageRight from "@/components/LoginPageRight.vue";

export default {
  name: "LoginPage",
  data() {
    return {
      images: require("../assets/phone.png"),
    };
  },
  components: {
    LoginPageRight,
  },
};
</script>

<style scoped>
.main-page {
  padding-top: 10%;
}

.left {
  display: flex;
  padding: 0;
  margin: 0;
  align-content: center;
  height: 582px;
  width: 430px;
  background-repeat: no-repeat;
  background-size: 468px 634px;
  background-image: url(https://www.instagram.com/static/images/homepage/phones/home-phones-2x.png/cbc7174b4f05.png);
}

.login-img {
  position: relative;
  top: 1%;
  left: 35.5%;
  width: 260px;
  height: 540px;
}
</style>
