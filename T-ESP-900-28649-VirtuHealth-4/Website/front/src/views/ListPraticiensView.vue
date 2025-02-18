<template>
  <div class="particiens">
    <ul class="list-options">
      <li v-for="(user, index) in users" :key="index" class="list">
        <AppCard :user="user" />
      </li>
    </ul>
  </div>
</template>

<script>
import AppCard from "@/components/AppCard.vue";
import json from "/data.json";
export default {
  name: "ListParticiensView",
  components: {
    AppCard,
  },
  data() {
    return {
      users: json,
    };
  },
  methods: {},
};
</script>
<style scoped>
.particiens {
  display: flex;
  margin-bottom: 100px;
}
.list-options {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  list-style-type: none;
}
.list {
  margin: 20px;
}
</style>
