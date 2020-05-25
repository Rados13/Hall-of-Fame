<template>
         <div v-if="!change">
            <p> Class num: {{inattendance.class_num}}   justified {{inattendance.justified?"justified":"unjustified"}}
                <button @click="change=!change" class='button'>Modify</button>
                <button @click="$emit('deleteInattendance',inattendance)" class="del">X</button>               
            </p>
        </div>  
        <div v-else>
            <form action='#' @submit.prevent = "changeInattendance()">
                <p>
                <input type='number' v-bind:classNum=classNum v-model='classNum'>
                <input type='checkbox' v-bind:justified=justified v-model='justified'>
                </p>
                <p><input type='submit' value='Submit' ></p>
            </form>
        </div>

</template>

<script>

export default {
    name: "InattendanceElem",
    props: ['inattendance'],
    data(){
        return {
            classNum: this.inattendance.class_num,
            justified: this.inattendance.justified,  
            change: false,
        }
    },
    methods:{
        changeInattendance(){
            this.change = !this.change;
            this.$emit('changeInattendance',this.inattendance,this.classNum,this.justified);
        }
    }
}

</script>

<style scoped>
@import './stylesheet.css';    
</style>