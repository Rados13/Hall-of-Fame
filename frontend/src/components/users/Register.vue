<template>
    <div id="app">
        <p>{{text}}</p>
        <h1>Register</h1>
        <form action='#' @submit.prevent='register'>
            <p><input type='text' placeholder="email" v-model='email'></p>
            <p><input type='text' placeholder="First name" v-model='first_name'></p>
            <p><input type='text' placeholder="Last name" v-model='last_name'></p>
            <p><input type='text' placeholder="password" v-model='password'></p>
            <p><input type='submit' value='Submit'></p>
        </form>
    </div>
</template>

<script>

    import Entry from '../../services/Entry';


    export default {
        name: 'Register',
        components: {},
        data() {
            return {
                email: '',
                password: '',
                first_name: '',
                last_name: '',
                text: '',
            }
        },
        methods: {
            async register() {
                await new Entry(this.$router).register(this.email, this.first_name, this.last_name, this.password);
                this.$store.commit('getInfo');
                this.$store.dispatch({type: 'refreshThread'});
            },
        }
    }
</script>