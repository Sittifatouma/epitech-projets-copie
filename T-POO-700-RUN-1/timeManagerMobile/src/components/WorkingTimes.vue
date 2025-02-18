<template>
    <div>
        <div class="blocktext" v-if="this.$session.exists()">
            <div class="container alert alert-primary">
                <h1>User's information </h1><br>
                <h3>Name: <b>{{$route.params.name}}</b></h3>
                <h3>Email: <b>{{$route.params.mail}}</b></h3>
                
    
            </div>
            <div  v-if="this.$session.get('role')=='manager'|| this.$session.get('role')=='directeur' ">
                <ul  class="nav justify-content-center">
                    <li class="nav-item">
                    <button class="btn btn-primary" @click="pointforhim($route.params.id,$route.params.name,$route.params.mail)">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-stopwatch-fill" viewBox="0 0 16 16">
                            <path d="M6.5 0a.5.5 0 0 0 0 1H7v1.07A7.001 7.001 0 0 0 8 16a7 7 0 0 0 5.29-11.584.531.531 0 0 0 .013-.012l.354-.354.353.354a.5.5 0 1 0 .707-.707l-1.414-1.415a.5.5 0 1 0-.707.707l.354.354-.354.354a.717.717 0 0 0-.012.012A6.973 6.973 0 0 0 9 2.071V1h.5a.5.5 0 0 0 0-1h-3zm2 5.6V9a.5.5 0 0 1-.5.5H4.5a.5.5 0 0 1 0-1h3V5.6a.5.5 0 1 1 1 0z"/>
                        </svg>
                        Point for him 
                        </button>
                    </li>
                </ul>
            </div><br>
           
            <div class="table-responsive table-striped table-bordered table-hover" id="table">
            <table class="table">
                <thead>
                    <tr>
                    <!--th scope="col">#id</th-->
                          <th scope="col">Start</th>
                          <th scope="col">End</th>
                        <th scope="col">Extra Hours</th>
                    </tr>
                </thead>
                <tbody>
                    <tr :key="index" v-for="(workingtime,index) in workingtimes">
                              <!--td  v-if="workingtime.user_id == $route.params.id"> {{index +1}}</td-->
                              <td  v-if="workingtime.user_id == $route.params.id"> {{moment(workingtime.start).format("YYYY-MM-DD HH:mm:ss")  }}</td>
                              <td  v-if="workingtime.user_id == $route.params.id"> {{ moment(workingtime.end).format("YYYY-MM-DD HH:mm:ss")}}</td>
                              <td  v-if="workingtime.user_id == $route.params.id && moment(workingtimes.end).format('HH') > 17 "> {{ moment(workingtimes.end).format('HH') - nuit }}</td>
                      </tr>
                </tbody>
            </table>
            </div> 
            <!--a href="#" class="btn btn-primary" @click="refreshData()">Update</a>
            <a href="#" class="btn btn-primary">Delate</a-->
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

    export default {
        name: 'WorkingTimes',
        data () {
            return {
            msg: 'Welcome to your user interface',
            end: " ",
            start: " ",    
            workingtimes: [],
            nuit:'17',
            toto: 2,
            addworkingtimes:false
            }
        },
        
        mounted(){
            this.refreshData()
        },
        methods:{
            pointforhim(id,name,mail){
                this.$router.push({ name: 'PointForHim', params: { id:id,name:name,mail:mail} })
            },
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
                console.log(this.$route)
                //alert("hier"),
                axios
                .get(`http://localhost:4000/api/workingtimes/`,
                {  headers: { Authorization: 'Bearer ' + this.$session.get("token") }})
                .then((reponse) => {
                
                    this.end = reponse.data.data.end,
                    this.start= reponse.data.data.start,
                    this.workingtimes = reponse.data.data
                    console.log(reponse.data.data.end)
                 })
                 .catch(error =>{
                    console.log(error)
                 })
                
//alert("aujourdoui")
            }  

        }
    }
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#mydiv{
    margin-left: 50px;
}
#table{
  margin-left: 20px;
  padding-right: 20px;
}
</style>
