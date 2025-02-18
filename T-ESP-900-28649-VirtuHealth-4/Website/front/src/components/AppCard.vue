<template>
  <div class="profil-cards">
    <div class="img-container" style="background-image: url(`${user.picture}`)">
      <img class="profil-img" :src="user.picture" />
    </div>
    <div class="title-profil">{{ user.name }} {{ user.lastname }}</div>
    <p class="profil-body">{{ user.university }}</p>
    <p class="profil-body">{{ user.email }}</p>
    <router-link class="options-links" to="/myprofil">
      <ButtonMain @click="goToProfil">See more</ButtonMain>
    </router-link>
  </div>
</template>
  
  <script>
import { mapMutations } from "vuex";
import ButtonMain from "@/components/ButtonMain.vue";
export default {
  components: {
    ButtonMain,
  },
  data() {
    return {};
  },
  methods: {
    goToProfil() {
      this.setSelectedUser(this.user);
    },
    ...mapMutations(["setSelectedUser"]),
  },
  props: {
    user: {
      type: Object,
      required: true,
    },
  },
};
</script>
  
  <style scoped>
.profil-cards {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  margin: auto;
  text-align: center;
  border: none 1px;
  border-radius: 35px;
  width: 400px;
}

.title-profil {
  color: grey;
  font-size: 18px;
}

.profil-img {
  border-top-right-radius: 35px;
  border-top-left-radius: 35px;
  width: 100%;
  height: 100%;
}
.img-container {
  width: 400px;
  height: 500px;
  overflow: hidden;
  background-size: cover;
}
</style>
  