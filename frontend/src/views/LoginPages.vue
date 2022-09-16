<template>
  <div class="main-page">
    <!-- Left -->
    <div class="left">
      <div>
        <img :src="images" alt="" class="login-img" />
      </div>
    </div>
    <!-- Right -->
    <div class="right">
      <div class="right-page">
        <img :src="InstagramImage" alt="" style="padding: 0px 70px 30px 70px" />
        <input
          v-model="user_name"
          placeholder="Please enter your email."
          type="text"
        />
        <input
          v-model="user_password"
          placeholder="Please enter your password"
          type="password"
        />
        <!-- Login Button -->
        <div
          style="
            background-color: rgba(0, 149, 246, 0.3);
            text-align: center;
            color: white;
            margin-top: 10px;
            border-radius: 5px;
            padding: 10px;
          "
        >
          Log In
        </div>
        <!-- OR -->
        <div
          style="
            display: flex;
            margin-top: 30px;
            flex-direction: row;
            align-items: center;
          "
        >
          <div
            style="
              background-color: rgb(219, 219, 219);
              height: 1px;
              width: 142px;
            "
          ></div>
          <div
            style="font-weight: 600; color: gray; padding: 0px 20px 0px 20px"
          >
            OR
          </div>
          <div
            style="
              background-color: rgb(219, 219, 219);
              height: 1px;
              width: 142px;
            "
          ></div>
        </div>
        <!-- Log in with Facebook -->
        <div
          style="
            text-align: center;
            margin-top: 20px;
            color: rgb(56, 81, 133);
            font-weight: 600;
            font-size: 18px;
          "
        >
          <span>Log in with Facebook</span>
        </div>
        <!-- Forget password? -->
        <div
          style="color: rgb(0, 55, 107); text-align: center; padding-top: 20px"
        >
          Forget password?
        </div>
      </div>
      <!-- Don't have an account? -->
      <div
        style="
          background-color: white;
          border: 1px solid rgb(219, 219, 219);
          text-align: center;
          padding: 20px;
          margin: 20px;
        "
      >
        Don't have an account?
        <span style="color: rgba(0, 149, 246, 1); font-weight: 600"
          >Sign up?</span
        >
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "LoginPages",
  data() {
    return {
      images: require("../assets/phone.png"),
      InstagramImage: require("../assets/instagram.png"),
      user_name: "",
      user_password: "",
    };
  },
  mounted() {
    axios.get("http://localhost:8000/user-api/").then((res) => {
      console.log(res.data);
    });
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
  background-color: white;
  border: 1px solid rgb(219, 219, 219);
  padding: 40px;
  margin: 20px;
}
</style>
