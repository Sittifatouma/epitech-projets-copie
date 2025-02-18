<template>

  <div class=" ">
    
    <router-link to="/ClockManager/1">Aller à ClockManager</router-link>
    <div class="= row mt-3">
      <div class="col-lg-6">
          <button  class="btn btn-primary" @click="showAddModal=true">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-person-plus" viewBox="0 0 16 16">
          <path d="M6 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm2-3a2 2 0 1 1-4 0 2 2 0 0 1 4 0zm4 8c0 1-1 1-1 1H1s-1 0-1-1 1-4 6-4 6 3 6 4zm-1-.004c-.001-.246-.154-.986-.832-1.664C9.516 10.68 8.289 10 6 10c-2.29 0-3.516.68-4.168 1.332-.678.678-.83 1.418-.832 1.664h10z"/>
          <path fill-rule="evenodd" d="M13.5 5a.5.5 0 0 1 .5.5V7h1.5a.5.5 0 0 1 0 1H14v1.5a.5.5 0 0 1-1 0V8h-1.5a.5.5 0 0 1 0-1H13V5.5a.5.5 0 0 1 .5-.5z"/>
        </svg>
        Add new user
      </button>
      </div>
      
      <div class="=mt-3">
        <div class="col-lg-6">
          <br>
        </div>
      </div>
    </div>
      
      
        <div class="table-responsive table-striped table-bordered table-hover" id="table">
          <table class="table">
              <thead>
                <tr>
                  <th scope="col">#</th>
                      <th scope="col">Name</th>
                      <th scope="col">mail</th>
                      <th scope="col">options</th>
                      <!--th scope="col">testoptions</th-->
                </tr>
              </thead>
              <tbody>
                  <tr :key="index" v-for="(user,index) in users">
                      <td > {{ index +1}}</td>
                      <td > {{ user.username }}</td>
                      <td > {{ user.email.toLowerCase() }}</td>
                      
                      <!--td>
                        <a v-link="{ name: 'Viewuser', params: { name: index }}">View</a>
                        <router-link to="Viewuser/index">Update</router-link>
                        <router-link to="Viewuser/index">Delete</router-link>
                      </td-->
                      <td > 
                        <button type="button" class="btn btn-light mr-1" 
                        data-bs-toggle="modal"
                        data-bs-target="#exempleModal"
                            @click="f_view(user.id,user.username,user.email)">
                          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-eye" viewBox="0 0 16 16">
                            <path d="M16 8s-3-5.5-8-5.5S0 8 0 8s3 5.5 8 5.5S16 8 16 8zM1.173 8a13.133 13.133 0 0 1 1.66-2.043C4.12 4.668 5.88 3.5 8 3.5c2.12 0 3.879 1.168 5.168 2.457A13.133 13.133 0 0 1 14.828 8c-.058.087-.122.183-.195.288-.335.48-.83 1.12-1.465 1.755C11.879 11.332 10.119 12.5 8 12.5c-2.12 0-3.879-1.168-5.168-2.457A13.134 13.134 0 0 1 1.172 8z"/>
                            <path d="M8 5.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5zM4.5 8a3.5 3.5 0 1 1 7 0 3.5 3.5 0 0 1-7 0z"/>
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
                        <button type="button" class="btn btn-light mr-1" data-bs-toggle="modal"
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
                    <input type="text" class="form-control form-control-lg" placeholder="User Name" v-model="name_u" required>
                  </div><br>
                  <div class="form-group">
                    <input type="email" class="form-control" aria-describedby="emailHelp" placeholder="User E-mail" v-model="email_u" required>
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

    

                 <!-- Edit user Model -->
      <div class="" id="overlay" v-if="showEditModal">
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
                    <input type="text" class="form-control"   required v-model="nom">
                  </div><br>
                  <div class="form-group">
                    <input type="Email" class="form-control" aria-describedby="emailHelp"  required v-model="e_mail" >
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
      //e_mail:null,
      //nom:null
    }
  },
  mounted(){
      this.refreshData()
  },
  methods:{
    refreshData(){
      axios
      .get('http://localhost:4000/api/users')
       ,{headers: { 'Authorization': 'Bearer ' + this.$session.get("token")}}  
      .then((reponse) => {
          this.users = reponse.data.data;
          //alert(this.users)
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
      axios.delete('http://localhost:4000/api/users/'+id)
        .then((reponse) => {
           this.refreshData()
           alert("Supression réussi");
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
      },console.log(this.name_user))
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
      alert(id+" "+name+" "+email)
      axios.put('http://localhost:4000/api/users/'+id, 
        {"user":
            { "username":name,
              "email":email,
            }
        },
        console.log(this.name_user)
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
