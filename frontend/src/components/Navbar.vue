<template>
    <div id='app' >
        <div id="left" class="has_flex" style="flex-grow: 8">
            <div v-if="!isLogged" class="has_flex">
                <ul> <router-link to="/login">Login</router-link></ul>
                <ul> <router-link to="/register">Register</router-link></ul>
            </div>
            <ul> <router-link to="/groups">Groups list</router-link> </ul>
            <div v-if="isStudent" class="has_flex">
                <ul> <router-link to="/studentgroups">My student groups</router-link> </ul>
            </div>
            <div v-if="isLecture" class="has_flex">
                <ul> <router-link to="/students">User data</router-link> </ul>
                <ul> <router-link to="/addGroup">Create group</router-link> </ul>
                <ul> <router-link to="/lecturegroups">My lecture groups</router-link> </ul>
            </div>
        </div>
        <div id="right" class="has_flex" style="flex-grow: 2">
            <div v-if="isLogged" class="has_flex">
                <ul class="name">{{firstName}} {{lastName}}  </ul>
                <ul><a @click="logout">Logout</a></ul>
            </div>
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
        isLogged(){
            return this.$store.state.isLogged;
        },
        firstName(){
            return this.$store.state.firstName;
        },
        lastName(){
            return this.$store.state.lastName;
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
    #app {
        display: flex;
        padding-bottom: 20px;
    }

    .has_flex {
        display: flex;
        flex-direction: row;
        margin: 0;
        padding: 0;
        list-style: none;
        font-size: medium;
    }

    #left {
        justify-content: left;
    }
    #right {
        justify-content: right;
    }

    a:hover {
        color: #bebebe;
    }

    ul {
      padding: 0;
    }

    .name {
        color: lightgray;
        padding: 0 15px;
    }

    a{
        cursor: pointer;
        display: block;
        color: white;
        text-decoration: none;
        /*background-color: black;*/
        padding: 0 15px;
    }

</style>

