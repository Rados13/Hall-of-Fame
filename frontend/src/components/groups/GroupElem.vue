<template>
    <div class="list-item">
        <div id="courseName">
            <p>{{group.course}}</p>
        </div>
        <div v-bind:key="dateTime.day_of_week" v-for="dateTime in group.date_time">
            <p> Day: {{dateTime.day_of_week}} time: {{dateTime.time}}</p>
        </div>
        <div v-bind:key="elem.pk" v-for="elem in group.lectures_list">
            <p> Lecturer: {{elem.lecture.first_name}} {{elem.lecture.last_name}}</p>
        </div>
        <div class="buttons" v-if="!toWatch">
            <button v-if="!isStudent && !isLecture && $store.state.isLogged" @click="signFor(group.pk)" class='button'>
                Sign for course
            </button>
            <button v-if="isStudent" @click="goToStudentPanel(group.pk)" class='button'>Show my grades and inattendace
            </button>
            <button v-if="isLecture" @click="goToGroupPanel(group.pk)" class='button'>Go to group panel</button>
        </div>
    </div>
</template>

<script>

    import GroupRUD from '../../services/GroupRUD.js';

    export default {
        name: "GroupElem",
        props: ['group', 'isStudent', 'isLecture', 'toWatch'],
        data() {
            return {
                lectures: [],
            }
        },
        methods: {
            goToGroupPanel(id) {
                this.$router.push('/lecturegroups/' + id);
            },
            goToStudentPanel(id) {
                this.$router.push('/studentgroups/' + id);
            },
            signFor(id) {
                GroupRUD.signFor(id);
            },

        }
    }
</script>

<style scoped>
    @import './stylesheet.css';

    #courseName p {
        font-size: 30px;
        margin: 0 0 10px 0;
    }
</style>