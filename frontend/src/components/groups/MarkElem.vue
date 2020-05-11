<template>
         <div v-if="!change">
            <p> Value: {{mark.value}} / {{mark.max_points}} | For what: {{mark.for_what}} |  Additional note: {{mark.note}}
                <button @click="change=!change" class='button'>Modify</button>
                <button @click="$emit('deleteMark',mark)" class="del">X</button>               
            </p>
        </div>  
        <div v-else>
            <form action='#' @submit.prevent = "changeMark()">
                <p>
                    <input type='number' v-bind:grade=grade v-model='grade'>
                    <input type='number' v-bind:maxPoints=maxPoints v-model='maxPoints'>
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
            description: this.mark.for_what,  
            note: this.mark.note,  
            maxPoints: this.mark.max_points,
            change: false,
        }
    },
    methods:{
        changeMark(){
            this.change = !this.change;
            this.$emit('changeMark',this.mark,this.grade,this.description,this.note,this.maxPoints);
        }
    }
}

</script>

<style scoped>
@import './stylesheet.css';    
</style>