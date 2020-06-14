<template>
    <form action='#' @submit.prevent = "$emit('addAllMark',grades,forWhat,maxPoints)">
    <p>Name of mark: <input type='text' v-bind:description=forWhat v-model='forWhat'></p>
    <p>Max points: <input type='number' v-bind:description=maxPoints v-model='maxPoints'></p>
    <div class='item-list' v-bind:key="elem.user" v-for="elem in studentList">
        <p>{{elem.student.first_name}}  {{elem.student.last_name}} </p>
        <p> Value: <input type='number' v-bind:key=grades[elem.student.pk][value] v-model='grades[elem.student.pk][value]'></p>
        <p>Note: <input type='text' v-bind:note=grades[elem.student.pk][note] v-model='grades[elem.student.pk][note]'></p>
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
            this.grades[elem.student.pk] = {};
            this.grades[elem.student.pk][this.value] = 0;
            this.grades[elem.student.pk][this.note]="";
        }
    },
}
</script>

<style scoped>
@import './stylesheet.css';    
</style>