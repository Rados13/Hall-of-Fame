<template>
    <div id='app'>
    <ul > <router-link to="/login">Login</router-link></ul>
    <ul> <router-link to="/register">Register</router-link></ul>
    <ul> <router-link to="/students">User data</router-link> </ul>
    <ul> <router-link to="/addGroup">Create group</router-link> </ul>
    <ul> <router-link to="/groups">Groups list</router-link> </ul>
    </div>
</template>

<script>


export default {
    name: 'NavbarApp',
    components:{
    }
}
</script>

<style scoped>
    * {
        display: flex;
        margin: 0 10px 0 0;
        padding: 0;
        list-style: none;
        justify-content: flex-start;
        flex-wrap: wrap;
    }
</style>

