<template>
  <div>
    <div class="hello" v-if="this.$session.exists()">
      <h1>Chart</h1>
      <!--<column-chart :data="[['Sun', this.resulat], ['Mon', 15], ['Tue', 20]]"></column-chart>-->
      <h3>Start hour</h3>
      <p>{{ this.date_start }}</p>
      <h3>End hour</h3>
      <p>{{ this.date_end }}</p>
      <h3>Elapsed hour</h3>
      <p>{{ this.date_elapsed }}</p><br>
      <h3>Convert elapsed to hours and minutes</h3>
      <p>Hours = {{this.y}} and minutes = {{this.i}}</p>
      <h3>Resultat after concate hours and minutes</h3>
      <p>Hours = {{this.resultat}}</p>
      <table class="table">
                <thead>
                    <tr>
                    <!--th scope="col">#id</th-->
                          <th scope="col">Start</th>
                          <th scope="col">End</th>
                        <th scope="col">Extra Hourss</th>
                    </tr>
                </thead>
                <tbody>
                    <tr :key="index" v-for="(workingtime,index) in this.workingtimes">
                              <!--td  v-if="workingtime.user_id == $route.params.id"> {{index +1}}</td-->
                              <td > {{moment(workingtime.start).format("YYYY-MM-DD HH:mm:ss")  }}</td>
                              <td > {{ moment(workingtime.end).format("YYYY-MM-DD HH:mm:ss")}}</td>
                              <td> {{ moment(workingtimes.end).format('HH')}}</td>
                      </tr>
                </tbody>
            </table>
      <button @click="date_calcul()"> Afficher</button>
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
import ChartMaker from 'vue-chartmaker'

export default {
  name: 'Chart',
  component: {
    ChartMaker
  },
  props:{
    date:Array,
  },
  data() {
    return {
      //week:[Mon,Tue,Wed,Thu,Fri,Sat,Sun],
      workingtimes:[],
      
      x:"",
      y: "",
      i: "",
      resultat: 0,
      tempTime:"",
      
      //Variable date_calcul
      date_start: "",
      date_end: "",
      date_elapsed: "",
    }
  }, 

  mounted(){
    this.fetch_data()
    //this.date_calcul()
  },
  methods:{
    mamethode(elapsed){

      this.x = elapsed,

      this.tempTime = moment.duration(this.x, 'ms'),

      this.y = this.tempTime.hours(),
      this.i = this.tempTime.minutes(),
      this.resultat = parseInt(this.y) + parseFloat((this.i / 60).toFixed(2))
    },

    date_calcul() {

      //for(var workingtime in this.workingtimes) {
      alert("Work = " + this.workingtimes[0].start)
      this.date_start = new Date(
                            moment(this.workingtimes[0].start).format("YYYY"),
                            moment(this.workingtimes[0].start).format("MM") - 1,
                            moment(this.workingtimes[0].start).format("DD"),
                            moment(this.workingtimes[0].start).format("HH"),
                            moment(this.workingtimes[0].start).format("mm"),
                            moment(this.workingtimes[0].start).format("ss"),),
      this.date_end = new Date(
                            moment(this.workingtimes[0].end).format("YYYY"),
                            moment(this.workingtimes[0].end).format("MM") - 1,
                            moment(this.workingtimes[0].end).format("DD"),
                            moment(this.workingtimes[0].end).format("HH"),
                            moment(this.workingtimes[0].end).format("mm"),
                            moment(this.workingtimes[0].end).format("ss"),), 
      this.date_elapsed = this.date_end - this.date_start,
      this.mamethode(this.date_elapsed)
      //}
      
    },

    fetch_data(){
      
      axios
        .get(`http://localhost:4000/api/workingtimes/`,
        {  headers: { Authorization: 'Bearer ' + this.$session.get("token") }})
        .then((reponse) => {
            this.workingtimes = reponse.data.data
            
         })
         .catch(error =>{
            console.log(error)
          })
    }
  }
}
</script>

<style scoped>

</style>