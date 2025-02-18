<template>
    <div>
        <div v-if="this.$session.exists() && (this.$session.get('role')=='manager' || this.$session.get('role')=='directeur')">
            <!--div class="container blocktext alert alert-danger">
                <h1>{{this.$session.get('token')}}</h1>
            </div--><br>
            <form>
                <div class="form-group row">
                    <label for="inputEmail3" class="col-sm-2 col-form-label">Start</label>
                    <div class="col-sm-5">
                        <input type="date" class="form-control" id="inputEmail3" placeholder="Start" v-model="date_start" required>
                    </div>
                    <div class="col-sm-5">
                        <input type="time" class="form-control" id="inputEmail3" placeholder="Start" v-model="time_start" required>
                    </div>
                </div><br>
                <div class="form-group row">
                    <label for="inputPassword3" class="col-sm-2 col-form-label">End</label>
                    <div class="col-sm-5">
                        <input type="date" class="form-control" id="inputPassword3" placeholder="End" v-model="date_end" required>
                    </div>
                    <div class="col-sm-5">
                        <input type="time" class="form-control" id="inputPassword3" placeholder="End" v-model="time_end" required>
                    </div>
                </div><br>            
                <div class="form-group row">
                    <div class="col-sm-12">
                        <button class="btn btn-primary" @click="addpoint($route.params.id,date_start,time_start,date_end,time_end)">Sign in</button>
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
        name: 'PointForHim',
        data () {
            return {
            msg: 'Date de début ne doit pas etre supérieur à la date de fin.',
            end: " ",
            start: " ", 
            d_start:" ",
            d_end:" ",
            t_start:" ",
            t_end:" "
            //view: false   
            }
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
            addpoint(id,d_start,t_start,d_end,t_end){
                if(d_start>d_end){
                    //view==true
                    alert( "Date de début ne doit pas etre supérieur à la date de fin.")
                    
                }
                else{
                    if(d_start == d_end && t_start>t_end){
                        alert( "Date de début ne doit pas etre supérieur à la date de fin.( verifiez les heures saisies)")
                    }else{
                        if(d_end > moment().format("YYYY-MM-DD")){
                            alert("Les dates saisies ne doivent pas etre superieur à la date du jour")
                        }
                        else{
                            this.start = moment( d_start+" "+t_start).format('YYYY-MM-DD HH:mm:ss'),
                            this.end = moment( d_end+" "+t_end).format('YYYY-MM-DD HH:mm:ss'),
                            //alert(id+" "+this.end+" "+this.start),  
                            axios.post(`http://localhost:4000/api/workingtimes/`,
                            {"workingtime":
                                {"end":this.end,
                                "start":this.start,
                                "user_id":id
                                }
                            },
                            {  headers: { Authorization: 'Bearer ' + this.$session.get("token") }})
                            .catch(error => {
                                this.errorMessage = error.message;
                                console.error("There was an error!", error)
                                
                            })
                            .then((reponse) => {
                               // alert(this.$route.params.name+" "+this.$route.params.mail),
                                this.$router.push({ name: 'WorkingTimes', params: { id:this.$route.params.id,name:this.$route.params.name,mail:this.$route.params.mail } })

                            })
                        }
                        
                    }
                    
                        
                }
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
        }
    }


</script>
<style scoped>
#form{
  margin-left: 20px;
  padding-right: 20px;
}

</style>
