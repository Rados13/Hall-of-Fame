<template>
         <div v-if="!change">
            <p> Lecture: {{lecture.lecture.first_name}} {{lecture.lecture.last_name}} 
                <button @click="change=!change" class='button'>Modify</button>
                <button @click="$emit('deleteLecture',lecture)" class="del">X</button>               
            </p>
        </div>  
        <div v-else>
            <form action='#' @submit.prevent = "updateLecture()">
                <select v-model="newLecture">
                        <option v-bind:key="elem.pk" v-for='elem in lectures' v-bind:value="elem.pk"> 
                            {{elem.last_name}} {{elem.first_name}}
                        </option>
                </select>
                <p><input type='submit' value='Submit' ></p>
            </form>
        </div>

</template>
<script>

export default {
    name: "GroupLecture",
    props: ['lecture','lectures'],
    data(){
        return {
        first_name: "",
        last_name: "",  
        newLecture: null,
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
            this.$emit('updateLecture',this.lecture,this.lectures.filter(elem => elem.pk === this.newLecture)[0]);
        }
    }
}

</script>

<style scoped>
@import './stylesheet.css';    
</style>