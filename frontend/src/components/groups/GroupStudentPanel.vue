<template>
    <div class="list-item">
        <p> Course name: {{group.course}} 
        <div v-bind:key="dateTime.day_of_week" v-for="dateTime in group.date_time">    
            <p> Day: {{dateTime.day_of_week}}  time:  {{dateTime.time}} </p> 
        </div>  

        <div v-bind:key="elem.lecture.pk" v-for="elem in group.lectures_list">    
           <p> Lecture: {{elem.lecture.first_name}} {{elem.lecture.last_name}} </p>
        </div>    

        <div v-bind:key="student.enrolled_id" v-for="student in group.enrolled_list">
            <p>Marks: </p>
            <div v-bind:key="mark.for_what" v-for="mark in student.marks_list">
                <p>Value: {{mark.value}}   for what {{mark.for_what}}   additional note {{mark.note}}</p>
            </div>
            <p>Average: {{avg}}</p>
            <p>Inattendances: </p>
            <div v-bind:key="inattendance.class_num" v-for="inattendance in student.inattendances_list">
                <p>Class:  {{inattendance.class_num}}   
                    <input type="checkbox" name="Justified" value='inattendance.justified' readonly></p>
            </div>
        </div>
        <button class="button" @click="createMail">{{mailButtonText}}</button>
        <div v-if="sendMail">
            <MailForm v-bind:users_list="group.lectures_list" 
            v-bind:type= "'student'"
            @sended='createMail'></MailForm>
        </div>

    </div>
</template>

<script>

import GroupRUD from '../../services/GroupRUD.js';
import MailForm from './MailForm';
export default {
    name: "GroupStudentPanel",
    components:{
        MailForm
    },
    data(){
    return {
      group: Object,
      avg: 0.0,
      sendMail: false,
      mailButtonText: "Create mail to lecture",
    }
  },
    created(){
        GroupRUD.getGroup(this.$route.params.groupID,false).then(data => {
            this.group = data;
            var sum = 0;
            if(this.group.enrolled_list.length===0)return;
            var student = this.group.enrolled_list[0];
            for(var elem of student.marks_list){
                sum+=elem.value;
            }
            this.avg = student.marks_list.length>0?sum/student.marks_list.length:0.0;
        });
    },
    methods:{
        createMail(){
            this.mailButtonText = this.sendMail?"Create mail to lecture" :"Discard mail"; 
            this.sendMail = !this.sendMail;
        }
    }
}
</script>


<style scoped>
@import './stylesheet.css';    
</style>