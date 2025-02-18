<template>
<div>
    <div v-if="this.$session.exists()">
       
        <div class="blocktext">
            <div class="container alert alert-primary">
                <h1>User's information </h1><br>
                <h3>Name: <b>{{this.user.username}}</b></h3>
                <h3>Email: <b>{{this.user.email}}</b></h3>
                <!--h3>moment: <b>{{this.date+" "+this.user.id+" "+this.status}}</b></h3-->
            </div>
        </div>

        <!--h1> Welcome to your check-in area <b>{{showModal}} </b>!</h1><br-->
        <br><h4>Please, click below to declare your working hour:: </h4><br>
        <br><h8>When you 're working', the buttom must indicated "Working time" </h8><br>
        <br><h8>When you don't working, the buttom must indicated "Resting time"  </h8><br><br>
        
        
    
       
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
                <label class="form-check-label" for="flexSwitchCheckDefault" id="textcheck"> Resting time</label>
            </div>
        </div>
        </form>
        <form v-if="status==false">
        <div v-if="status==false" class="container blocktext alert alert-secondary" id="container">
            
            <div class="form-check form-switch ">
                <input class="form-check-input" type="checkbox" id="flexSwitchCheckDefault" v-model="status" name="checkbox-1" unchecked-value="" @click="check(status)">
                <label class="form-check-label" for="flexSwitchCheckDefault"> Working time</label>
            </div>
        </div>
        </form>
       
        
        

    </div>
    <div  v-else>
        <h1 class="alert alert-danger">
            You do not have access to this page.<br> If you think this is a mistake, please identify yourself by clicking on the button
            
        </h1>
        <button class="btn btn-primary" @click="logout()"> Sign in</button>
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
            clocks: [],
            start:moment().format('YYYY-MM-DD hh:mm:ss')
            
            
        }
    },
    mounted(){
      this.refreshData()
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
      },
        refreshData(){
          axios
          .get(`http://localhost:4000/api/users/${this.$route.params.id}`,
            {  headers: { Authorization: 'Bearer ' + this.$session.get("token") }}
            )
          .then((reponse) => {
              this.user = reponse.data.data;
              //alert("entre")
          })
            
        },
        refrechDate(){
            this.date= moment().format('YYYY-MM-DD hh:mm:ss') 
            
        },
        check(status){
            this.refrechDate(),
            this.status= !status
            //alert("in check")
            // Check in
            if(this.status == true){
                axios.post('http://localhost:4000/api/clocks'
                ,
                {"clock":
                    {"time":this.date,
                    "status":this.status,
                    "user_id":this.user.id
                    }
                },
                {  headers: { Authorization: 'Bearer ' + this.$session.get("token") }})
                .catch(error => {
                    this.errorMessage = error.message;
                    console.error("There was an error!", error)
                    
                })
                .then((reponse) => {
                    //alert("in then")
                    //this.refreshData()
                    //alert("Ajout réussi")
                })
            }
            // check out
            // recupere la dernier insersition dans clocks qui corespond à notre utilisateur, son statut doit etre true et la plus grande date de toute

            else{

                //je recupere toutes le lignes de ma tables clocks
                axios
                .get(`http://localhost:4000/api/clocks/`,
                {  headers: { Authorization: 'Bearer ' + this.$session.get("token") }})
                .then((reponse) => {
                    //this.end = reponse.data.data.end,
                    //this.start= reponse.data.data.start,
                    this.clocks = reponse.data.data
                    //alert("get reussi")
                 })
                 .catch(error =>{
                    console.log(error)
                 })
                //je parcours tout les lignes
                for ( var clock in this.clocks){

                    // je verifie s'il corresponde à mon utilisteur , si oui je les retiens
                    if(clock.user_id == this.user.id){

                        // je vrifie aussi s'il ont true comme statut 
                        if(clock.status==true){

                            //je les enregistre dans ma variable start. 
                            //la derniere valeur que va prendre ma variable est la bonne
                            this.start = clock.time

                        }
                    }
                }
                //alert(this.start),

                //enregistre dans clocks

                axios.post('http://localhost:4000/api/clocks'
                ,
                {"clock":
                    {"time":this.date,
                    "status":this.status,
                    "user_id":this.user.id
                    }
                },
                {  headers: { Authorization: 'Bearer ' + this.$session.get("token") }})
                .catch(error => {
                    this.errorMessage = error.message;
                    console.error("There was an error!", error)
                    
                })
                .then((reponse) => {
                    //this.refreshData()
                    //alert("Ajout réussi")
                }),
                //enregistre dans workingtimes
//alert("fin clocks debut working times")
                axios.post(`http://localhost:4000/api/workingtimes/`
                ,
                {"workingtime":
                    {"end":this.date,
                    "start":this.start,
                    "user_id":this.user.id
                    }
                },
                {  headers: { Authorization: 'Bearer ' + this.$session.get("token") }})
                .catch(error => {
                    this.errorMessage = error.message;
                    console.error("There was an error!", error)
                    
                })
                .then((reponse) => {
                    //alert(this.date+" then working times "+this.start+" "+this.user.id+"  response:"+reponse)
                    //this.refreshData()
                    //alert("Ajout réussi")
                })
            }
            

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
