<template>
    <form action='#' @submit.prevent = "$emit('addAllMark',grades,forWhat)">
    Name of mark: <input type='text' v-bind:description=forWhat v-model='forWhat'>
    <div class='item-list' v-bind:key="student.user_id" v-for="student in studentList">
        <p>
            {{student.first_name}}  {{student.last_name}} 
            Value: <input type='number' v-bind:key=grades[student.user_id][value] v-model='grades[student.user_id][value]'>
            Note: <input type='text' v-bind:note=grades[student.user_id][note] v-model='grades[student.user_id][note]'>
        </p>
    </div>
    <p><input type='submit' value='Submit' ></p>
    </form>
</template>
<script>

export default {
    name: "MarksList",
    props: ['studentList'],
        data(){
        return {
            forWhat: "",
            grades: {},
            value:"value",
            note:"note"
        }
    },
    created(){
        for(const elem of this.studentList){
            this.grades[elem.user_id] = {};
            this.grades[elem.user_id][this.value] = 0;
            this.grades[elem.user_id][this.note]="";
        }
    },
}
</script>

<style scoped>
@import './stylesheet.css';    
</style>