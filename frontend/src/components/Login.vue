<template>
  <div id="app">
    <h1>Login</h1>
    <form action='#' @submit.prevent = 'login'>
    <p><input type='text' placeholder="login" v-model='name'></p>
    <p><input type='text' placeholder="password" v-model='password'></p>
    <p><input type='submit' value='Submit' ></p>
    </form>
  </div>
</template>

<script>

import axios from 'axios';

const baseURL = 'http://127.0.0.1:8000/api/auth/login';

export default {
  name: 'Login',
  components:{
  },
  data(){
    return {
      name: '',
      password: '',
      token: ''
    }
  },
  methods: {
    login(){
        axios.post(baseURL,{username: this.name,password: this.password}).then(response =>{
            console.log(response);
            this.$emit('token-event',response.data.token);
            console.log(response.data.token);
        }).catch(error => {
            console.log(error);
        });

        
    }
  }
}
</script>