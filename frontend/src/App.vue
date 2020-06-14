<template>
    <div id="main">
        <!--        <h1 id="title">Hall of Fame</h1>-->
        <NavbarApp v-if="isLogged" />
        <router-view></router-view>
    </div>
</template>

<script>

    import NavbarApp from './components/Navbar';


    export default {
        beforeCreate: function () {
            document.body.classList.add('home');
        },
        name: 'App',
        components: {
            NavbarApp,
        },
        computed: {
            isLecture() {
                return this.$store.state.isLecture || this.$store.state.isAdmin;
            },
            isStudent() {
                return this.$store.state.isStudent || this.$store.state.isAdmin;
            },
            isLogged() {
                return this.$store.state.isLogged;
            }
        },
    }
</script>


<style>

    #main {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: white;
        background: #545454;
        height: 100%;
        margin: 0;
        padding: 20px;
        min-height: 100vh;
    }

    body {
        max-width: 1200px;
        margin: auto;
    }

    #title {
        padding-top: 1px;
    }

    .home {
        background-color: #545454;
    }

</style>
