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
import Entry from '../../services/Entry.js';

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
    new Entry().getUsers().then(data=> this.students = data);
  },
  
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
