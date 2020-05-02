

import axios from 'axios';
import Entry from './Entry';
const baseURL = 'http://127.0.0.1:8000/api/groups/';
const lectureURL = 'http://127.0.0.1:8000/api/groups/';
const studentURL = 'http://127.0.0.1:8000/api/groups/';

export default class {
    static async getGroups(){
      return await axios.get(baseURL,{
          headers: {Authorization: `Bearer ${localStorage.getItem("accessToken")}`}
        }).then(response =>{
          return response.data;
        }).catch(e =>{
        console.error(e);
      });  
    }
    static async getLectureGroups(){
      return await axios.get(lectureURL, {
        headers: {Authorization: `Bearer ${localStorage.getItem("accessToken")}`}
      }).then(response => {return response.data;}).catch(e=> console.error(e)); 
    }  
    static async getStudentGroups(){
      return await axios.get(studentURL, {
        headers: {Authorization: `Bearer ${localStorage.getItem("accessToken")}`}
      }).then(response => {return response.data;}).catch(e=> console.error(e)); 
    }
    static async getGroup(id,isLecture = true){
      var groups = [];
      if(isLecture){
        await this.getLectureGroups().then(data => groups = data);
      }else{
        await this.getStudentGroups().then(data=> groups = data)
      }
      return groups.filter(e => e.pk == id)[0];
    }
  
    

    static async getGroupLecturesNames( lecturesList){
      var users;
      await new Entry().getUsers().then( data => users = data);
      return users.filter(elem => lecturesList.map(elem=>elem.lecture_id).includes(elem.pk));
    }
    static async getGroupStudentsNames( studentList){
      var users;
      await new Entry().getUsers().then( data => users = data);
      return users.filter(elem => studentList.map(elem=>elem.user_id).includes(elem.pk));
    }
    
    static async signFor(id){
        await axios.post(baseURL+id+"/student/",{
          headers: {Authorization: `Bearer ${localStorage.getItem("accessToken")}`},
        }).then(response => {
          console.log(response.data);
        }).catch(e => console.error(e));
    }

    static async deleteGroup(id){
      await axios.delete(baseURL+id+'/',{
        headers: {Authorization: `Bearer ${localStorage.getItem("accessToken")}`}
      }).catch(e=> console.error(e));
    }

    static async updateGroup(group){
      console.log(group);
      await axios.patch(baseURL+group.pk+'/',{
        headers: {Authorization: `Bearer ${localStorage.getItem("accessToken")}`},
        group: {course: group.course, date_time: group.date_time, 
        lectures_list: group.lectures_list, enrolled_list: group.enrolled_list}
      }).catch(e=> console.error(e));
    }
}