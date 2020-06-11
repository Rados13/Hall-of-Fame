<template lang="html">

  <section class="welcome">
    <div id = "message">
        <p>Welcome to the Hall Of Fame</p>
    </div>

    <div id="entries">
        <div class="entry">
          <Login/>
        </div>
      <div class="entry">
        <Register/>
      </div>
    </div>

  </section>

</template>

<script lang="js">

  import Login from "./components/users/Login";
  import Register from "./components/users/Register";
  export default  {
    name: 'welcome',
    components: {Register, Login},
    props: [],
    mounted () {

    },
    data () {
      return {

      }
    },
    methods: {

    },
    computed: {

    }
}

</script>

<style scoped>
   p{
    font-size: 40px
  }

  #entries{
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-column-gap: 16px;
  }

  #message{
      margin: 100px 0;
  }

</style>
