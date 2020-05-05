<template>
    <!-- <div v-bind:class="{'styleclass':value}"> If value is True set styleclass on this div -->
    <div class="list-item"> 
        <p> Course name: {{group.course}}</p>
            <!-- <input type="checkbox" v-on:change="markComplete"> -->
        <div v-bind:key="dateTime.day_of_week" v-for="dateTime in group.date_time">    
            <p> Day: {{dateTime.day_of_week}} hour of start: {{dateTime.time}}</p>
        </div>    
        <div v-bind:key="lecture.lecture_id" v-for="lecture in group.lectures_list">    
            <p> Lecture: {{lecture.first_name}}  {{lecture.last_name}}</p>
        </div>    
        <div class="buttons">
        <button v-if="!isStudent && !isLecture" @click="signFor(group.pk)" class='button'>Sign for course</button>
        <button v-if="isStudent" @click="goToStudentPanel(group.pk)" class='button'>Show my grades and inattendace</button>    
        <button v-if="isLecture" @click="goToGroupPanel(group.pk)" class='button'>Go to group panel</button>    
        </div>
    </div>
</template>

<script>

import GroupRUD from '../../services/GroupRUD.js';

export default {
    name: "GroupElem",
    props: ['group','isStudent','isLecture'],
    data(){
    return {
        lectures: [],
      }
    },
    methods:{ 
      goToGroupPanel(id){
          this.$router.push('/lecturegroups/'+id);
      },
      goToStudentPanel(id){
          this.$router.push('/studentgroups/'+id);
      },
      signFor(id){
        GroupRUD.signFor(id);
      },
    
    }
}
</script>

<style scoped>
@import './stylesheet.css';    
</style>