<template>
    <div id='app'>
    <ul> <router-link to="/login">Login</router-link></ul>
    <ul> <router-link to="/register">Register</router-link></ul>
    <ul> <router-link to="/students">User data</router-link> </ul>
    <!-- <ul> <router-link to="/groups">My groups</router-link> </ul> -->
    </div>
</template>

<script>
export default {
    name: 'NavbarApp',
    components:{
    },
}
</script>

