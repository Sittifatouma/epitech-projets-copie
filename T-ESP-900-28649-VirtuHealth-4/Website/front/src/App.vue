<template>
  <div class="flex-container">
    <AppBar />
    <AppFooter />
  </div>
</template>

<script>
import AppFooter from "@/components/AppFooter.vue";
import AppBar from "@/components/AppBar.vue";

export default {
  data() {
    return {};
  },
  components: {
    AppFooter,
    AppBar,
  },
};
</script>
<style>
#app {
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  font-weight: 400;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
body {
  margin: 0px;
}
.flex-container {
  display: flex;
  flex-direction: column;
}
</style>
