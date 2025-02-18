<template>
  <div class="hello">
      <main class="form-signin">
          <form @submit.prevent="signRegister(nom,email,password,password_confirmation)">
              <h1>Please sign up</h1>
              <div class="form-floating">
                <input type="text" class="form-control" id="floatingInput" placeholder="text" v-model="nom" required>
                <label for="floatingInput">Username</label><br>
              </div>
              <div class="form-floating">
                <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com" v-model="email" required>
                <label for="floatingInput">Email address</label><br>
              </div>
              <div class="form-floating">
                  <input type="password" class="form-control" id="floatingPassword" placeholder="Password" v-model="password" required>
                  <label for="floatingInput">Password</label>
              </div>
              <div class="form-floating">
                  <input type="password" class="form-control" id="floatingPassword" placeholder="Password" v-model="password_confirmation" required>
                  <label for="floatingPassword">password_confirmation</label>
              </div>
                <button class="w-100 btn btn-lg btn-primary" type="submit">Sign up</button>
          </form>
      </main>
  </div>
</template>

<script>
import axios from 'axios'
export default {

    name: 'Register',
    data () {
        return {
            msg: 'Create your account',
            token: null,
            users: []

        }
    },
    methods:{
        signRegister(nom,email,password,password_confirmation){
            // insert in registry table
            axios.post('http://localhost:4000/api/auth/register',
            {"email":email, "password":password, "password_confirmation":password_confirmation})
              .then((reponse) => 
              { this.token = reponse.data.token
        
               // insert in role table
               alert(this.token),
               axios.post('http://localhost:4000/api/users',
               {"role": {"username":nom, "email":email,"role": "employee"}},
               {headers: { Authorization: 'Bearer ' + this.token }})
               
            }),

            // push to login page
            this.$router.push('/')
        }
        }   
}
</script>

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