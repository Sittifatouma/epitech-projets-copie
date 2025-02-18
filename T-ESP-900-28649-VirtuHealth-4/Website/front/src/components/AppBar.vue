<template>
  <div class="navbar">
    <div class="navbar-options-left">
      <ul class="list-options">
        <li class="list">
          <router-link class="options-links" to="/home">Home</router-link>
          <router-link class="options-links" to="/praticiens">
            Nos Praticiens
          </router-link>
          <router-link class="options-links" to="/about">About</router-link>
        </li>
      </ul>
    </div>
    <div class="navbar-options-right" v-if="this.$route.path === `/praticiens`">
      <ul class="list-options">
        <li class="list">
          <div class="search-bar-wrapper">
            <font-awesome-icon icon="fa-magnifying-glass" class="icon" />
            <input
              class="searchbar"
              type="text"
              placeholder="Praticien, établissement..."
            />
            <button class="button">Rechercher</button>
          </div>
        </li>
      </ul>
    </div>
  </div>
  <router-view />
</template>

<script>
export default {
  data() {
    return {
      on: true,
    };
  },
};
</script>

<style scoped>
.navbar {
  background-color: #008cba;
  display: flex;
  justify-content: space-between;
  width: 100%;
}
.navbar-options-left .navbar-options-right {
  display: flex;
  list-style-type: none;
}

.list-options {
  list-style-type: none;
}

a {
  color: #f9f3ed;
  margin: 10px;
  text-decoration: none;
  font-size: 20px;
  font-weight: bold;
}

.list-options a:hover {
  color: #333;
}
.navbar-options-right .list-options {
}
.list {
  margin: 10px;
  display: flex;
}
.search-nav {
  border: none;
  width: 200px;
  height: 30px;
  border-radius: 15px;
  padding: 5px;
  border: none;
}
.searchbar {
  border: none;
  padding: 5px;
  border-top-left-radius: 15px;
  border-bottom-left-radius: 15px;
  font-size: 15px;
}
.searchbar:focus-visible {
  outline: 0px;
}

.search-bar-wrapper {
  display: flex;
  border-radius: 10px;
  background-color: white;
}
.button {
  background-color: white;
  border: none;
  width: 100px;
  border-top-right-radius: 10px;
  border-bottom-right-radius: 10px;
  font-size: 15px;
}
.button:hover {
  background-color: #008cba;
  color: white;
  border: solid 1px #ccc;
}
.icon {
  color: grey;
  margin: 15px 10px 10px 10px;
}
</style>
