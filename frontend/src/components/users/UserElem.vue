<template>
    <div class="list-item"> 
        <p> {{user.first_name}} {{user.last_name}} </p>         
        <p><button class="button" @click="$emit('goToAdmin',user.pk)">Go to admin panel</button></p>
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

    .button {
    background: #393939;
    color: #fff;
    border: none;
    padding: 8px 20px 12px 20px;
    margin: 1%;
    align-self: center;
    cursor: pointer;
    }
</style>