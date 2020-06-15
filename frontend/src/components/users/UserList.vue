<template>
    <div class="hello">
        <div v-bind:key="user.pk" v-for="user in users">
            <UserElem v-bind:user="user" @goToAdmin="goToAdminPanel"/>
        </div>
    </div>
</template>

<script>

import UserElem from './UserElem.vue';
import Entry from '../../services/Entry.js';


export default {
    name: 'UserList',
    components: {
        UserElem
    },
    data() {
        return {
            users: []
        }
    },
    created() {
        Entry.getUsers().then(data => {
            this.users=data;
        });
    },
    methods:{
        goToAdminPanel(userID){
            this.$router.push({path: '/adminPanel/' + userID});
        }
    }  
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    h3 {
        margin: 40px 0 0;
    }

    ul {
        list-style-type: none;
        padding: 0;
    }

    li {
        display: inline-block;
        margin: 0 10px;
    }

    a {
        color: #42b983;
    }
</style>
