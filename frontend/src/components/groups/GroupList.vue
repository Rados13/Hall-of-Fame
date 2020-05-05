<template>
  <div class="hello">
    <h1>Hello world</h1>
  <div v-bind:key="group.pk" v-for="group in groups">
    <GroupElem v-bind:group = "group" v-bind:isLecture="lecture" v-bind:isStudent="student"/>
  </div>
  </div>
</template>

<script>

import GroupElem from './GroupElem.vue';
import GroupRUD from '../../services/GroupRUD.js';


export default {
  name: 'GroupList',
  components:{
    GroupElem
  },
  props: ['lecture','student'],
  data(){
    return {
      groups: []
    }
  },
  created(){
    if(this.student){ GroupRUD.getStudentGroups().then(data=> this.groups = data);}
    else if(this.lecture){ GroupRUD.getLectureGroups().then(data=> this.groups =data);  }
    else{ GroupRUD.getGroups().then(data => this.groups = data); }
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
