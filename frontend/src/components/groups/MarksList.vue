<template>
    <div class='item-list'>
        <p>{{this.studentName}} | Final Grade: {{this.finalGrade}} <button @click="addMark" class="button">Add mark</button></p>
        <div v-bind:key="mark.for_what" v-for="mark in marksList">
           <MarkElem v-bind:mark="mark" @deleteMark="$emit('deleteMark',studentID,mark)" @changeMark="changeMark"></MarkElem>
        </div>
    </div>
</template>
<script>

import MarkElem from './MarkElem';
export default {
    name: "MarksList",
    components:{
        MarkElem,
    },
    props: ['studentName','marksList','studentID','finalGrade'],
    methods:{
        changeMark(mark,value,description,note,maxPoints){
            this.$emit('changeMark',mark,value,description,note,maxPoints);
        },
        addMark(){
            this.$emit('addMark');
        }
    }
}
</script>

<style scoped>
@import './stylesheet.css';    
</style>