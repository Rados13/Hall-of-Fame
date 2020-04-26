<template>
  <div id="app">
    <h1>CreateCourse</h1>
    <form action='#' @submit.prevent = 'addGroup'>
    <p><input type='text' placeholder="Course" v-model='course'></p>
    <p><input type='text' placeholder="Day of week" v-model='dayOfWeek'></p>
    <p><input type='text' placeholder="Time" v-model='time'></p>
    <p><input type='text' placeholder="Lecturer" v-model='lecture'></p>
    <p><input type='submit' value='Submit' ></p>
    </form>
  </div>
</template>

<script>


import axios from 'axios';
const url = 'http://127.0.0.1:8000/api/groups/';

export default {
  name: 'CreateGroup',
  components:{
  },
  data(){
    return {
      course: '',
      dayOfWeek: '',
      time: '',
      lecture: '',
    }
  },
  methods: {
    addGroup(){
        axios.post(url,{course: this.course, date_time: [{day_of_week: this.dayOfWeek,time: this.time}],
        lectures_list: [{lecture_id: this.lecture,main_lecture: true}],enrolled_list: []}).then(() =>{
            console.log("Work")
        }).catch(error => {
            console.log(error);
        });
    }
  }
}
</script>