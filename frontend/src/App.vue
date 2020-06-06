<template>
    <div id="main">
        <h1 id="title">Hall of Fame</h1>
        <NavbarApp/>
        <router-view></router-view>
    </div>
</template>

<script>

    import NavbarApp from './components/Navbar';


    export default {
        beforeCreate: function(){
            document.body.classList.add('home');
            console.log("Happen");
        },
        name: 'App',
        components: {
            NavbarApp,
        },
    }
</script>

<style>
    #main {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: white;
        background: grey;
        height: 100%;
        margin: 0;
        padding: 20px;
        min-height: 100vh;
    }
    #title{
        padding-top: 60px;
    }
    .home{
    background-color: grey;
    margin: 0;
}
</style>
