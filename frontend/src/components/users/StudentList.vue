<template>
  <div class="hello">
    <h1>Hello world</h1>
  <div v-bind:key="student.id" v-for="student in students">
    <StudentElem v-bind:student = "student" v-on:del-student="deleteUser(student.id)"/>
  </div>
  </div>
</template>

<script>

import StudentElem from './StudentElem.vue';
import axios from 'axios';
const baseURL = 'http://127.0.0.1:8000/api/users/';

export default {
  name: 'StudentList',
  components:{
    StudentElem
  },
  data(){
    return {
      students: []
    }
  },
  // props: ['students'],
  created(){
    console.log("Happen");
    this.getUsers();
  },
  methods:{
  async getUsers(){
    console.log("Start");
        try{
        await axios.get(baseURL,{
          headers: {Authorization: `Bearer ${localStorage.getItem("accessToken")}`}
        }).then(response =>{
          this.students = response.data;
        });
      }catch(e){
        console.error(e);
      }  
    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
