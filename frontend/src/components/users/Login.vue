<template>
    <div id="app">
        <p>{{text}}</p>
        <h1>Login</h1>
        <form action='#' @submit.prevent='login'>
            <p><input type='text' placeholder="Email" v-model='email'></p>
            <p><input type='text' placeholder="Password" v-model='password'></p>
            <p><input type='submit' value='Submit'></p>
        </form>
    </div>
</template>

<script>


    import Entry from '../../services/Entry.js';

    export default {
        name: 'Login',
        components: {},
        data() {
            return {
                email: '',
                password: '',
                text: '',
            }
        },
        methods: {
            login() {
                console.log("Start");
                new Entry(this.$router).login(this.email, this.password);
                console.log("End");
            }
        }
    }
</script>