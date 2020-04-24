<template>
  <div id="app">
    <NavbarApp/>
    <router-view></router-view>
    <!-- <Login v-if="this.token==null" @token-event = 'setToken'/> -->
    <!-- <StudentList v-if="this.token!=null" v-bind:students='students' v-on:del-student="deleteStudent" /> -->
    
  </div>
</template>

<script>

import axios from 'axios';
// import StudentList from './components/StudentList';
// import Login from './components/Login';
import NavbarApp from './components/Navbar';

const baseURL = 'http://127.0.0.1:8000/api/users/';

export default {
  name: 'App',
  components:{
    // StudentList,
    // Login,
    NavbarApp,
  },
  data(){
    return {
      token: localStorage.getItem("accesToken"),
      students: [],
      studentName: '',
    }
  },
  methods: {
    async getUsers(){
        try{
        await axios.get(baseURL,{
          headers: {Authorization: `Bearer ${localStorage.getItem("accessToken")}`}
        }).then(response =>{
          console.log(response.data);
          this.students = response.data;
        });
      }catch(e){
        console.error(e);
      }  
    },
    async addStudent(){
      const res = await axios.post(baseURL,{Name: this.studentName});
      this.students = [...this.students,res.data];
      this.studentName = null;
    },
    deleteStudent(id){
      console.log(this.students);
      this.students = this.students.filter(student => student.id !== id);
    },
    setToken(result){
      if(result==true){
        this.getUsers();
        this.token = true;
      }
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
