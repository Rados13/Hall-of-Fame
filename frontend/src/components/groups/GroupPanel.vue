<template>
    <div>

        <div v-if="nameChange">
            <p class="course-name">{{group.course}}</p>
            <button @click="nameChange=!nameChange" class='button'>Modify course name</button>
        </div>
        <div v-else>
            <form action='#' @submit.prevent='changeCourseName()'>
                <p><input type='text' v-bind:course=group.course v-model='group.course'><input type='submit'
                                                                                               value='Submit'>
                </p>
            </form>
        </div>

        <div class="groupPanel">
            <div class="list-item">
                <p>Course ended: <input type='checkbox' v-bind:active=group.course_end v-model='group.course_end'/></p>

                <input class='button' type="submit" @click="calculateAllFinalGrade"
                       value="Calculate final grade for all students"/>

                <div class="buttons">
                    <button @click="deleteGroup()" class='button'>Delete course</button>
                    <button @click="updateGroup()" class='button'>Save changes</button>
                </div>

            </div>

            <div class="list-item">

                <div v-bind:key="lecture.lecture_id" v-for="lecture in group.lectures_list">
                    <GroupLecture v-bind:lecture="lecture" @updateLecture="updateLecture"
                                  @deleteLecture="deleteLecture"/>
                </div>

                <div v-if="addLectureBool">
                    <GroupLecture v-bind:lecture="null" @updateLecture="addLecture"
                                  @deleteLecture="addLectureBool=false"/>
                </div>
                <button @click="addLectureBool= !addLectureBool" class='button'>Add lecture</button>

            </div>


            <div class="list-item">
                <div v-bind:key="dateTime.day_of_week" v-for="dateTime in group.date_time">
                    <GroupDateTime v-bind:dateTime="dateTime" @updateDateTime="updateTerm" @deleteTerm="deleteTerm"/>
                </div>
                <button @click="addTerm" class="button">Add term</button>

            </div>


            <div class="list-item">
                <button @click="showMarks=!showMarks" class="button">Show marks</button>
                <div v-if="showMarks">
                    <div v-bind:key="elem.enrolled_id" v-for="elem in group.enrolled_list">
                        <MarksList v-bind:marksList="elem.marks_list" v-bind:finalGrade="elem.final_grade"
                                   v-bind:studentName="elem.student.first_name+'  '+elem.student.last_name"
                                   v-bind:studentID="elem.student.pk"
                                   @changeMark='changeMark' @deleteMark='deleteMark' @addMark='addMark(elem.marks_list)'
                        ></MarksList>
                    </div>
                </div>
                <button @click="addAllStudentMark=!addAllStudentMark" class="button">Add all student mark</button>
                <div v-if="addAllStudentMark">
                    <AllMarks v-bind:studentList=group.enrolled_list
                              @addAllMark='addAllMark'
                    ></AllMarks>
                </div>
            </div>


            <div class="list-item">
                <button @click="showInattendance=!showInattendance" class="button">Show inattendance</button>
                <div v-if="showInattendance">
                    <div v-bind:key="elem.enrolled_id" v-for="elem in group.enrolled_list">
                        <InattendanceList v-bind:student="elem.student"
                                          v-bind:inattendanceList="elem.inattendances_list"
                                          @changeInattendance='changeInattendance'
                                          @deleteInattendance='deleteInattendance'
                                          @addInattendance='addInattendance(elem.inattendances_list)'
                        ></InattendanceList>
                    </div>
                </div>
            </div>

            <div class="list-item">
                <button @click="getStats()" class="button">{{showGroupStats}}</button>
                <div v-if="showGroupStats==='Hide stats'">
                    <GroupStats v-bind:stats="groupStatsDictionary"
                                v-bind:link="statsLink"
                    ></GroupStats>
                </div>

            </div>
            <div class="list-item">

                <button class="button" @click="createMail">{{mailButtonText}}</button>
                <div v-if="sendMail">
                    <MailForm v-bind:users_list="group.enrolled_list"
                              v-bind:type="'lecture'"
                              @sended='createMail'
                    ></MailForm>
                </div>

            </div>


        </div>
    </div>

</template>

