<template>
  <div class="my-profil">
    <div class="side-drawer">
      <button class="button">Patients</button>
      <button class="button">Scénarios</button>
    </div>
    <div class="profil-card">
      <h3>Dr {{ selectedUser.name }} {{ selectedUser.lastname }}</h3>
      <div class="profil-detail">
        <img
          :src="selectedUser.picture"
          alt="Profile Picture"
          class="profil-picture"
          width="350"
        />
        <p>{{ selectedUser.university }}</p>
        <p>{{ selectedUser.email }}</p>
        <p>{{ selectedUser.degree }}</p>
      </div>
    </div>
    <div></div>
  </div>
</template>
  
  <script>
import { mapState } from "vuex";
export default {
  data() {
    return {
      user: "",
    };
  },
  methods: {
    open() {},
    close() {},
  },
  computed: {
    ...mapState(["selectedUser"]),
  },
};
</script>
  
  <style scoped>
.my-profil {
  display: flex;
  justify-content: space-between;
}
.profil-card {
  border: none 1px;
  border-radius: 15px;
  background-color: #ccc;
  margin: 15px;
  color: #333;
  width: 50vw;
}
.profil-detail {
}
.profil-navigation {
}
.button {
  border: none;
  width: 150px;
  height: 50px;
  background-color: #008cba;
  margin: 1px;
  border-top-right-radius: 10px;
  border-bottom-right-radius: 10px;
  text-decoration: none;
  font-size: 15px;
  font-weight: bold;
  color: white;
}
.button:hover {
  color: #333;
}

.side-drawer {
  display: flex;
  flex-direction: column;
  background-color: white;
}
.profil-picture {
  margin: 5px;
  border-radius: 30px;
}
</style>
  