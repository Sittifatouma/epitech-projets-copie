<template>
<div>

  <div v-if="this.$session.exists() && (this.$session.get('role')=='manager' || this.$session.get('role')=='directeur')">
    
    <div class="= row mt-3">
      <div class="col-lg-6">
      <button class="btn btn-primary" @click="goClockManager()">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-stopwatch-fill" viewBox="0 0 16 16">
          <path d="M6.5 0a.5.5 0 0 0 0 1H7v1.07A7.001 7.001 0 0 0 8 16a7 7 0 0 0 5.29-11.584.531.531 0 0 0 .013-.012l.354-.354.353.354a.5.5 0 1 0 .707-.707l-1.414-1.415a.5.5 0 1 0-.707.707l.354.354-.354.354a.717.717 0 0 0-.012.012A6.973 6.973 0 0 0 9 2.071V1h.5a.5.5 0 0 0 0-1h-3zm2 5.6V9a.5.5 0 0 1-.5.5H4.5a.5.5 0 0 1 0-1h3V5.6a.5.5 0 1 1 1 0z"/>
        </svg>
        Pointing
        </button>
      </div>
      
      <div class="=mt-3">
        <div class="col-lg-6">
          <br>
        </div>
      </div>
    </div>
      <!-- manager list -->
      
        <div v-if="this.$session.get('role')=='manager'" class="table-responsive table-striped table-bordered table-hover" id="table">
          <table class="table">
              <thead>
                <tr>
                  <th scope="col">#</th>
                      <th scope="col">Name</th>
                      <th scope="col">mail</th>
                      <th scope="col">Role</th>
                      <th scope="col">options</th>
                      <!--th scope="col">testoptions</th-->
                </tr>
              </thead>
              <tbody>
                  <tr :key="index" v-for="(user,index) in users">
                      <td > {{ index +1}}</td>
                      <td > {{ user.username }}</td>
                      <td > {{ user.email.toLowerCase() }}</td>
                      <td v-if="user.role=='employee'"> Employee</td>
                      <td v-if="user.role=='manager'">Manager</td>
                      <td v-if="user.role=='directeur'"> General Manager</td>
                      
                      <td> 
                        <button type="button" class="btn btn-light mr-1" 
                        data-bs-toggle="modal"
                        data-bs-target="#exempleModal"
                            @click="f_view(user.id,user.username,user.email)">
                          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-stopwatch" viewBox="0 0 16 16">
                            <path d="M8.5 5.6a.5.5 0 1 0-1 0v2.9h-3a.5.5 0 0 0 0 1H8a.5.5 0 0 0 .5-.5V5.6z"/>
                            <path d="M6.5 1A.5.5 0 0 1 7 .5h2a.5.5 0 0 1 0 1v.57c1.36.196 2.594.78 3.584 1.64a.715.715 0 0 1 .012-.013l.354-.354-.354-.353a.5.5 0 0 1 .707-.708l1.414 1.415a.5.5 0 1 1-.707.707l-.353-.354-.354.354a.512.512 0 0 1-.013.012A7 7 0 1 1 7 2.071V1.5a.5.5 0 0 1-.5-.5zM8 3a6 6 0 1 0 .001 12A6 6 0 0 0 8 3z"/>
                          </svg>
                        </button>
                      </td>
                    </tr>
              </tbody>
          </table>
        
      </div>

      <!-- General Manager list -->
      <div v-if="this.$session.get('role')=='directeur'" class="table-responsive table-striped table-bordered table-hover" id="table">
          <table class="table">
              <thead>
                <tr>
                  <th scope="col">#</th>
                      <th scope="col">Name</th>
                      <th scope="col">mail</th>
                      <th scope="col">Role</th>
                      <th scope="col">options</th>
                      <!--th scope="col">testoptions</th-->
                </tr>
              </thead>
              <tbody>
                  <tr :key="index" v-for="(user,index) in users">
                      <td > {{ index +1}}</td>
                      <td > {{ user.username }}</td>
                      <td > {{ user.email.toLowerCase() }}</td>
                      <td v-if="user.role=='employee'"> Employee</td>
                      <td v-if="user.role=='manager'">Manager</td>
                      <td v-if="user.role=='directeur'"> General Manager</td>
                      
                      <!--td>
                        <a v-link="{ name: 'Viewuser', params: { name: index }}">View</a>
                        <router-link to="Viewuser/index">Update</router-link>
                        <router-link to="Viewuser/index">Delete</router-link>
                      </td-->
                      <td> 
                        <button type="button" class="btn btn-light mr-1" 
                        data-bs-toggle="modal"
                        data-bs-target="#exempleModal"
                            @click="f_view(user.id,user.username,user.email)">
                          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-stopwatch" viewBox="0 0 16 16">
                            <path d="M8.5 5.6a.5.5 0 1 0-1 0v2.9h-3a.5.5 0 0 0 0 1H8a.5.5 0 0 0 .5-.5V5.6z"/>
                            <path d="M6.5 1A.5.5 0 0 1 7 .5h2a.5.5 0 0 1 0 1v.57c1.36.196 2.594.78 3.584 1.64a.715.715 0 0 1 .012-.013l.354-.354-.354-.353a.5.5 0 0 1 .707-.708l1.414 1.415a.5.5 0 1 1-.707.707l-.353-.354-.354.354a.512.512 0 0 1-.013.012A7 7 0 1 1 7 2.071V1.5a.5.5 0 0 1-.5-.5zM8 3a6 6 0 1 0 .001 12A6 6 0 0 0 8 3z"/>
                          </svg>
                        </button>
                        <button type="button" class="btn btn-light mr-1" data-bs-toggle="modal"
                      data-bs-target="#exempleModal" 
                      @click="f_edit(user.id,user.username,user.email)">
                          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">
                            <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
                            <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>
                          </svg>
                        </button>


                        <button  type="button" class="btn btn-light mr-1" data-bs-toggle="modal"
                          data-bs-target="#exempleModal"
                          @click="f_delete(user.id,user.username)">
                          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16">
                            <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"/>
                            <path fill-rule="evenodd" d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"/>
                          </svg>
                        </button>
                      </td>
                    </tr>
              </tbody>
          </table>
      </div>

             <!-- Add user Model -->
      <div class="" id="overlay" v-if="showAddModal">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title">Add new user</h5>
              <button type="button" class="close" @click="showAddModal=false">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body p-4">
              <form action="#" @submit="checkForm">
                <p v-if="errors.length">
                  <b>Please correct the following error(s):</b>
                  <ul>
                    <li v-for="error in errors" :key="error">{{ error }}</li>
                  </ul>
                </p>
                  <div class="form-group">
                    <label>Username</label>
                    <input type="text" class="form-control form-control-lg" placeholder="Username" v-model="name_u" required>
                  </div><br>
                  <div class="form-group">
                    <label>Email</label>
                    <input type="email" class="form-control" aria-describedby="emailHelp" placeholder="E-mail" v-model="email_u" required>
                  </div><br>
                  <div class="form-group">
                    <button class="btn btn-info btn-block btn-lg"
                    @click="validation_form(name_u,email_u)">
                        Add user
                    </button>
                  </div>
              </form>
              
            </div>
          </div>
        </div>
      </div>
      
                 <!-- View user Model -->
      <div class="" id="overlay" v-if="showViewModal">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title">User's information </h5>
              <button type="button" class="close" @click="showViewModal=false">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body p-4">
              <div class="form-group">
                <h4>Name :<b> {{sauveName}}</b></h4>
              </div>
              <div class="form-group">
                <h4>E-mail: <i>{{sauveMail}}</i></h4><br>
              </div>
              <div class="form-group">
                <button class="btn btn-info btn-block btn-lg"
                @click="showViewModal=false">
                    Close
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>

                 <!-- Edit user Model General manager-->
      <div  class="" id="overlay" v-if="this.$session.get('role')=='directeur' && showEditModal">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title">Edit user</h5>
              <button type="button" class="close" @click="showEditModal=false">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body p-4">
              <form action="#">
                  <!--div class="form-group">
                    <label>Username</label>
                    <input type="text" class="form-control" placeholder="Username"  v-model="nom" required >
                  </div><br>

                  <div class="form-group" >
                    <label>Email</label>
                    <input type="Email" class="form-control" placeholder="Email" aria-describedby="emailHelp"   v-model="e_mail" required>
                  </div--><br>
                  <div class="form-group" >
                    <label>Select Role</label>
                    <select id="inputState" class="form-control" required v-model="selected">
                      <option disabled selected>--- Select Role ---</option>
                      <option value="employee">Employee</option>
                      <option value="manager">Manager</option>
                      <!--option value="directeur">General Manager</option-->
                    </select>
                  </div><br>
                  
                  <div class="form-group">
                    <button class="btn btn-info btn-block btn-lg"
                    @click="edit_user_g_manager(sauveId,selected)">
                        Update user
                    </button>
                  </div>
              </form>
            </div>
          </div>
        </div>
      </div>
                 <!-- Edit user Model manager-->
      <div  class="" id="overlay" v-if="this.$session.get('role')=='manager' && showEditModal">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title">Edit user</h5>
              <button type="button" class="close" @click="showEditModal=false">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body p-4">
              <form action="#">
                  <div class="form-group">
                    <label>Username</label>
                    <input type="text" class="form-control"  v-model="nom" required >
                  </div><br>
                  <div class="form-group" >
                    <label>Email</label>
                    <input type="Email" class="form-control" aria-describedby="emailHelp"   v-model="e_mail" required>
                  </div><br>
                  <div class="form-group">
                    <button class="btn btn-info btn-block btn-lg"
                        @click="edit_user(sauveId,nom,e_mail)">
                        Update user
                    </button>
                  </div>
              </form>
            </div>
          </div>
        </div>
      </div>

                   <!-- delete user Model -->
      <div class="" id="overlay" v-if="showDeleteModal">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title">Delete user</h5>
              <button type="button" class="close" @click="showDeleteModal=false">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body p-4">
              <h4 class="text-danger">Are you sure want to delete this user?</h4>
              <h5 >You are deleting {{sauveName}}</h5>
              <hr>
              <button class="btn btn-danger btn-lg" @click="delete_user(sauveId)">Yes </button>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
              <button class="btn btn-success btn-lg" @click="showDeleteModal=false">No</button>
            </div>
          </div>
        </div>
      </div>
      
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
  name: 'Postuser',
  data () {
    return {
      msg: 'Welcome to your user interface',
      users: [],
      errors: [],
      showAddModal:false,
      showEditModal:false,
      showDeleteModal:false,
      showViewModal:false,
      deleteUser:false,
      sauveId:String,
      sauveName:String,
      sauveMail:String,
      name_user:null,
      email_user:null,
      //role:this.$session.get('role'),
      selected:""
      //e_mail:null,
      //nom:null
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
      .get('http://localhost:4000/api/users',
      {  headers: { Authorization: 'Bearer ' + this.$session.get("token") }}
      )  
      .then((reponse) => {
          this.users = reponse.data.data;
         
          //alert(this.$session.get("token"))
      })
      .catch(error =>{
        console.log(error)
      }),
      this.showAddModal=false,
      this.showEditModal=false,
      this.showDeleteModal=false,
      this.showViewModal=false,
      this.deleteUser=false,
      this.sauveId="",
      this.sauveName="",
      this.sauveMail=""
    },
   goClockManager(){
      this.$router.push({ name: 'ClockManager', params: { id:this.$session.get("id")} })

   },

    view_user:function(id){
     
      this.$router.push('Postuser')
    },
    f_delete:function(id,name){
      this.showDeleteModal=true,
      this.sauveId=id,
      this.sauveName=name
    },
    f_view:function(id,name,mail){
      //this.showViewModal=true,
      this.sauveName=name,
      this.sauveMail=mail
      this.sauveId=id
      //alert(this.sauveMail)
      this.$router.push({ name: 'WorkingTimes', params: { id:this.sauveId,name:this.sauveName,mail:this.sauveMail } })
    },
    f_edit:function(id,name,mail){
      this.showEditModal=true,
      this.sauveId=id,
      this.sauveName=name,
      this.sauveMail=mail
      
    },
    f_add:function(name,mail){
      this.showAddModal=true,
      this.sauveName=name,
      this.sauveMail=mail
      
    },
    delete_user:function(id){
      axios.delete('http://localhost:4000/api/users/'+id,
      {  headers: { Authorization: 'Bearer ' + this.$session.get("token") }}
      )
        .then((reponse) => {
           this.refreshData()
           //alert("Supression réussi");
         }),
      this.showDeleteModal=false
    },
    validation_form:function(nom,mail){
      //alert(nom+" "+mail),
      axios.post('http://localhost:4000/api/users',
      {"role":
          {"username":nom,
          "email":mail,
          "role": "employee"
          }
      },
      {  headers: { Authorization: 'Bearer ' + this.$session.get("token") }}
      )
      .catch(error => {
        this.errorMessage = error.message;
        console.error("There was an error!", error)
        
      })
      .then((reponse) => {
        this.refreshData()
        //alert("Ajout réussi")
      }),
      this.showAddModal=false
      
    },
    edit_user:function(id,name,email){
     // alert(id+" "+name+" "+email)
      axios.put('http://localhost:4000/api/users/'+id, 
        {"role":
            { "username":name,
              "email":email,
            }
        }
        ,
      {  headers: { Authorization: 'Bearer ' + this.$session.get("token") }}
      )
      .catch(error => {
          this.errorMessage = error.message;
          console.error("There was an error!", error)
        
      })
      .then((reponse) => {
        this.refreshData()
        //alert("Edition réussi")
      }),
      this.showEditModal=false
    },
    
    edit_user_g_manager :function(id,selected){
     // alert(id+" "+name+" "+email)
      axios.put('http://localhost:4000/api/users/'+id, 
        {"role":
            { 
              "role":selected
            }
        }
        ,
      {  headers: { Authorization: 'Bearer ' + this.$session.get("token") }}
      )
      .catch(error => {
          this.errorMessage = error.message;
          console.error("There was an error!", error)
        
      })
      .then((reponse) => {
        this.refreshData()
        //alert("Edition réussi")
      }),
      this.showEditModal=false
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  #overlay{
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background: rgba(0,0,0,0,6);
    
}
#table{
  margin-left: 20px;
  padding-right: 20px;
}

</style>
