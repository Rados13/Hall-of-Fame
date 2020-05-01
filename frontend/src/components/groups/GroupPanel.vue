
<template>

    <!-- <div v-bind:class="{'styleclass':value}"> If value is True set styleclass on this div -->
    <div class="list-item"> 
        <div v-if="nameChange">
            <p> Course name: {{group.course}} 
            <button @click="nameChange=!nameChange" class='button'>Modify course name</button></p>
        </div>
        <div v-else>
            <form action='#' @submit.prevent = 'changeCourseName()'>
                <p><input type='text' v-bind=group.course v-model='group.course'><input type='submit' value='Submit' ></p>
            </form>
        </div>

        <div v-bind:key="dateTime.day_of_week" v-for="dateTime in group.date_time">    
            <GroupDateTime v-bind:dateTime = "dateTime" @updateDateTime="updateTerm" @deleteTerm="deleteTerm"/>
        </div>  

        <button @click="addTerm" class="button">Add term</button>  
        <div v-bind:key="lecture.lecture_id" v-for="lecture in lectures">    
            <GroupLecture v-bind:lecture = "lecture" @updateLecture = "updateLecture" @deleteLecture="deleteLecture" />
        </div>    
        <button @click="addLecture" class='button'>Add lecture</button>
        <div class="buttons">
        <button @click="deleteGroup()" class='button'>Delete course</button>    
        <button @click="updateGroup()" class='button'>Save changes</button>
        </div>
    </div>
</template>

<script>

import GroupRUD from '../../services/GroupRUD.js';
import Entry from '../../services/Entry.js';
import GroupDateTime from './GroupDateTime';
import GroupLecture from './GroupLecture';
export default {
    name: "GroupPanel",
    components:{
        GroupDateTime,
        GroupLecture
    },
    data(){
    return {
      group: Object,
      lectures: null,
      nameChange: true
    }
  },
    created(){
        GroupRUD.getGroup(this.$route.params.groupID).then(data => {
            this.group = data;
            this.refreshLectures();
        });
       
    },
    methods:{
        refreshLectures(){
            return GroupRUD.getGroupLecturesNames(this.group.lectures_list).then(data=> this.lectures=data);
        },
        updateGroup(){
            GroupRUD.updateGroup(this.group);
        },
        async deleteGroup(){
            GroupRUD.deleteGroup(this.group.pk);
            await this.$router.push('/groups');
        },
        changeCourseName(){
            console.log(this.nameChange);
            this.nameChange = !this.nameChange;
            console.log(this.nameChange);
        },
        addLecture(){
            this.group.lectures_list.push({lecture_id: null,main_lecture: false});
            this.lectures.push({pk: null,first_name:"",last_name:""});
        },
        updateLecture(lecture,firstName,lastName){
            new Entry().getUser(firstName,lastName).then(data=>{
                if( data!== null){
                    this.group.lectures_list.filter(elem => elem.lecture_id===lecture.pk)[0].lecture_id = data[0].pk;
                    this.refreshLectures();
                }
            }).catch(e=>console.log(e));
        },
        deleteLecture(lecture){
            this.group.lectures_list = this.group.lectures_list.filter(elem => elem.lecture_id !== lecture.pk);
            this.lectures = this.lectures.filter(elem => elem.pk !== lecture.pk);
        },
        addTerm(){
            this.group.date_time.push({day_of_week: "",time: ""});
        },
        deleteTerm(dateTime){
            this.group.date_time = this.group.date_time.filter(elem => elem!== dateTime);
        },
        updateTerm(dateTime,day,time){
            dateTime.day_of_week = day;
            dateTime.time = time;
        }

        
    }
}
</script>


<style scoped>
@import './stylesheet.css';    
</style>