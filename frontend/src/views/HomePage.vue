<template>
  <div class="container-fluid">
    <!-- NavBar -->
    <div class="row">
      <nav class="navbar navbar-expand-lg bg-light">
        <div class="container-fluid">
          <a class="navbar-brand" href="#">Navbar</a>
          <button
            class="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="#">Home</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Link</a>
              </li>
            </ul>
            <form class="d-flex" role="search">
              <input
                class="form-control me-2"
                type="search"
                placeholder="Search"
                aria-label="Search"
              />
              <button class="btn btn-outline-success" type="submit">
                Search
              </button>
            </form>
            <button
              type="button"
              class="btn btn-outline-danger"
              style="margin-left: 8px"
              v-if="hasLogin"
            >
              {{ username }}
            </button>
            <button
              type="button"
              class="btn btn-outline-warning"
              style="margin-left: 8px"
              v-else
            >
              <router-link to="/" class="login-btn"> 登陆 </router-link>
            </button>
          </div>
        </div>
      </nav>
    </div>
    <!-- Main -->
    <div class="row"></div>
    <!-- Footer -->
    <div class="row"></div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "HomePage",
  data() {
    return {
      username: "",
      hasLogin: false,
    };
  },
  mounted() {
    const that = this;
    const storage = localStorage;
    const expiredTime = Number(storage.getItem("expiredTime.pocketbook"));
    const currentTime = new Date().getTime();
    const refreshToken = storage.getItem("refresh.pocketbook");
    that.username = storage.getItem("useremail.pocketbook");

    if (expiredTime > currentTime) {
      that.hasLogin = true;
    } else if (refreshToken != null) {
      axios
        .post("http://localhost:8000/api/token/refresh/", {
          refresh: refreshToken,
        })
        .then((response) => {
          // 获取headers中的时间
          var res = new XMLHttpRequest();
          res.open("GET", location, false);
          res.send(null);
          const date = res.getResponseHeader("Date");

          const nextExpiredTime = Date.parse(date) + 86400000;

          storage.setItem("access.pocketbook", response.data.access);
          storage.setItem("expiredTime.pocketbook", nextExpiredTime);
          storage.removeItem("refresh.pocketbook");

          that.hasLogin = true;
        })
        .catch((error) => {
          // storage.clear()
          console.log(error);
          that.hasLogin = false;
        });
    }
  },
};
</script>

<style scoped>
.login-btn {
  text-decoration: none;
  color: #ffc107;
}

.login-btn:hover {
  color: white;
}
</style>
