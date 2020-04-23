<template>
  <div id="app">
    <h1>Login</h1>
    <form action='#' @submit.prevent = 'login'>
    <p><input type='text' placeholder="email" v-model='email'></p>
    <p><input type='text' placeholder="password" v-model='password'></p>
    <p><input type='submit' value='Submit' ></p>
    </form>
  </div>
</template>

<script>

import axios from 'axios';

const baseURL = 'http://127.0.0.1:8000/api/token';

export default {
  name: 'Login',
  components:{
  },
  data(){
    return {
      email: '',
      password: '',
      token: ''
    }
  },
  methods: {
    login(){
      localStorage.setItem("email", this.email);
      localStorage.setItem("password", this.password);
        axios.post(baseURL,{email: this.email,password: this.password}).then(response =>{
            console.log(response);
            localStorage.setItem("accessToken", response.data.access);      
            localStorage.setItem("refreshToken", response.datarefresh);
            this.$emit('token-event',true);
        }).catch(error => {
            console.log(error);
            this.$emit('token-event',false);
        });

        
    }
  }
}
</script>