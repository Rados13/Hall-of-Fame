<template>
    <!-- <div v-bind:class="{'styleclass':value}"> If value is True set styleclass on this div -->
    <div class="list-item"> 
        <p> Course name: {{group.course}}</p>
            <!-- <input type="checkbox" v-on:change="markComplete"> -->
        <div v-bind:key="dateTime.day_of_week" v-for="dateTime in group.date_time">    
            <p> Day: {{dateTime.day_of_week}} hour of start: {{dateTime.time}}</p>
        </div>    
        <div v-bind:key="lecture.lecture_id" v-for="lecture in group.lectures_list">    
            <p> Lecture: {{lecture.lecture_id}}</p>
        </div>    
        <div class="buttons">
        <button @click="$emit('del-group',group.pk)" class='del'>X</button>    
        <button @click="$emit('sign-group',group.pk)" class='signForGroup'>Sign for course</button>   
        </div>
    </div>
</template>

<script>
export default {
    name: "GroupElem",
    props: ['group'],
}
</script>

<style scoped>
    .list-item{
        background: #f4f4f4;
        padding: 10px;
        border-bottom: 1px #ccc dotted;
    }

    .del {
    background: #ff0000;
    color: #fff;
    border: none;
    padding: 5px 9px;
    border-radius: 50%;
    cursor: pointer;
    }
    
    .signForGroup{
    background: #ff0000;
    color: #fff;
    border: none;
    padding: 5px 9px;
    margin-left: 5%;
    cursor: pointer;        
    }
    .buttons{
        display: flex;
        flex-flow: row;
        justify-content: center;
    }
</style>