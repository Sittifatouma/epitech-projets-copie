<template>
  <div id="login">
    <div class="container-fluid">
      <div class="row">
        <div class="col-md-6" id="left"><br><br>
          <span id="signin">
            Do you already have an account ? <router-link to="/Signin">sign in </router-link >
          </span><br><br>
          <h1 id="welcome" class="align-items-center">Welcome to Infocrypto</h1>
          <main class="form-signin">
            <!--span id="signin" v-if="msg !=''" style="color:red"></span-->
            <form @submit.prevent="submit(lastname,firstname,email,password,password_confirmation)">
              <h1>Please sign up</h1>
              <div class="form-floating">
                <input type="text" class="form-control" id="floatingInput" placeholder="text" v-model="lastname" required>
                <label for="floatingInput">Last name</label><br>
              </div>
              <div class="form-floating">
                <input type="text" class="form-control" id="floatingInput" placeholder="text" v-model="firstname" required>
                <label for="floatingInput">First Name</label><br>
              </div>
              <div class="form-floating">
                <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com" v-model="email" required>
                <label for="floatingInput">Email address</label><br>
              </div>
              <div class="form-floating">
                  <input type="password" class="form-control" id="floatingPassword" placeholder="Password" v-model="password" required>
                  <label for="floatingInput">Password</label><br>
              </div>
              <div class="form-floating">
                  <input type="password" class="form-control" id="floatingPassword" placeholder="Password" v-model="password_confirmation" required>
                  <label for="floatingPassword">confirm your password</label><br>
              </div>
              <div> 
                <h1>Choose your avatar ... </h1><br>
                  <b-avatar-group size="5rem" overlap="0">
                    <b-avatar :src="require('../../assets/lion.png' )" variant="light" button @click="setNameAvatar('lion.png')" ></b-avatar>
                    <b-avatar :src="require('../../assets/aigle.png' )" variant="light" button @click="setNameAvatar('aigle.png')"></b-avatar>
                    <b-avatar :src="require('../../assets/antilope.png' )" variant="light" button @click="setNameAvatar('antilope.png')"></b-avatar>
                    <b-avatar :src="require('../../assets/crocodile.png' )" variant="light" button @click="setNameAvatar('crocodile.png')"></b-avatar>
                    <b-avatar :src="require('../../assets/perroquet.png' )" variant="light" button @click="setNameAvatar('perroquet.png')" ></b-avatar>
                    <b-avatar :src="require('../../assets/renard.png' )" variant="light" button @click="setNameAvatar('renard.png')"></b-avatar>
                    <b-avatar :src="require('../../assets/singe.png' )" variant="light" button @click="setNameAvatar('singe.png')"></b-avatar>
                  </b-avatar-group>
              </div><br>
              <button type="submit" class="btn btn-primary">Sign up</button>
            </form>
          </main>
        </div>
        <div class="col-md-6" id="right">
          <h1 id="textright" class="h-100 mx-auto align-items-center">Become inform about crypto ... </h1>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios"
export default {
  name: 'Signup',
  data () {
    return {
     imgAvatar:"lion.png", 
     msg:""
    }
  },
  methods:{
    setNameAvatar:function(myImgAvatar){
      this.imgAvatar=myImgAvatar
    },
    submit:function(lastname,firstname,email,password,password_confirmation){
      if(password_confirmation==password){
        axios.post('http://51.210.40.154:4000/api/users/',
          {"firstname":firstname, "lastname":lastname.toUpperCase(), "email":email, "password":password, "avatar":this.imgAvatar})
        .then((response) => 
        {
          if (response.status === 201) {
            //localStorage.setItem('token',response.data.token)
            //localStorage.setItem('id', response.data.userID)
            console.log(response.data )
            //console.log(localStorage.getItem('id'))
            alert("Votre compte a été crée avec succée! Vous allez etre redirigé dans une autre page pour vous connecté.")
            this.$router.push({name: "Signin"})
            //this.$router.push('Home')
          } 
        })
        .catch(function (error) {
          console.log(error);
        });
      }
      else{ 
        alert("password non confirmé")
      }
    },
  }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .template {
    height:100%;
    width:100%
  }
  .container-fluid {
    height: 100vh;
    width: 100vw;
  }
  .row{
    height: 100%;
  }
  #left {
    background-color: #FFFFFF;
  }
  #right {
    background: linear-gradient(0deg,  #6100FF 100%, #0167FF 100%);
  }
  #textright{
    font-family: Ubuntu;
    font-style: normal;
    font-weight: bold;
    font-size: 550%;
    display: flex;
    text-align: center;
    color: #FFFFFF;
  }
  #signin{
    display:table;
    margin:0 auto;
  }
   #welcome{
    font-family: Ubuntu;
    font-style: normal;
    font-weight: bold;
    font-size: 350%;
    line-height: 55px;
    align-items: center;
    text-align: center;
    line-height:2em;
    color: #000000;
  }
  #avatarchoose{
    position: absolute;
    width: 403px;
    height: 115px;
    left: 50px;
    top: 408px;
  }
  #id{
    width: 10%;
    height: 10%;
  }
  #textright2{
    font-family: Ubuntu;
    font-style: italic;
    font-weight: normal;
    font-size: 30px;
    align-items: center;
    text-align: center;
    color: #FFFFFF;
  }
  .form-signin{
    margin: 20%;
    margin-bottom: 20px;
    margin-top: 60px;
    text-align: center;
  }

</style>
