<template>
<div>
  <form id="App" 
    @submit="checkForm"
    method="post">

    <p v-if="errors.length">
      <b>Please correct the following error(s):</b>
      <ul>
        <li v-for="error in errors" :key="error">{{ error }}</li>
      </ul>
    </p>

    <p>
      <label for="surname">Surname:</label>
      <input name="surname" type="text" v-model="surname">
    </p>

    <p>
      <label for="firstname">Firstname:</label>
      <input name="firstname" type="text" v-model="firstname">
    </p>

    <p>
      <label for="email">Mail:</label>
      <input name="email" type="email" v-model="email">
    </p>

    <p>
      <input type="submit" value="Submit">
    </p>
  </form>
  </div>
</template>
<script>
export default {
  name: 'Postuser',
  components:{} ,
  data() {
    return {
      errors: [],
      surname: null,
      firstname: null,
      email: null
    }
  },
  methods: {
    checkForm: function(e) {

      // Clear errors
      this.errors = [];

      // Check if the surname is not empty and length <= 50
      if (!this.surname || this.surname.length > 50)
      {
        this.errors.push("The surname can not be empty and must have a length <= 50 !");
      }

      // Check if the firstname is not empty and length <= 50
      if (!this.firstname || this.firstname.length > 50)
      {
        this.errors.push("The firstname can not be empty and must have a length <= 50 !");
      }

      // Check if the email is not empty and match the email pattern
      var re = /(^$|^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$)/;
      if (!this.email || !re.test(this.email))
      {
        this.errors.push("The email can not be empty and must be a valid email !");
      }

      if (!this.errors.length)
      {
        return true;
      }

      e.preventDefault();
    }
  }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
