<template>
    <div class="hello">
        <h1>Hello world</h1>
        <div v-bind:key="student.id" v-for="student in students">
            <StudentElem v-bind:student="student" v-on:del-student="deleteUser(student.id)"/>
        </div>
    </div>
</template>

<script>

    import StudentElem from './StudentElem.vue';
    import Entry from "../../services/Entry";
    // import axios from 'axios';

    const baseURL = 'http://127.0.0.1:8000/api/users/';

    export default {
        name: 'StudentList',
        components: {
            StudentElem
        },
        data() {
            return {
                students: []
            }
        },
        // props: ['students'],
        created() {
            this.getUsers();
        },
        methods: {

            getUsers() {
                Entry.sendGet(baseURL).then(r => {this.students = r.data; this.$forceUpdate();}, r => console.log(r));
                // console.log();
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
