<template>
         <div v-if="!change">
            <p> Lecture: {{lecture.lecture.first_name}} {{lecture.lecture.last_name}} 
                <button @click="change=!change" class='button'>Modify</button>
                <button @click="$emit('deleteLecture',lecture)" class="del">X</button>               
            </p>
        </div>  
        <div v-else>
            <form action='#' @submit.prevent = "updateLecture()">
                <p>Name: <input type='text' v-bind:first_name=first_name v-model='first_name'>
                Last name: <input type='text' v-bind:last_name=last_name v-model='last_name'></p>
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
        first_name: "",
        last_name: "",  
        change: false,
        }
    },
    created(){
        if(this.lecture===null)this.change=true;
        else {
            this.first_name=this.lecture.lecture.first_name;
            this.last_name = this.lecture.lecture.last_name;
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