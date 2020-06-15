<template>
         <div v-if="!change">
            <p> Day: {{dateTime.day_of_week}}   time: {{dateTime.time}}
                <button @click="change=!change" class='button'>Modify</button>
                <button @click="$emit('deleteTerm',dateTime)" class="del">X</button>               
            </p>
        </div>  
        <div v-else>
            <form action='#' @submit.prevent = "changeDateTime()">
                <p><input type='text' v-bind:day=day v-model='day'>
                <input type='text' v-bind:time=time v-model='time'></p>
                <p><input type='submit' value='Submit' ></p>
            </form>
        </div>

</template>
<script>

export default {
    name: "GroupDateTime",
    props: ['dateTime'],
    data(){
        return {
        day: this.dateTime.day_of_week,
        time: this.dateTime.time,  
        change: false,
        }
    },
    methods:{
        changeDateTime(){
            this.change = !this.change;
            this.$emit('updateDateTime',this.dateTime,this.day,this.time);
        }
    }
}

</script>

<style scoped>
@import './stylesheet.css';    
</style>