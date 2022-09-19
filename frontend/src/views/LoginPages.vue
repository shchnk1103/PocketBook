<template>
  <div class="container-fluid text-center main-page">
    <div class="row justify-content-md-center">
      <div class="col-1"></div>
      <!-- Left -->
      <div class="col-5 left align-items-center">
        <img :src="images" alt="" class="img-fluid login-img" />
      </div>
      <!-- Right -->
      <div class="col-5 align-items-center">
        <div class="right-page col needs-validation">
          <img
            :src="InstagramImage"
            alt=""
            style="padding: 0px 70px 30px 70px"
          />
          <form class="needs-validation" novalidate>
            <!-- user_email -->
            <div class="btn-email">
              <input
                v-model="user_email"
                type="text"
                class="form-control"
                id="exampleFormControlInput1"
                placeholder="Please enter your email."
                required
              />
              <div class="invalid-feedback">Please enter a email.</div>
            </div>
            <!-- user_password -->
            <div class="btn-password">
              <input
                v-model="user_password"
                type="password"
                class="form-control"
                id="exampleFormControlInput1"
                placeholder="Please enter your password"
                required
              />
              <div class="invalid-feedback">Please enter a password.</div>
            </div>
          </form>
          <!-- Login Button -->
          <div
            @click="login()"
            style="
              background-color: rgba(0, 149, 246, 0.3);
              text-align: center;
              color: white;
              margin-top: 10px;
              border-radius: 5px;
              padding: 10px;
            "
            type="submit"
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
            style="
              color: rgb(0, 55, 107);
              text-align: center;
              padding-top: 20px;
            "
          >
            Forget password?
          </div>
        </div>
        <!-- Don't have an account? -->
        <div
          class="col"
          style="
            background-color: white;
            border: 1px solid rgb(219, 219, 219);
            text-align: center;
            padding: 20px;
            margin: auto;
            margin-top: 20px;
            width: 350px;
          "
        >
          Don't have an account?
          <span style="color: rgba(0, 149, 246, 1); font-weight: 600"
            >Sign up?</span
          >
        </div>
      </div>
      <div class="col-1"></div>
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
      user_email: "",
      user_password: "",
    };
  },
  methods: {
    login() {
      const that = this;
      axios
        .post("http://localhost:8000/api/token/", {
          email: that.user_email,
          password: that.user_password,
        })
        .then((response) => {
          const storage = localStorage;
          // 过期时间. Django设置了1分钟, 所以加上了60000ms.
          // 之后要修改的地方
          const expiredTime = Date.parse(response.headers.date) + 60000;
          // Set localStorage
          storage.setItem("access.pocketbook", response.data.access);
          storage.setItem("refresh.pocketbook", response.data.refresh);
          storage.setItem("expiredTime.pocketbook", expiredTime);
          storage.setItem("useremail.pocketbook", that.user_email);
          // 之后要修改的地方
          that.$router.push({ name: "Test" });
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped>
.main-page {
  padding-top: 10%;
}

.btn-email,
.btn-password {
  width: 248px;
  margin-top: 10px;
}

input {
  all: unset;
  padding: 10px;
  border: 1px solid rgba(219, 219, 219);
  border-radius: 4px;
  text-align: left;
  width: 100%;
  height: 100%;
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
  margin: auto;
  margin-top: 20px;
}
</style>
