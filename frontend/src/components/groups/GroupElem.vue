<template>
    <!-- <div v-bind:class="{'styleclass':value}"> If value is True set styleclass on this div -->
    <div class="list-item"> 
        <p> Course name: {{group.course}}</p>
            <!-- <input type="checkbox" v-on:change="markComplete"> -->
        <div v-bind:key="dateTime.day_of_week" v-for="dateTime in group.date_time">    
            <p> Day: {{dateTime.day_of_week}} hour of start: {{dateTime.time}}</p>
        </div>    
        <div v-bind:key="lecture.lecture_id" v-for="lecture in lectures">    
            <p> Lecture: {{lecture.first_name}}  {{lecture.last_name}}</p>
        </div>    
        <div class="buttons">
        <button @click="signFor(group.pk)" class='button'>Sign for course</button>
        <button @click="goToGroupPanel(group.pk)" class='button'>Go to group panel</button>    
        </div>
    </div>
</template>

<script>

import GroupRUD from '../../services/GroupRUD.js';

export default {
    name: "GroupElem",
    props: ['group'],
    data(){
    return {
        lectures: []
      }
    },
    created(){
        GroupRUD.getGroupLecturesNames(this.group.lectures_list).then(data=> this.lectures=data).catch(e=>console.log(e));     
    },
    methods:{ 
      goToGroupPanel(id){
          this.$router.push('/groups/'+id);
      },
      signFor(id){
        GroupRUD.signFor(id);
      }
    }
}
</script>

<style scoped>
@import './stylesheet.css';    
</style>