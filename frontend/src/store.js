import Vue from 'vue';
import Vuex from 'vuex';
import Entry from './services/Entry';
import GroupRUD from './services/GroupRUD';

Vue.use(Vuex);

export const store = new Vuex.Store({
    state: {
        isStudent: false,
        isLecture: false, 
        isAdmin: false,
        isLogged: false,
        firstName: 'none',
        lastName: 'none',
        groups: [],
    },
    getters:{},
    mutations:{
        getInfo(state){
            Entry.getUserInfo().then(data =>{
                state.isStudent = data.is_student;
                state.isLecture = data.is_lecture;
                state.isAdmin = data.is_admin;
                state.firstName = data.first_name;
                state.lastName = data.last_name;
                state.isLogged = true;
            }).catch(error => console.log(error));
        },
        logout(state){
            state.isLogged = false;
            state.isLecture= false;
            state.isStudent= false;
            state.isAdmin= false;
            localStorage.setItem('accessToken','');
            localStorage.setItem('refreshToken','');
        },
        refreshToken(state){
            if(state.isLogged){
                Entry.refreshToken();    
                this.dispatch('refreshThread');
            }else{
                this.$router.push('/');
            }
        },
        getGroups(state,param){
            if(param==='student')GroupRUD.getStudentGroups().then(data => state.groups = data);
            else if(param==='lecture')GroupRUD.getLectureGroups().then(data=>state.groups=data);
            else GroupRUD.getGroups().then(data => state.groups=data);
        }
    },
    actions:{
        refreshThread(context){
            setTimeout(() => context.commit('refreshToken'),59000);
        }
    }
});