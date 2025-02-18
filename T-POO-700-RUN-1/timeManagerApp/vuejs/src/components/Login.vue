<template>
  <div class="hello">
    <h1></h1>
    
    <main class="form-signin">
  <form @submit.prevent="signInButtonPressed(email,password)">
    <h1 class="h3 mb-3 fw-normal">Please sign in</h1>
    <div class="form-floating">
      <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com" v-model="email" required>
      <label for="floatingInput">Email address</label><br>
    </div>
    <div class="form-floating">
      <input type="password" class="form-control" id="floatingPassword" placeholder="Password" v-model="password" required>
      <label for="floatingPassword">Password</label>
    </div>

    <div class="checkbox mb-3">
      <!--label>
        <input type="checkbox" value="remember-me"> Remember me
      </label-->
    </div>
    <button class="w-100 btn btn-lg btn-primary" type="submit">Sign in</button>
    </form><br>
    <h6>If you don't have an account yet, click on <b>Sign up</b> to create your account </h6>
  <router-link to="/Register">
   <button class="w-100 btn btn-lg btn-primary" type="submit">Sign up</button>
  </router-link>
      <p class="mt-5 mb-3 text-muted">&copy; 2021–2023</p>

</main>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      token: null,
      users:[]
      
    }
  },
  methods:{
    signInButtonPressed(email,password){
      axios.post('http://localhost:4000/api/auth/login',
      {"email":email,
       "password":password
      }      
      )
      .then((reponse) => {
          this.token = reponse.data.token
         // alert(this.token)
          this.$session.start()
          this.$session.set("token",this.token)
         
          //recuperation du role de l'user pour le mettre dans une session
          axios.get('http://localhost:4000/api/users/', 
          {  headers: { Authorization: 'Bearer ' + this.$session.get("token") }}
          )
          .catch(error => {
              this.errorMessage = error.message;
              console.error("There was an error!", error)
            
          })
          .then((reponse) => {
            //alert(reponse.data.data)
            //this.refreshData()
            //alert("Edition réussi")
            this.users= reponse.data.data
            for(var user in this.users){
              //alert(this.users[user].email)
              if( this.users[user].email == email){
                this.$session.set("role",this.users[user].role)
                //alert("id: "+this.users[user].id)
                this.$session.set("id",this.users[user].id)
                this.$session.set("name",this.users[user].username)
                this.$session.set("mail",this.users[user].email)
                //alert(" session id :"+this.$session.get("id"))
              }
            }
            if(this.$session.get("role")=="manager" || this.$session.get("role")=="directeur"){
              this.$router.push('User')
            }
            else{
              this.$router.push({ name: 'ClockManager', params: { id:this.$session.get("id")} })

            }
          })
          
          
          
          })
          .catch(error => {
            this.errorMessage = error.message;
            console.error("There was an error!", error)
            
          })


    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .bd-placeholder-img {
    font-size: 1.125rem;
    text-anchor: middle;
    -webkit-user-select: none;
    -moz-user-select: none;
    user-select: none;
  }

  @media (min-width: 768px) {
    .bd-placeholder-img-lg {
      font-size: 3.5rem;
    }
  }
  .form-signin {
  width: 100%;
  max-width: 330px;
  padding: 15px;
  margin: auto;
}

.form-signin .checkbox {
  font-weight: 400;
}

.form-signin .form-floating:focus-within {
  z-index: 2;
}

.form-signin input[type="email"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}

.form-signin input[type="password"] {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}

</style>
