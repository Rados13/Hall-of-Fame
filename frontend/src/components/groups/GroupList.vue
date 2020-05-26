<template>
  <div class="hello">
    <h1>Hello world</h1>
  <div v-bind:key="group.pk" v-for="group in groups">
    <GroupElem v-bind:group = "group" v-bind:isLecture="isLecture" v-bind:isStudent="isStudent"/>
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
  props: ['type'],
  computed:{
      groups(){
        return this.$store.state.groups;
    }
  },
  data(){
    return {
      isLecture: false,
      isStudent: false,
    }
  },
  watch:{
    '$route'(){
      this.getGroups();
    }
  },
  created(){
    this.getGroups();
  },
  methods:{
    getGroups(){
      this.isLecture = this.type==='lecture';
      this.isStudent = this.type==='student';
      this.$store.commit('getGroups',this.type);
    }
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
