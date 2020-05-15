<template>
    <form action='#' @submit.prevent = "$emit('addAllMark',grades,forWhat,maxPoints)">
    Name of mark: <input type='text' v-bind:description=forWhat v-model='forWhat'>
    Max points: <input type='number' v-bind:description=maxPoints v-model='maxPoints'>
    <div class='item-list' v-bind:key="student.user" v-for="student in studentList">
        <p>
            {{student.first_name}}  {{student.last_name}} 
            Value: <input type='number' v-bind:key=grades[student.student][value] v-model='grades[student.student][value]'>
            Note: <input type='text' v-bind:note=grades[student.student][note] v-model='grades[student.student][note]'>
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
            maxPoints: "",
            grades: {},
            value:"value",
            note:"note"
        }
    },
    created(){
        for(const elem of this.studentList){
            this.grades[elem.student] = {};
            this.grades[elem.student][this.value] = 0;
            this.grades[elem.student][this.note]="";
        }
    },
}
</script>

<style scoped>
@import './stylesheet.css';    
</style>