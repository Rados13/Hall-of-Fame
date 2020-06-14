<template>
    <div class="list-item">
        
        <p> {{user.first_name}}  {{user.last_name}} </p>
        <p> Student: <input type="checkbox" v-bind:active="user.is_student" v-model='user.is_student'></p>
        <p> Lecture: <input type="checkbox" v-bind:active="user.is_lecture" v-model='user.is_lecture'> </p>
        <p> Admin:   <input type="checkbox" v-bind:active="user.is_admin" v-model='user.is_admin'> </p>
        <button @click="saveChanges" class="button">Save changes</button>
        <p>Lecture groups: </p>
        
        <p>Student groups: </p>

    </div>    
</template>

<script>

import Entry from '../../services/Entry.js';
// import GroupRUD from '../../services/GroupRUD.js';

export default {
    name: "AdminPanel",
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
        });
    },
    methods:{
        saveChanges(){
            console.log(this.user);
            Entry.patchUserData({"is_admin": this.user.is_admin,"is_lecture": this.user.is_lecture,
            "is_student": this.user.is_student}, this.user.pk);
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
    background: #292929;
    color: #fff;
    border: none;
    padding: 8px 20px 12px 20px;
    margin: 1%;
    align-self: center;
    cursor: pointer;
}
</style>