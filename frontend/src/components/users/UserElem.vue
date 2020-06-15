<template>
    <div >
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
    @import "../groups/stylesheet.css";

</style>