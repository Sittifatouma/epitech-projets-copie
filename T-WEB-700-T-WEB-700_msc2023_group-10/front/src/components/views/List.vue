<template>
  <div class="home_page">
    <Navigation />
    <ListCrypto title="Crypto Market"/>
  </div>
</template>

<script>
import Navigation from "../box/Navigation.vue";
import ListCrypto from "../box/ListCrypto.vue";
import axios from "axios";

export default {
  components: {
    Navigation,
    ListCrypto,
  },
  data: function () {
    return {
      crypto: [],
    };
  },
  mounted: function () {
    const data = axios
      .get("http://51.210.40.154:4000/api/cryptos/")
      .then((reponse) => console.log(reponse.data));
    console.log(data)
  },
};
</script>

<style>
.home_page {
  display: flex;
  width: 100%;
  height: 100%;
}
</style>
