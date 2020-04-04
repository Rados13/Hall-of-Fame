<template>
  <div id="app">
    <Login v-if="token===null"/>
    <StudentList v-if="token!==null" v-bind:students='students' v-on:del-student="deleteStudent" @token-event = 'setToken'/>
    
  </div>
</template>

<script>

import axios from 'axios';
import StudentList from './components/StudentList';
import Login from './components/Login';

const baseURL = 'http://127.0.0.1:8000/api/students/';
// const addURL = 'http://127.0.0.1:8000/api/students/';

export default {
  name: 'App',
  components:{
    StudentList,
    Login
  },
  data(){
    return {
      token: null,
      students: [],
      studentName: ''
    }
  },
  async created(){
    try{
      const res = await axios.get(baseURL);

      this.students = res.data;
    }catch(e){
      console.error(e);
    }
  },
  methods: {
    async addStudent(){
      const res = await axios.post(baseURL,{Name: this.studentName});
      this.students = [...this.students,res.data];
      this.studentName = null;
    },
    deleteStudent(id){
      console.log(this.students);
      this.students = this.students.filter(student => student.id !== id);
    },
    setToken(token){
      console.log("Whatever");
      console.log(token);
      this.token = token;
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
