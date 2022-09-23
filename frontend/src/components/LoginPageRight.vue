<template>
  <div class="col-5 align-items-center">
    <div class="right-page col needs-validation">
      <img :src="InstagramImage" alt="" class="ins-img" />
      <form class="needs-validation" novalidate>
        <!-- user_email -->
        <div class="btn-email">
          <input
            v-model="user_email"
            type="text"
            class="form-control"
            id="email"
            placeholder="Please enter your email."
            v-bind:class="{ 'is-invalid': emailError }"
            required
          />
          <div class="invalid-feedback text-to-left" v-if="errors[0]">
            {{ errors[0].message }}
          </div>
        </div>
        <!-- user_password -->
        <div class="btn-password">
          <input
            v-model="user_password"
            type="password"
            class="form-control"
            id="password"
            placeholder="Please enter your password"
            v-bind:class="{ 'is-invalid': passwordError }"
            required
          />
          <div class="invalid-feedback text-to-left" v-if="errors[0]">
            {{ errors[0].message }}
          </div>
        </div>
      </form>
      <!-- Login Button -->
      <button
        @click="login()"
        class="login-btn"
        :style="{ 'background-color': dynamicColor }"
        type="submit"
        :disabled="disabledFlag"
      >
        Log In
      </button>
      <!-- OR -->
      <div class="or-overall-arrangement">
        <div class="slash"></div>
        <div class="text-or">OR</div>
        <div class="slash"></div>
      </div>
      <!-- Log in with Facebook -->
      <div class="login-facebook-overall-arrangement">
        <span>Log in with Facebook</span>
      </div>
      <!-- Forget password? -->
      <div class="forget-password-btn">Forget password?</div>
    </div>
    <!-- Don't have an account? -->
    <div class="col account-overall-arrangement">
      Don't have an account?
      <span class="sign-up">Sign up?</span>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "LoginPageRight",
  data() {
    return {
      InstagramImage: require("../assets/instagram.png"),
      user_email: "",
      user_password: "",
      emailError: false,
      passwordError: false,
      errors: [],
      dynamicColor: "rgba(0, 149, 246, 0.3)",
      disabledFlag: true,
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
    validate() {
      const that = this;
      if (
        // eslint-disable-next-line no-useless-escape
        /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(that.user_email) &&
        that.user_password.length > 0
      ) {
        that.login;
      } else if (
        // eslint-disable-next-line no-useless-escape
        !/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(that.user_email)
      ) {
        that.emailError = true;
        that.errors.push({
          message: "Email is invalid.",
        });
      } else if (that.user_password.length <= 0) {
        that.passwordError = true;
        that.errors.push({
          message: "You must enter a password",
        });
      }
    },
  },
  computed: {
    userForm() {
      const { user_email, user_password } = this;
      return {
        user_email,
        user_password,
      };
    },
  },
  watch: {
    user_email: {
      handler(newValue) {
        if (
          // eslint-disable-next-line no-useless-escape
          /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(newValue)
        ) {
          this.emailError = false;
        } else {
          this.emailError = true;
          this.errors.push({
            message: "Email is invalid.",
          });
        }
      },
    },
    user_password: {
      handler(newValue) {
        if (newValue.length > 0) {
          this.passwordError = false;
        } else {
          this.passwordError = true;
          this.errors.push({
            message: "You must enter a password.",
          });
        }
      },
    },
    userForm: {
      handler(newValue) {
        console.log(newValue);
        if (
          newValue.user_email.length != 0 &&
          newValue.user_password.length != 0
        ) {
          this.dynamicColor = "rgba(var(--d69,0,149,246),1)";
          this.disabledFlag = false;
        }
      },
    },
  },
};
</script>

<style scoped>
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

.btn-email,
.btn-password {
  width: 100%;
  margin-top: 10px;
}

input {
  all: unset;
  padding: 10px;
  border: 1px solid rgba(219, 219, 219);
  border-radius: 4px;
  text-align: left;
  box-sizing: border-box;
  width: 100%;
  height: 100%;
}

.ins-img {
  padding: 0px 70px 30px 70px;
}

.text-to-left {
  text-align: left;
}

.login-btn {
  text-align: center;
  color: white;
  margin-top: 10px;
  border-radius: 5px;
  padding: 10px;
  border: 0px;
}

.text-or {
  font-weight: 600;
  color: gray;
  padding: 0px 20px 0px 20px;
}

.slash {
  background-color: rgb(219, 219, 219);
  height: 1px;
  width: 142px;
}

.forget-password-btn {
  color: rgb(0, 55, 107);
  text-align: center;
  padding-top: 20px;
}

.or-overall-arrangement {
  display: flex;
  margin-top: 30px;
  flex-direction: row;
  align-items: center;
}

.login-facebook-overall-arrangement {
  text-align: center;
  margin-top: 20px;
  color: rgb(56, 81, 133);
  font-weight: 600;
  font-size: 18px;
}

.account-overall-arrangement {
  background-color: white;
  border: 1px solid rgb(219, 219, 219);
  text-align: center;
  padding: 20px;
  margin: auto;
  margin-top: 20px;
  width: 350px;
}

.sign-up {
  color: rgba(0, 149, 246, 1);
  font-weight: 600;
}
</style>
