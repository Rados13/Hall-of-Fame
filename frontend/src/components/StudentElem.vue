<template>
    <!-- <div v-bind:class="{'styleclass':value}"> If value is True set styleclass on this div -->
    <div class="list-item"> 
        <p>
            <input type="checkbox" v-on:change="markComplete">
            {{student.name}} {{student.surname}}
            <button @click="$emit('del-student',student.id)" class='del'>X</button>    
        </p> 
    </div>
</template>

<script>
export default {
    name: "StudentElem",
    props: ['student'],
    methods:{
        markComplete(){
            console.log(123)
        }
    }
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
    float: right;
  }
</style>