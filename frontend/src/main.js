import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import Login from './components/Login.vue'
import StudentList from './components/StudentList.vue'
import Register from './components/Register.vue'

Vue.config.productionTip = false

Vue.use(VueRouter)

const routes = [
  { path: '/login', component: Login },
  { path: '/register', component: Register },
  { path: '/students', component: StudentList },
  // { path: '/groups', component: GrouptList }
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
