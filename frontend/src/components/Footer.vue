<template>
  <!-- 1 -->
  <div class="footer">
    <div class="detail-link">
      <a href="#">
        <div>Meta</div>
      </a>
    </div>
    <div class="detail-link">
      <a href="#">
        <div>About</div>
      </a>
    </div>
    <div class="detail-link">
      <a href="#">
        <div>Blog</div>
      </a>
    </div>
    <div class="detail-link">
      <a href="#">
        <div>Jobs</div>
      </a>
    </div>
    <div class="detail-link">
      <a href="#">
        <div>Privacy</div>
      </a>
    </div>
    <div class="detail-link">
      <a href="#">
        <div>Terms</div>
      </a>
    </div>
    <div class="detail-link">
      <a href="#">
        <div>Top Accounts</div>
      </a>
    </div>
    <div class="detail-link">
      <a href="#">
        <div>Hashtags</div>
      </a>
    </div>
    <div class="detail-link">
      <a href="#">
        <div>Locations</div>
      </a>
    </div>
    <div class="detail-link">
      <a href="#">
        <div>Instagram Lite</div>
      </a>
    </div>
    <div class="detail-link">
      <a href="#">
        <div>Contact Uploading & Non-Users</div>
      </a>
    </div>
  </div>
  <!-- 2 -->
  <div class="footer">
    <div class="detail-link">
      <a href="#">
        <div>Dance</div>
      </a>
    </div>
    <div class="detail-link">
      <a href="#">
        <div>Food & Drink</div>
      </a>
    </div>
    <div class="detail-link">
      <a href="#">
        <div>Home & Garden</div>
      </a>
    </div>
    <div class="detail-link">
      <a href="#">
        <div>Music</div>
      </a>
    </div>
    <div class="detail-link">
      <a href="#">
        <div>Visual Arts</div>
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
</template>

<script>
export default {
  name: "FooterBar",
};
</script>

<style scoped>
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
