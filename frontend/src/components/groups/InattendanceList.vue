<template>
    <div class='item-list'>
        <p>{{this.studentName}} <button @click="addInattendance" class="button">Add inattendance</button> </p>
        <div v-bind:key="inatt.class_num" v-for="inatt in inattendanceList">
           <InattendanceElem v-bind:inattendance="inatt" @deleteInattendance="$emit('deleteInattendance',student.pk,inatt)" 
           @changeInattendance="changeInattendance"></InattendanceElem>
        </div>
    </div>
</template>
<script>

import InattendanceElem from './InattendanceElem';
export default {
    name: "InattendanceList",
    components:{
        InattendanceElem,
    },
    props: ['studentName','inattendanceList'],
    methods:{
        changeInattendance(inattendance,classNum,justified){
            this.$emit('changeInattendance',inattendance,classNum,justified);
        },
        addInattendance(){
            this.$emit('addInattendance');
        }
    }
}
</script>

<style scoped>
@import './stylesheet.css';    
</style>