<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-primary text-white">
    <div class="container justify-content-center">
      <a class="navbar-brand" href="/">
        <img src="../assets/logo.png" alt="Logo" class="logo">
        <span class="project-name">Nostradamovies</span>
      </a>
      
      
    </div>
  </nav>
</template>
  
  <script>
  export default {
    data() {
      return {
        showMenu: false
      }
    },
    methods: {
      toggleMenu() {
        this.showMenu = !this.showMenu
      }
    }
  }
</script>

<style scoped>
.logo {
  width: 100px;
  height: 100px;
  margin-right: 5px;
}

.project-name {
  font-weight: bold;
  text-transform: uppercase;
  margin-left: 5px;
}
</style>