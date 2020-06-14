<template>
    <div id='app'>
        <div v-if="!isLogged">    
            <ul> <router-link to="/login">Login</router-link></ul>
            <ul> <router-link to="/register">Register</router-link></ul>
        </div>
        <ul> <router-link to="/groups">Groups list</router-link> </ul>
        <div v-if="isStudent">
            <ul> <router-link to="/studentgroups">My student groups</router-link> </ul>
        </div>
        <div v-if="isLecture">
            <ul> <router-link to="/addGroup">Create group</router-link> </ul>
            <ul> <router-link to="/lecturegroups">My lecture groups</router-link> </ul>
        </div>
        <div v-if="isAdmin">
            <ul> <router-link to="/users">User data</router-link> </ul>
        </div>
        <div v-if="isLogged">
            <ul><a @click="logout">Logout</a></ul>
        </div>
    </div>
</template>

<script>


export default {
    name: 'NavbarApp',
    computed:{
        isLecture(){
            return this.$store.state.isLecture || this.$store.state.isAdmin;
        },
        isStudent(){
            return this.$store.state.isStudent || this.$store.state.isAdmin;
        },
        isAdmin(){
            return this.$store.state.isAdmin;
        },
        isLogged(){
            return this.$store.state.isLogged;
        }
    },
    methods:{
        logout(){
            this.$store.commit({type: 'logout'});
            this.$router.push('/');
        }
    }
}
</script>

<style scoped>
    div {
        display: flex;
        flex-direction: row;
        margin: 0;
        padding: 0;
        list-style: none;
        justify-content: center;
        font-size: large;
    }
    a:hover {
        color: #bebebe;
    }
</style>
<style>
    a{
        cursor: pointer;
        display: block;
        color: white;
        text-decoration: none;
        /*background-color: black;*/
        padding: 0 20px;
    }
</style>

