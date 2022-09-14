<template>
  <h1>Login Page</h1>
  <div class="main-page">
    <div class="left">
      <div>
        <img :src="images" alt="" class="login-img" />
      </div>
    </div>

    <div class="right">
      <div class="right-page">
        <img :src="InstagramImage" alt="" style="padding: 0px 50px 0px 50px" />
        <input placeholder="Please enter your email." type="text" />
        <input placeholder="Please enter your password" type="password" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LoginPages",
  data() {
    return {
      images: require("../assets/phone.png"),
      InstagramImage: require("../assets/instagram.png"),
    };
  },
};
</script>

<style scoped>
input {
  all: unset;
  padding: 10px;
  border: 1px solid rgba(219, 219, 219);
  margin-top: 10px;
  text-align: left;
}

.main-page {
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  align-content: center;
  justify-content: center;
  align-items: center;
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
  top: 27px;
  left: 157px;
  width: 251px;
}

.right-page {
  display: flex;
  flex-direction: column;
  flex-wrap: nowrap;
  align-content: center;
  align-items: stretch;
  justify-content: center;
  width: 350px;
}
</style>
