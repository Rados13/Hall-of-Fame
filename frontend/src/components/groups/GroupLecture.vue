<template>
         <div v-if="!change">
            <p> Lecture: {{lecture.first_name}} {{lecture.last_name}} 
                <button @click="change=!change" class='button'>Modify</button>
                <button @click="$emit('deleteLecture',lecture)" class="del">X</button>               
            </p>
        </div>  
        <div v-else>
            <form action='#' @submit.prevent = "updateLecture()">
                <p><input type='text' v-bind:first_name=first_name v-model='first_name'>
                <input type='text' v-bind:last_name=last_name v-model='last_name'></p>
                <p><input type='submit' value='Submit' ></p>
            </form>
        </div>

</template>
<script>

export default {
    name: "GroupLecture",
    props: ['lecture'],
    data(){
        return {
        first_name: this.lecture.first_name,
        last_name: this.lecture.last_name,  
        change: false,
        }
    },
    methods:{
        updateLecture(){
            this.change = !this.change;
            this.$emit('updateLecture',this.lecture,this.first_name,this.last_name);
        }
    }
}

</script>

<style scoped>
@import './stylesheet.css';    
</style>