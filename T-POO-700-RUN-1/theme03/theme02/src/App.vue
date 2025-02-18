<template>
  <div id="app">
    <!--nav class="navbar navbar-dark bg-primary" aria-label="First navbar example">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Never expand</a>
        <button @click="navbar()" class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarsExample01" aria-controls="navbarsExample01" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div v-if="navb==true">
          <ul class="navbar-nav me-auto mb-2">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="#">Home</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Link</a>
            </li>
            <li class="nav-item">
              <a class="nav-link disabled">Disabled</a>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="dropdown01" data-bs-toggle="dropdown" aria-expanded="false">Dropdown</a>
              <ul class="dropdown-menu" aria-labelledby="dropdown01">
                <li><a class="dropdown-item" href="#">Action</a></li>
                <li><a class="dropdown-item" href="#">Another action</a></li>
                <li><a class="dropdown-item" href="#">Something else here</a></li>
              </ul>
            </li>
          </ul>
          <form>
            <input class="form-control" type="text" placeholder="Search" aria-label="Search">
          </form>
        </div>
      </div>
    </nav-->
    <div id="connected" v-if="this.$session.exists()">
      <ul  class="nav justify-content-center">
        <li class="nav-item">
          <button class="btn btn-primary">Profile</button>
        </li>&nbsp;
        <li class="nav-item">
          <button @click="logout()" class="btn btn-primary">Logout</button>
        </li>
        <!--li class="nav-item ">
          <a class="nav-link active" aria-current="page" href="#">Active</a>
        </li>
        
        <li class="nav-item">
          <a class="nav-link" href="Logout">Link</a>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled">Disabled</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" data-bs-toggle="dropdown" href="#" role="button" aria-expanded="false">Dropdown</a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Separated link</a></li>
          </ul>
        </li-->
      </ul>
    </div>
      <img src="./assets/logo.png">
      <h1 v-if="this.$session.exists()">Bienvennue {{this.$session.get("token")}}</h1>
    
    <router-view/>
  </div>
</template>
<script>
  export default {
    name: 'App',
    data () {
      return {
        navb:false
        
      }
    },
    methods:{
      logout(){
        //alert("in logout")
        if(confirm("Are you sure you want to disconnect?")){
          this.$session.destroy()
          if(this.$session.exists()){
              alert("erreur: session non detruit")
          }
          else{
            this.$router.push('/')
          }
        }
        //alert(navb)
      }
    }
  }
</script>
<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
  .navbar {
    margin-bottom: 20px;
  }
</style>
