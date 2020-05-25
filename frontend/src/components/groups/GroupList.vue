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


export default {
  name: 'GroupList',
  components:{
    GroupElem
  },
  props: ['lecture','student'],
  computed:{
      groups(){
        return this.$store.state.groups;
    }
  },
  created(){
    var param = "all";
    if(this.student)param="student";
    if(this.lecture)param="lecture";
    this.$store.commit('getGroups',param);
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
