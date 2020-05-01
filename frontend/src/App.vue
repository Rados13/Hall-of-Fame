<template>
    <div id="app">
        <NavbarApp/>
        <DebugApp/>
        <router-view></router-view>

    </div>
</template>

<script>

    import axios from 'axios';
    import NavbarApp from './components/Navbar';
    import DebugApp from './components/Debug';

    const baseURL = 'http://127.0.0.1:8000/api/users/';

    export default {
        name: 'App',
        components: {
            NavbarApp,
            DebugApp
        },
        data() {
            return {
                token: localStorage.getItem("accesToken"),
                students: [],
                studentName: '',
            }
        },
        methods: {
            async getUsers() {
                try {
                    await axios.get(baseURL, {
                        headers: {Authorization: `Bearer ${localStorage.getItem("accessToken")}`}
                    }).then(response => {
                        console.log(response.data);
                        this.students = response.data;
                    });
                } catch (e) {
                    console.error(e);
                }
            },
            async addStudent() {
                const res = await axios.post(baseURL, {Name: this.studentName});
                this.students = [...this.students, res.data];
                this.studentName = null;
            },
            deleteStudent(id) {
                console.log(this.students);
                this.students = this.students.filter(student => student.id !== id);
            },
            setToken(result) {
                if (result == true) {
                    this.getUsers();
                    this.token = true;
                }
            }
        }
    }
</script>

<style>
    #app {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        margin-top: 60px;
    }
</style>
