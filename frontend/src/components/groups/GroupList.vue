<template>
  <div class="hello">
    <h1>Hello world</h1>
  <div v-bind:key="group.pk" v-for="group in groups">
    <GroupElem v-bind:group = "group" v-on:del-group="deleteGroup" v-on:sign-group="signFor"/>
  </div>
  </div>
</template>

<script>

import GroupElem from './GroupElem.vue';
import axios from 'axios';
import Entry from "../../services/Entry";

const baseURL = 'http://127.0.0.1:8000/api/groups/';
export default {
  name: 'GroupList',
  components:{
    GroupElem
  },
  data(){
    return {
      groups: []
    }
  },
  // props: ['students'],
  created(){
    this.getGroups();
  },
  methods:{
  async getGroups(){
    console.log("Start");
      //   try{
      //   await axios.get(baseURL,{
      //     headers: {Authorization: `Bearer ${localStorage.getItem("accessToken")}`}
      //   }).then(response =>{
      //     this.groups = response.data;
      //     console.log(response.data);
      //   });
      // }catch(e){
      //   console.error(e);
      // }
        Entry.sendGet(baseURL).then(response =>{this.groups = response.data}, e => console.error(e))
    },
    delteGroup(id){
        console.log("Delete"+ id+"\n");
    },
    async signFor(id){
      console.log(id);
      try{
        await axios.post(baseURL+id+"/student/",{
          headers: {Authorization: `Bearer ${localStorage.getItem("accessToken")}`},
        }).then(response => {
          console.log(response.data);
        });
      }catch(e){
        console.error(e);
      }
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
