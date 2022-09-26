<template>
  <div class="row" style="margin-bottom: 52px; display: flex; margin-top: 80px">
    <div class="container-fluid">
      <div class="row" style="margin-top: 24px">
        <div
          class="col"
          style="
            padding: 0;
            align-content: stretch;
            line-height: 18px;
            width: 10px;
          "
        >
          <a href="" class="a-custom">
            <div class="font-xl">Meta</div>
          </a>
        </div>
        <div
          class="col"
          style="
            padding: 0;
            align-content: stretch;
            line-height: 18px;
            width: 10px;
          "
        >
          <a href="" class="a-custom">
            <div class="font-xl">About</div>
          </a>
        </div>
        <div class="col">
          <a href="" class="a-custom">
            <div class="font-xl">Blog</div>
          </a>
        </div>
        <div class="col">
          <a href="" class="a-custom">
            <div class="font-xl">Jobs</div>
          </a>
        </div>
        <div class="col">
          <a href="" class="a-custom">
            <div class="font-xl">Help</div>
          </a>
        </div>
        <div class="col">
          <a href="" class="a-custom">
            <div class="font-xl">API</div>
          </a>
        </div>
        <div class="col">
          <a href="" class="a-custom">
            <div class="font-xl">Privacy</div>
          </a>
        </div>
        <div class="col">
          <a href="" class="a-custom">
            <div class="font-xl">Terms</div>
          </a>
        </div>
        <div class="col">
          <a href="" class="a-custom">
            <div class="font-xl">Top Accounts</div>
          </a>
        </div>
        <div class="col">
          <a href="" class="a-custom">
            <div class="font-xl">Hashtags</div>
          </a>
        </div>
        <div class="col">
          <a href="" class="a-custom">
            <div class="font-xl">Locations</div>
          </a>
        </div>
        <div class="col" style="padding: 0">
          <a href="" class="a-custom">
            <div class="font-xl">Instagram Lite</div>
          </a>
        </div>
        <div class="col">
          <a href="" class="a-custom">
            <div class="font-xl">Contact Uploading & Non-Users</div>
          </a>
        </div>
      </div>
      <div class="row">
        <div class="english">
          <span>English</span>
          <span style="margin-left: 16px">© 2022 Instagram from Meta</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "FooterBar",
};
</script>

<style scoped>
.font-xl {
  font-size: 12px;
  line-height: 16px;
  margin: -2px 0 -3px;
}

.a-custom {
  flex-direction: column;
  margin: 0;
  padding: 0;
  text-decoration: none;
}

.english {
  margin-top: 12px;
  margin-bottom: 12px;
  color: rgba(var(--f52, 142, 142, 142), 1);
  display: inline-block;
  cursor: pointer;
  position: relative;
  vertical-align: top;
  font-size: 12px;
  font-weight: 400;
  font-family: inherit;
}
</style>
