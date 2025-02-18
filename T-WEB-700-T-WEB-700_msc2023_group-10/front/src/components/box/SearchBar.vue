<template>
  <div class="search_bar_content">
    <select class="search_bar"></select>
  </div>
</template>

<script>
import $ from "jquery";
import "select2";
import "select2/dist/css/select2.css";
import axios from "axios";

export default {
  
  mounted: function() {
    axios
      .get("http://51.210.40.154:4000/api/cryptos/list")
      .then(function (response) {
        return response
      })
      .catch(function (error) {
        // handle error
        console.log(error);
      })
      .then(function(data) {
        return data.data.map((e) => {
          return {
            id: e.id,
            text: e.full_name
          }
        }) 
      })
      .then(function (data) {
        $(document).ready(function () {
          $(".search_bar").select2({
            placeholder: "Research",
            data: data
          });
        });
      });
  },
};
</script>

<style>
.search_bar_content {
  width: 100%;
}

.search_bar_content .search_bar {
  width: 100%;
}
</style>
