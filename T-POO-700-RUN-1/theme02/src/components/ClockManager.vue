<template>
<div>
    <div v-if="this.$session.exists() && this.$session.get('name')=='mama'">
       
        <!--h1> Welcome to your check-in area <b>{{showModal}} </b>!</h1><br-->
        <h1> Welcome to your check-in area!</h1><br>
        
        
        <div class="blocktext">
            <div class="container alert alert-primary">
                <h1>User's information </h1><br>
                <h3>Name: <b>{{this.user.username}}</b></h3>
                <h3>Email: <b>{{this.user.email}}</b></h3>
                <!--h3>moment: <b>{{this.date+" "+this.user.id+" "+this.status}}</b></h3-->
            </div>
        </div>
       
       <!-- Button trigger modal -->
<!--button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModalLong" @click="showModal==true">
  Launch demo modal
</button-->

<!-- Modal -->
<div  v-if="showModal==true" class="modal fade" id="exampleModalLong" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLongTitle">Modal title</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true"  @click="showModal==false">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <h1>My Modal</h1>
        <p>
            Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.
        </p>

      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-primary" data-dismiss="modal" @click="showModal==false">Close</button>
      </div>
    </div>
  </div>
</div>

       <form v-if="status==true">
        <div  class="container blocktext alert alert-success" id="container">
            
            <div class="form-check form-switch ">
                <input class="form-check-input" type="checkbox" id="flexSwitchCheckDefault" v-model="status" name="checkbox-1" unchecked-value="" @click="check(status)">
                <label class="form-check-label" for="flexSwitchCheckDefault" id="textcheck"> don't forget to click again to deactivate</label>
            </div>
        </div>
        </form>
        <form v-if="status==false">
        <div v-if="status==false" class="container blocktext alert alert-secondary" id="container">
            
            <div class="form-check form-switch ">
                <input class="form-check-input" type="checkbox" id="flexSwitchCheckDefault" v-model="status" name="checkbox-1" unchecked-value="" @click="check(status)">
                <label class="form-check-label" for="flexSwitchCheckDefault"> click here to activate scoring</label>
            </div>
        </div>
        </form>
       
        
        

    </div>
<div  v-else>
    <h1 class="alert alert-danger">
        Vous n'avez pas accés à cette page.<br> Si vous pensez que c'est une erreur, veuillez vous identifier en cliquant sur le boutton
        
    </h1>
    <button class="btn btn-primary"> S'identifier</button>
</div>
</div>

</template>
<script>
import axios from 'axios'
import moment from 'moment'

export default {
    name: 'ClockManager',
    data () {
        return {
            status:false,
            showModal:true,
            user: [],
            utilisateur:"",
            date: moment().format('YYYY-MM-DD hh:mm:ss'),
            
            
        }
    },
    mounted(){
      this.refreshData()
    },
    methods:{
        refreshData(){
              axios
              .get(`http://localhost:4000/api/users/${this.$route.params.id}`)
              .then((reponse) => {
                  this.user = reponse.data.data;
              })
            
        },
        refrechDate(){
            this.date= moment().format('YYYY-MM-DD hh:mm:ss') 
            
        },
        check(status){
            this.refrechDate(),
            this.status= !status,

            axios.post('http://localhost:4000/api/clocks',
                {"clock":
                    {"time":this.date,
                    "status":this.status,
                    "user_id":this.user.id
                    }
      },console.log(this.name_user))
      .catch(error => {
        this.errorMessage = error.message;
        console.error("There was an error!", error)
        
      })
      .then((reponse) => {
        this.refreshData()
        //alert("Ajout réussi")
      })

        }
    }
}
</script>
<style scoped>
#flexSwitchCheckDefault{
    margin-left: 50px;
    width: 50px;
    height: 50px;
}
#textcheck{
    margin-left: 0%;
}
#container {
                position: relative;
                text-align:center;
                margin:20px auto;
                width:80%;
                max-width:100%;
                height:100px;
            }
</style>
