<template>
         <div v-if="!change">
            <p> Value: {{mark.value}}   for what {{mark.for_what}}   additional note {{mark.note}}
                <button @click="change=!change" class='button'>Modify</button>
                <button @click="$emit('deleteMark',mark)" class="del">X</button>               
            </p>
        </div>  
        <div v-else>
            <form action='#' @submit.prevent = "changeMark()">
                <p>
                <input type='number' v-bind:grade=grade v-model='grade'>
                <input type='text' v-bind:description=description v-model='description'>
                <input type='text' v-bind:note=note v-model='note'>
                </p>
                <p><input type='submit' value='Submit' ></p>
            </form>
        </div>

</template>

<script>

export default {
    name: "MarkElem",
    props: ['mark'],
    data(){
        return {
            grade: this.mark.value,
            description: this.mark.description,  
            note: this.mark.note,  
            change: false,
        }
    },
    methods:{
        changeMark(){
            this.change = !this.change;
            this.$emit('changeMark',this.mark,this.grade,this.description,this.note);
        }
    }
}

</script>

<style scoped>
@import './stylesheet.css';    
</style>