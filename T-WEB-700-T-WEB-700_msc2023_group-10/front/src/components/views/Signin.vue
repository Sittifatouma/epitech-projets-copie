<template>
  <div id="login">
    <div class="container-fluid">
      <div class="row">
        <div class="col-md-6" id="left"><br><br>
          <span id="signin" class = "mx-auto">
            Don't have an account yet ? <router-link to="/Signup">sign up </router-link>
          </span><br><br>
          <h1 id="welcome" class="align-items-center">Welcome to Infocrypto</h1>
          <div class="form-signin">
            <form @submit.prevent="login(email,password)">
              <h1 class="mx-auto align-items-center">Please sign in</h1>
              <div class="form-floating">
                <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com" v-model="email" required>
                <label for="floatingInput">Email address</label><br>
              </div>
              <div class="form-floating">
                  <input type="password" class="form-control" id="floatingPassword" placeholder="Password" v-model="password" required>
                  <label for="floatingInput">Password</label><br>
              </div>
              <button type="submit" class="btn btn-primary">Sign in</button><br><br>
            </form>
          </div>
          <div class="form-signin ">
            Or Sign in with Google<br><br>
            <b-avatar id="img" :src="require('../../assets/google.png' )" variant="light" button  @click="loginGoogle()"></b-avatar>            
            <!--button type="submit" class="btn btn-primary" @click="logout()">Logout</button><br><br-->
          </div>
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
    name: 'Signin',
    data () {
      return {
      }
    },
    methods:{
      async logout() {
        if(confirm("Are you sure you want to disconnect?")){
          if(this.$gAuth.isAuthorized){
            const result = await this.$gAuth.signOut()
            console.log("result:",result)
          }
          localStorage.removeItem('token')
          this.$router.push({name: "Signin"})
        }
      },
      async loginGoogle() {
        const googleUser= await this.$gAuth.signIn();
        let self = this
        if(this.$gAuth.isAuthorized){
           axios.post('http://51.210.40.154:4000/api/users/createWithoutOnlyMail',
          {"email":googleUser.getBasicProfile().lv, })
          .then(function (response) {
            console.log("status: "+response.status)
            if (response.status === 201 || response.status === 200) {
              localStorage.setItem('token', response.data.token)
              localStorage.setItem('id', response.data.userID)
              
              self.$router.push({name: "Home"})
            } 
          })
          .catch(function (error) {
            console.log(error.message);
          });
        }
        else{
          alert("Error: we could not connect you, please try again");
        }
      },
      login:function(email,password){
        axios.post('http://51.210.40.154:4000/api/users/login/',
          {"email":email,
          "password":password
          }      
        )
        .then((response) => 
        {
          if (response.status === 200) {
            localStorage.setItem('token',response.data.token)
            localStorage.setItem('id', response.data.userId)
            console.log(response.data)
            this.$router.push({name: "Home"})
          } 
        })
        .catch(function (error) {
          alert("Error: we could not connect you, please check if the information entered is valid and try again");
          console.log(error);
        });
      }
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
