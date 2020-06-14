import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import {store} from './store'
import Login from './components/users/Login.vue'
import UserList from './components/users/UserList.vue'
import AdminPanel from './components/users/AdminPanel.vue'
import Register from './components/users/Register.vue'
import CreateGroup from './components/groups/CreateGroup.vue'
import GroupList from './components/groups/GroupList.vue'
import GroupPanel from './components/groups/GroupPanel.vue'
import GroupStudentPanel from './components/groups/GroupStudentPanel.vue'
import Welcome from "./Welcome";

Vue.config.productionTip = false

Vue.use(VueRouter)

const routes = [
  { path: '/', component: Welcome },
  { path: '/login', component: Login },
  { path: '/register', component: Register },
  { path: '/users', component: UserList },
  { path: '/addGroup', component: CreateGroup },
  { path: '/groups', component: GroupList, props: {type: "all"}},
  { path: '/studentgroups', component: GroupList, props:{type: "student"}},
  { path: '/adminPanel/:userID', component: AdminPanel},
  { path: '/studentgroups/:groupID', component: GroupStudentPanel, props:{type: "student"}},
  { path: '/lecturegroups', component: GroupList, props:{type: "lecture"}},
  { path: '/lecturegroups/:groupID', component: GroupPanel, props:{type: "student"}}
]
const router = new VueRouter({
    routes,
    mode: 'history'
})

new Vue({
    el: '#app',
    store,
    router,
    render: h => h(App),
}).$mount('#app')
