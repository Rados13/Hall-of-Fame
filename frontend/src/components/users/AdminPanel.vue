<template>
    <div class="list-item">
        
        <p> {{user.first_name}}  {{user.last_name}} </p>
        <p> Student: <input type="checkbox" v-bind:active="user.is_student" v-model='user.is_student'></p>
        <p> Lecture: <input type="checkbox" v-bind:active="user.is_lecture" v-model='user.is_lecture'> </p>
        <p> Admin:   <input type="checkbox" v-bind:active="user.is_admin" v-model='user.is_admin'> </p>
        <p> Active:   <input type="checkbox" v-bind:active="user.is_active" v-model='user.is_active'> </p>
        <button @click="saveChanges" class="button">Save changes</button>
        
        <p>Lecture groups: </p>
        <div v-bind:key="group.pk" v-for="group in lectureGroups">
            <GroupElem v-bind:group="group" v-bind:toWatch="true"/>
        </div>
        <p>Student groups: </p>
        <div v-bind:key="group.pk" v-for="group in studentGroups">
            <GroupElem v-bind:group="group" v-bind:toWatch="true" v-bind:isLecture="false" v-bind:isStudent="false"/>
        </div>
    </div>    
</template>

<script>

import Entry from '../../services/Entry.js';
import GroupRUD from '../../services/GroupRUD.js';
import GroupElem from '../groups/GroupElem';

export default {
    name: "AdminPanel",
    components:{
        GroupElem,
    },
    data() {
        return {
            user: Object,
            lectureGroups: [],
            studentGroups: []
        }
    },
    created(){
        Entry.getUserByID(this.$route.params.userID).then(result => {
            this.user=result;
            GroupRUD.getStudentGroupsUser(this.user.pk).then(result => this.studentGroups = result);
            GroupRUD.getLectureGroupsUser(this.user.pk).then(result => this.lectureGroups = result);
        });
    },
    methods:{
        saveChanges(){
            Entry.patchUserData({"is_admin": this.user.is_admin,"is_lecture": this.user.is_lecture,
            "is_student": this.user.is_student, "is_active": this.user.is_admin}, this.user.pk);
        }
    }
}
</script>

<style scoped>
    .list-item{
        background: #222222;
        padding: 10px;
        border-bottom: 1px #ccc outset;
    }

    .button {
    background: #393939;
    color: #fff;
    border: none;
    padding: 8px 20px 12px 20px;
    margin: 1%;
    align-self: center;
    cursor: pointer;
    }
</style>