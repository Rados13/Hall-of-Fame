import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import Login from './components/users/Login.vue'
import StudentList from './components/users/StudentList.vue'
import Register from './components/users/Register.vue'
import CreateGroup from './components/groups/CreateGroup.vue'
import GroupList from './components/groups/GroupList.vue'
import GroupPanel from './components/groups/GroupPanel.vue'
import GroupStudentPanel from './components/groups/GroupStudentPanel.vue'

Vue.config.productionTip = false

Vue.use(VueRouter)

const routes = [
  { path: '/login', component: Login },
  { path: '/register', component: Register },
  { path: '/students', component: StudentList },
  { path: '/addGroup', component: CreateGroup },
  { path: '/groups', component: GroupList },
  { path: '/studentgroups', component: GroupList, props:{default: true, student:true}},
  { path: '/studentgroups/:groupID', component: GroupStudentPanel, props: {default: true,student: true}},
  { path: '/lecturegroups', component: GroupList, props:{default: true, lecture:true}},
  { path: '/lecturegroups/:groupID', component: GroupPanel, props: {default: true,student: true}}
]
const router = new VueRouter({
    routes,
    mode: 'history'
})

new Vue({
    el: '#app',
    router,
    render: h => h(App),
}).$mount('#app')
