
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


        <button @click="showMarks=!showMarks" class="button">Show marks</button>
        <div v-if="showMarks">
            <div  v-bind:key="student.enrolled_id" v-for="student in group.enrolled_list">
                <MarksList v-bind:student="students.filter(elem=> elem.pk==student.user_id)[0]" 
                    v-bind:marksList="student.marks_list" @changeMark='changeMark' 
                    @deleteMark='deleteMark' @addMark='addMark(student.marks_list)'
                    ></MarksList>
            </div>
            <!-- <button @click="addAllPersonMark" class="button">Add all student mark</button> -->
        </div>

        <button @click="showInattendance=!showInattendance" class="button">Show inattendance</button>
        <div v-if="showInattendance">
            <div  v-bind:key="student.enrolled_id" v-for="student in group.enrolled_list">
                <InattendanceList v-bind:student="students.filter(elem=> elem.pk==student.user_id)[0]" 
                    v-bind:inattendanceList="student.inattendances_list" @changeInattendance='changeInattendance' 
                    @deleteInattendance='deleteInattendance' @addInattendance='addInattendance(student.inattendances_list)'
                    ></InattendanceList>
            </div>
            <!-- <button @click="addAllPersonMark" class="button">Check attendance</button> -->
        </div>
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
import MarksList from './MarksList';
import InattendanceList from './InattendanceList';
export default {
    name: "GroupPanel",
    components:{
        GroupDateTime,
        GroupLecture,
        MarksList,
        InattendanceList
    },
    data(){
        return {
            group: Object,
            lectures: null,
            students: null,
            nameChange: true,
            showMarks: false,
            showInattendance: false
        }
    },
    created(){
        GroupRUD.getGroup(this.$route.params.groupID).then(data => {
            this.group = data;
            this.refreshNames();
        });
       
    },
    methods:{
        refreshNames(){
            GroupRUD.getGroupLecturesNames(this.group.lectures_list).then(data=> this.lectures=data);
            GroupRUD.getGroupStudentsNames(this.group.enrolled_list).then(data=> this.students=data);
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
                    this.refreshNames();
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
        },
        getEnrolled(id){
            return this.group.enrolled_list.filter(elem=> elem.user_id===id)[0];
        },
        changeMark(mark,value,description,note){
            mark.value = value;
            mark.for_what = description;
            mark.note = note;
        },
        deleteMark(studentID,mark){
            this.getEnrolled(studentID).marks_list = this.getEnrolled(studentID).marks_list.filter(elem => elem !== mark);
        },
        addMark(marksList){
            if(marksList===null)marksList = [];
            marksList.push({value: null, for_what:null,note:null});
        },
        changeInattendance(inattendance,classNum,justified){
            inattendance.class_num = classNum;
            inattendance.justified = justified;
        },
        deleteInattendance(studentID,inattendance){
            console.log(this.getEnrolled(studentID));
            this.getEnrolled(studentID).inattendances_list = 
            this.getEnrolled(studentID).inattendances_list.filter(elem => elem !== inattendance);
        },
        addInattendance(inattendanceList){
            if(inattendanceList===null)inattendanceList = [];
            inattendanceList.push({class_num: null, justified:false});
        },
        // addAllPersonMark(){    }

        
    }
}
</script>


<style scoped>
@import './stylesheet.css';    
</style>