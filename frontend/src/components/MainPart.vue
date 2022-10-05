<template>
  <div class="main-content">
    <!-- Add button -->
    <div class="status-bar">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="50"
        height="50"
        fill="currentColor"
        class="bi bi-plus-circle-fill"
        viewBox="0 0 16 16"
      >
        <path
          d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8.5 4.5a.5.5 0 0 0-1 0v3h-3a.5.5 0 0 0 0 1h3v3a.5.5 0 0 0 1 0v-3h3a.5.5 0 0 0 0-1h-3v-3z"
        />
      </svg>
    </div>
    <!-- Detail-List -->
    <div class="detail-list">
      <div class="detail-item" v-for="item in pocket_book_list" :key="item">
        <div class="left-section">
          <img class="kind-img" src="@/assets/account-image.jpeg" alt="" />
          <div class="date-time">
            {{ formatted_time(item.time_of_occurrence) }}
          </div>
          <div class="title">{{ item.title }}</div>
          <div class="amount">¥ {{ item.amount }}</div>
        </div>
        <div class="right-section">
          <!-- edit-button -->
          <div class="edit-button">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="50"
              height="50"
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
          </div>
          <!-- delete-button -->
          <div class="delete-button">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="50"
              height="50"
              fill="currentColor"
              class="bi bi-x-circle"
              viewBox="0 0 16 16"
            >
              <path
                d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"
              />
              <path
                d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z"
              />
            </svg>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "MainPart",
  data() {
    return {
      pocket_book_list: [],
      token: "",
    };
  },
  methods: {
    formatted_time(iso_date_string) {
      const date = new Date(iso_date_string);
      return date.toLocaleDateString();
    },
  },
  mounted() {
    const that = this;
    const storage = localStorage;

    that.token = storage.getItem("access.pocketbook");

    axios
      .get("http://localhost:8000/api/pocketbooks/", {
        headers: { Authorization: "Bearer " + that.token },
      })
      .then((response) => {
        const data = response.data.results;
        that.pocket_book_list = data;
      });
  },
};
</script>

<style scoped>
.main-content {
  width: 100%;

  display: grid;
  grid-template-rows: 70px 1fr;
  justify-content: center;
  align-items: center;
}

.status-bar {
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  padding-right: 70px;
}

.detail-item {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;

  border: 2px solid black;
  border-radius: 55px;
  box-shadow: 10px 15px 40px rgb(245, 210, 210);
  height: 110px;
  width: 700px;
  margin: 10px 60px;

  transition: background-color 0.15s;
}

.detail-item:hover {
  background-color: rgb(245, 210, 210);
}

.left-section {
  width: 500px;
  display: flex;
  flex-direction: row;
  align-items: center;
}

.kind-img {
  height: 80px;
  border-radius: 40px;
  margin-left: 15px;
}

.title {
  height: 80px;
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 30px;
}

.amount {
  height: 80px;
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 25px;
  color: gray;
}

.date-time {
  height: 80px;
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 25px;
  font-weight: 200;
  color: gray;
  padding-left: 10px;
}

.right-section {
  display: flex;
  flex-direction: row;
}

.edit-button {
  margin-right: 10px;
  cursor: pointer;
}

.delete-button {
  margin-right: 15px;
  cursor: pointer;
}
</style>
