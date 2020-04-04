<template>
  <div class="hello">
    <h1>Hello world</h1>
  <div v-bind:key="student.id" v-for="student in students">
    <!-- <h3>{{student.name}}   {{student.surname}}</h3> -->
    <StudentElem v-bind:student = "student" v-on:del-student="$emit('del-student',student.id)"/>
  </div>
  </div>
</template>

<script>

import StudentElem from './StudentElem.vue';

export default {
  name: 'StudentList',
  components:{
    StudentElem
  },
  props: ['students']
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
