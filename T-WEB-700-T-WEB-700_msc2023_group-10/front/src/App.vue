

<template>
  <div id="app">
    <router-view/>
  </div>
  
</template>

<script>

export default {
  name: 'App',
  components: {
  }
}
</script>

<style>

@import url('https://fonts.googleapis.com/css2?family=Ubuntu:wght@300;500;700&display=swap');

:root{
  --blue: #0167FF
}

*{
  margin: 0; 
  padding: 0;
  font-family: 'Ubuntu', sans-serif;
  box-sizing: border-box;
}

#app {
  width: 100vw;
  height: 100vh;
}


</style>
