import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import Login from './components/users/Login.vue'
import StudentList from './components/users/StudentList.vue'
import Register from './components/users/Register.vue'
import CreateGroup from './components/groups/CreateGroup.vue'
import GroupList from './components/groups/GroupList.vue'

Vue.config.productionTip = false

Vue.use(VueRouter)

const routes = [
  { path: '/login', component: Login },
  { path: '/register', component: Register },
  { path: '/students', component: StudentList },
  { path: '/addGroup', component: CreateGroup },
  { path: '/groups', component: GroupList }
]
const router = new VueRouter({
  routes,
  mode:'history'
})

new Vue({
  el: '#app',
  router,
  render: h => h(App),
}).$mount('#app')
