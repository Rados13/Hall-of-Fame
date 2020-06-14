<template>
    <div class="list-item"> 
        <p> {{user.first_name}} {{user.last_name}} </p>         
        <p><button @click="$emit('goToAdmin',user.pk)">Go to admin panel</button></p>
        <button @click="$emit('deleteUser',user.pk)" class='del'>X</button>
    </div>
</template>

<script>


export default {
    name: "UserElem",
    props: ['user'],
}
</script>

<style scoped>
    .list-item{
        background: #222222;
        padding: 10px;
        border-bottom: 1px #ccc outset;
        display: flex;
        flex-direction: column;
        justify-content: center;

    }


    .del {
    background: #ff0000;
    color: #fff;
    border: none;
    padding: 5px 9px;
    border-radius: 50%;
    height: 50%;
    justify-self: center;
    align-self: center;
    cursor: pointer;
    float: right;
  }
</style>