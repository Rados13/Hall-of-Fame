<template>
  <div id="app">
    <p>{{text}}</p>
    <h1>Login</h1>
    <form action='#' @submit.prevent = 'register'>
    <p><input type='text' placeholder="email" v-model='email'></p>
    <p><input type='text' placeholder="First name" v-model='first_name'></p>
    <p><input type='text' placeholder="Last name" v-model='last_name'></p>
    <p><input type='text' placeholder="password" v-model='password'></p>
    <p><input type='submit' value='Submit' ></p>
    </form>
  </div>
</template>

<script>

import Entry from '../services/Entry.js';


export default {
  name: 'Register',
  components:{
  },
  data(){
    return {
      email: '',
      password: '',
      first_name:'',
      last_name:'',
      text: '',
    }
  },
  methods: {
    register(){
        new Entry(this.$router).register(this.email,this.first_name,this.last_name,this.password);
    },
  }
}
</script>