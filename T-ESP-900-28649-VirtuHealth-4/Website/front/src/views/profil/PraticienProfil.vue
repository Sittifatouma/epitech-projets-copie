<template>
  <div class="my-profil">
    <div class="side-drawer">
      <button class="button">Ctacter</button>
    </div>
    <div class="profil-card">
      <h3>Dr. Jean-Claude Dupont</h3>
      <div class="profil-detail">
        <img
          src="/img/praticien.jpg"
          alt="Profile Picture"
          class="profil-picture"
          width="350"
        />
        <p>Nombre de patients : 32</p>
        <p>Mode de paiment : carte bancaire</p>
        <p>Psychiatre/psychologue</p>
      </div>
    </div>
    <div></div>
  </div>
</template>
    
    <script>
export default {
  data() {
    return {};
  },
  methods: {
    open() {},
    close() {},
  },
  components: {},
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
    