<script>

    import GroupRUD from '../../services/GroupRUD.js';
    import Entry from '../../services/Entry.js';
    import GroupDateTime from './GroupDateTime';
    import GroupLecture from './GroupLecture';
    import MarksList from './MarksList';
    import AllMarks from './AllMarks';
    import InattendanceList from './InattendanceList';
    import GroupStats from './GroupStats';
    import MailForm from './MailForm';

    export default {
        name: "GroupPanel",
        components: {
            GroupDateTime,
            GroupLecture,
            MarksList,
            InattendanceList,
            AllMarks,
            GroupStats,
            MailForm

        },
        data() {
            return {
                group: Object,
                nameChange: true,
                showMarks: false,
                showInattendance: false,
                addAllStudentMark: false,
                addLectureBool: false,
                showGroupStats: "Show stats",
                groupStatsDictionary: null,
                mailButtonText: "Create mail to students",
                sendMail: false,
                statsLink: ""
            }
        },
        created() {
            GroupRUD.getGroup(this.$route.params.groupID).then(data => {
                this.group = data;
            });
        },
        methods: {
            updateGroup() {
                GroupRUD.updateGroup(this.group);
            },
            async deleteGroup() {
                GroupRUD.deleteGroup(this.group.pk);
                await this.$router.push('/groups');
            },

            changeCourseName() {
                this.nameChange = !this.nameChange;
            },
            addLecture(lecture, firstName, lastName) {
                new Entry().getUser(firstName, lastName).then(data => {
                    if (data !== null) this.group.lectures_list.push({"lecture": data, "main_lecture": false});
                });
                this.addLectureBool = false;
            },
            updateLecture(lecture, firstName, lastName) {
                new Entry().getUser(firstName, lastName).then(data => {
                    if (data !== null) {
                        var newLecture = this.group.lectures_list.filter(elem => elem.lecture.pk === lecture.pk)[0];
                        newLecture.lecture = data[0];
                    }
                }).catch(e => console.log(e));
            },
            deleteLecture(elemOfArray) {
                this.group.lectures_list = this.group.lectures_list.filter(elem => elem.lecture.pk !== elemOfArray.lecture.pk);
            },


            addTerm() {
                this.group.date_time.push({day_of_week: "", time: ""});
            },
            deleteTerm(dateTime) {
                this.group.date_time = this.group.date_time.filter(elem => elem !== dateTime);
            },
            updateTerm(dateTime, day, time) {
                dateTime.day_of_week = day;
                dateTime.time = time;
            },
            getEnrolled(id) {
                return this.group.enrolled_list.filter(elem => elem.student.pk === id)[0];
            },


            changeMark(mark, value, description, note, maxPoints) {
                mark.value = value;
                mark.for_what = description;
                mark.note = note;
                mark.max_points = maxPoints;
            },
            deleteMark(studentID, mark) {
                this.getEnrolled(studentID).marks_list = this.getEnrolled(studentID).marks_list.filter(elem => elem !== mark);
            },
            addMark(marksList) {
                if (marksList === null) marksList = [];
                marksList.push({value: null, for_what: null, note: null, max_points: 0});
            },
            addAllMark(marks, forWhat, maxPoints) {
                GroupRUD.addMarkAllStudent(this.group.pk, marks, forWhat, maxPoints);
                this.addAllStudentMark = !this.addAllStudentMark;
                this.$router.go(this.$router.currentRoute)
            },

            changeInattendance(inattendance, classNum, justified) {
                inattendance.class_num = classNum;
                inattendance.justified = justified;
            },
            deleteInattendance(studentID, inattendance) {
                this.getEnrolled(studentID).inattendances_list =
                    this.getEnrolled(studentID).inattendances_list.filter(elem => elem !== inattendance);
            },
            addInattendance(inattendanceList) {
                if (inattendanceList === null) inattendanceList = [];
                inattendanceList.push({class_num: null, justified: false});
            },

            getStats() {
                if (this.showGroupStats === 'Hide stats') this.showGroupStats = 'Show stats';
                else {
                    this.showGroupStats = 'Hide stats';
                    GroupRUD.getStats(this.group.pk).then(data => {
                        this.groupStatsDictionary = data;
                        this.statsLink = this.groupStatsDictionary.link;
                        delete this.groupStatsDictionary['link'];
                    });
                }
            },
            calculateAllFinalGrade() {
                GroupRUD.calculateAllFinalGrade(this.group.pk);
                this.$router.go(this.$router.currentRoute)
            },

            createMail() {
                this.mailButtonText = this.sendMail ? "Create mail to students" : "Discard mail";
                this.sendMail = !this.sendMail;
            }

        }
    }
</script>


<style scoped>
    @import './stylesheet.css';

    .groupPanel {
        display: grid;
        grid-template-columns: 1fr 1fr;
        /*grid-column-gap: 80px;*/
    }
</style>