<template>
  <div class="header">
    <div class="left-section">
      <img :src="InstagramImage" alt="" class="ins-img" />
    </div>
    <div class="right-section">
      <!-- Home -->
      <div class="nav-button">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="25"
          height="25"
          fill="currentColor"
          class="bi bi-house-door-fill"
          viewBox="0 0 16 16"
        >
          <path
            d="M6.5 14.5v-3.505c0-.245.25-.495.5-.495h2c.25 0 .5.25.5.5v3.5a.5.5 0 0 0 .5.5h4a.5.5 0 0 0 .5-.5v-7a.5.5 0 0 0-.146-.354L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293L8.354 1.146a.5.5 0 0 0-.708 0l-6 6A.5.5 0 0 0 1.5 7.5v7a.5.5 0 0 0 .5.5h4a.5.5 0 0 0 .5-.5z"
          />
        </svg>
        <div class="tooltip-home">Home</div>
      </div>
      <!-- Write -->
      <div class="nav-button">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="24"
          height="24"
          fill="currentColor"
          class="bi bi-pencil-square"
          viewBox="0 0 16 16"
        >
          <path
            d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"
          />
          <path
            fill-rule="evenodd"
            d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"
          />
        </svg>
        <div class="tooltip-write">Write</div>
      </div>
      <!-- Add -->
      <div class="nav-button">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="23"
          height="23"
          fill="currentColor"
          class="bi bi-plus-square"
          viewBox="0 0 16 16"
        >
          <path
            d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"
          />
          <path
            d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"
          />
        </svg>
        <div class="tooltip-add">Add</div>
      </div>
      <!-- Search -->
      <div class="nav-button">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="23"
          height="23"
          fill="currentColor"
          class="bi bi-search"
          viewBox="0 0 16 16"
        >
          <path
            d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"
          />
        </svg>
        <div class="tooltip-search">Search</div>
      </div>
      <!-- Account-image -->
      <div class="nav-button">
        <img :src="account_img" alt="" class="account-image" />
        <div class="account-status-bar">
          <img :src="account_img" alt="" class="info-account-image" />
          <div class="info-username">{{ username }}</div>
          <div class="info-email">{{ email }}</div>
          <div class="info-detail">Info</div>
          <div class="logout">Log out</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "NavBar",
  data() {
    return {
      InstagramImage: require("../assets/instagram.png"),
      token: "",
      username: "",
      account_img: "",
      email: "",
      Show: false,
    };
  },
  mounted() {
    const that = this;
    const storage = localStorage;
    const login_email = storage.getItem("useremail.pocketbook");

    that.token = storage.getItem("access.pocketbook");

    axios
      .get("http://localhost:8000/api/users/", {
        params: { search: login_email },
        headers: { Authorization: "Bearer " + that.token },
      })
      .then((response) => {
        const res = response.data.results[0];
        that.account_img = res.account_img;
        that.username = res.username;
        that.email = res.email;
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>

<style scoped>
.header {
  background-color: rgb(250, 250, 250);
  color: rgb(38, 38, 38);

  display: flex;
  flex-direction: row;
  height: 60px;
  justify-content: center;
  align-items: center;
  padding-left: 70px;
  padding-right: 70px;
}

.left-section {
  flex: 1;
}

.ins-img {
  height: 32px;
  cursor: pointer;
  margin-top: 2px;
}

.right-section {
  flex: 1;
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
}

.nav-button {
  margin-left: 22px;

  position: relative;

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.nav-button:hover .account-status-bar,
.nav-button:hover .tooltip-home,
.nav-button:hover .tooltip-write,
.nav-button:hover .tooltip-add,
.nav-button:hover .tooltip-search {
  opacity: 1;
}

.account-image {
  height: 24px;

  border-radius: 12px;
}

.nav-button .account-status-bar {
  background-color: rgb(225, 225, 225);
  border-radius: 6px;
  height: 250px;
  width: 200px;

  position: absolute;
  bottom: -260px;
  right: 0;

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  padding: 3px 5px;
  font-size: 12px;
  opacity: 0;
  transition: opacity 0.15s;
  pointer-events: none;
}

.nav-button .tooltip-home,
.nav-button .tooltip-write,
.nav-button .tooltip-add,
.nav-button .tooltip-search {
  font-size: 18px;

  display: flex;
  align-items: center;
  justify-content: center;

  position: absolute;
  bottom: -40px;

  background-color: rgb(225, 225, 225);
  border-radius: 6px;
  padding: 3px 10px;
  opacity: 0;
  transition: opacity 0.15s;
  pointer-events: none;
}

.info-account-image {
  width: 80px;
  border-radius: 40px;
  cursor: pointer;
}

.info-username {
  font-size: 18px;
  margin-top: 15px;
  cursor: pointer;
}

.info-email {
  color: gray;
  cursor: pointer;
}

.logout:hover {
  color: red;
  cursor: pointer;
}
</style>
