<template>
  <div class="main">
      <div class="user_component">
            <img :src="require(`../../assets/${this.imgAvatar}`)" >
            <h1>{{this.lastname}} {{this.firstname}}</h1>
            <h3 v-if="!this.connex" class="connex" ><router-link to="/Signin">Sign in </router-link ></h3>
            <h3 v-if="this.connex" class="connex" @click="logout()"><router-link to="">Sign out </router-link ></h3>
      </div>
      <div class="link_component">
            <div class="home">
                <Icon icon="akar-icons:home" color="white" class="icon"/>
                <router-link to="Home" class="link">Home</router-link>
            </div>
            <div class="list" v-if="this.connex">
                <Icon icon="akar-icons:heart" color="white" class="icon"/>
                <router-link to="Favorite" class="link">FAV</router-link>
            </div>
            <div class="favorite">
                <Icon icon="bi:list-nested" color="white" class="icon"/>
                <router-link to="List" class="link">Liste</router-link>
            </div>
      </div>
  </div>
</template>

<script>
  import axios from "axios"
  import { Icon } from '@iconify/vue2';



export default {
    components: {
        Icon
    },
   
    data () {
      return {
          firstname:"",
          lastname:"",
          imgAvatar:"lion.png",
          connex:false
      }
      
    },
    mounted: function () {
        console.log(this.connex)
        console.log("id "+localStorage.getItem('id'))
        if(localStorage.getItem('id')){
            axios.get(`http://51.210.40.154:4000/api/users/`+localStorage.getItem('id'), 
                {  headers: { Authorization: 'Bearer ' + localStorage.getItem('token')}}
                )
                .catch(error => {
                    this.errorMessage = error.message;
                    console.error("There was an error!", error)
                    
                })
                .then((response) => {
                    console.log(response.data)
                    this.connex = true
                    this.firstname = response.data.firstname,
                    this.lastname = response.data.lastname
                    this.imgAvatar= response.data.avatar
                    console.log(this.connex)
                })
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
          localStorage.removeItem('id')
          this.$router.push({name: "Signin"})
        }
      }
    }
    
}
</script>

<style scoped>

*{
    color: white;
}

.main {
    flex: 1;
    height: 100%;
    background: var(--blue);
    display: flex;
    flex-direction: column;
    border-top-right-radius: 5px;
    border-bottom-right-radius: 5px;
}

.main .user_component {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 30px 0;
}

.main .user_component img {
    width: 130px;
    height: 130px;
    margin-bottom: 20px;
}

.main .user_component h1 {
    text-align: center;
    font-size: 30px;
}

.main .link_component {
    flex: 3; 
    display: flex;
    flex-direction: column;
    justify-content: space-around;
}

.main .link_component>div {
    height: 80px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-top: solid white 1px;
    border-bottom: solid white 1px;
    
}

.main .link_component .icon {
    margin-right: 15px;
}

.main .link_component .link{
    font-size: 20px;
    text-decoration: none;
}

</style>