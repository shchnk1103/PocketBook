<template>
  <div class="main-footer">
    <!-- 1 -->
    <div class="footer">
      <div class="detail-link" v-for="item in footer_1" :key="item.msg">
        <a href="#">
          <div>{{ item.msg }}</div>
        </a>
      </div>
    </div>
    <!-- 2 -->
    <div class="footer">
      <div class="detail-link" v-for="item in footer_2" :key="item.msg">
        <a href="#">
          <div>{{ item.msg }}</div>
        </a>
      </div>
    </div>
    <!-- 3 -->
    <div class="footer">
      <div class="detail-link">
        <a href="#">
          <div>English</div>
        </a>
      </div>
      <div class="detail-link">
        <div class="copyright">© 2022 Instagram from Meta</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "FooterBar",
  data() {
    return {
      footer_1: [
        { msg: "Meta" },
        { msg: "About" },
        { msg: "Blog" },
        { msg: "Jobs" },
        { msg: "Terms" },
        { msg: "Top Accounts" },
        { msg: "Hashtags" },
        { msg: "Locations" },
        { msg: "Instagram Lite" },
        { msg: "Contact Uploading & Non-Users" },
      ],
      footer_2: [
        { msg: "Dance" },
        { msg: "Food & Drink" },
        { msg: "Home & Garden" },
        { msg: "Music" },
        { msg: "Visual Arts" },
      ],
    };
  },
};
</script>

<style scoped>
.main-footer {
  width: 100%;
  height: 134px;
  margin-top: 24px;
  background-color: rgb(245, 245, 245);
}

.footer {
  display: flex;
  flex-direction: row;
  justify-content: center;
}

.detail-link {
  margin-left: 8px;
  margin-right: 8px;
  margin-bottom: 12px;
}

a {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica,
    Arial, sans-serif;
  text-decoration-line: none;
  font-weight: 400;
  line-height: 16px;
  font-size: 12px;
  margin: -2px 0 -3px;
  color: rgba(var(--f52, 142, 142, 142), 1);
  align-items: baseline;
}

a:hover {
  color: rgba(var(--f52, 142, 142, 142), 1);
}

.copyright {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica,
    Arial, sans-serif;
  font-weight: 400;
  line-height: 16px;
  font-size: 12px;
  margin: -2px 0 -3px;
  color: rgba(var(--f52, 142, 142, 142), 1);
  padding-top: 2px;
}
</style>
