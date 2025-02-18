<template>

    
    <div class="blocktext">
        <div class="container alert alert-primary">
            <h1>User's information </h1><br>
            <h3>Name: <b>{{$route.params.name}}</b></h3>
            <h3>Email: <b>{{$route.params.mail}}</b></h3>
 
        </div>
        <div class="table-responsive table-striped table-bordered table-hover" id="table">
          <table class="table">
              <thead>
                <tr>
                  <th scope="col">#</th>
                      <th scope="col">Start</th>
                      <th scope="col">End</th>
                      <th scope="col">Extra Hours</th>
                </tr>
              </thead>
              <tbody>
                  <tr :key="index" v-for="(workingtime,index) in workingtimes">
                       

                          <td  v-if="workingtime.user_id == $route.params.id"> {{workingtime.user_id}}</td>
                          <td  v-if="workingtime.user_id == $route.params.id"> {{ workingtime.start }}</td>
                          <td  v-if="workingtime.user_id == $route.params.id"> {{ workingtime.end }}</td>
                          <td  v-if="workingtime.user_id == $route.params.id && moment(workingtimes.end).format('HH') > 1 "> {{ moment(workingtimes.end).format('HH') - nuit }}</td>

                    
                  </tr>
              </tbody>
          </table>
        
        </div> 
        <!--a href="#" class="btn btn-primary" @click="refreshData()">Update</a>
        <a href="#" class="btn btn-primary">Delate</a-->
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
            }
        },
        
        mounted(){
            this.refreshData()
        },
        methods:{

            refreshData(){
                console.log(this.$route)
                //alert("hier"),
                axios
                .get(`http://localhost:4000/api/workingtimes/`)
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
