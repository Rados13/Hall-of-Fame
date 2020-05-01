

import axios from 'axios';
import Entry from './Entry';
const baseURL = 'http://127.0.0.1:8000/api/groups/';
    

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
    static async getGroup(id){
      var groups = [];
      await this.getGroups().then(data => {
        groups = data;
      });
      return groups.filter(e => e.pk == id)[0];
    }
    static async getGroupLecturesNames( lecturesList){
      var users;
      await new Entry().getUsers().then( data => users = data);
      return users.filter(elem => lecturesList.map(elem=>elem.lecture_id).includes(elem.pk));
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
        lectures_list: group.lectures_list}
      }).catch(e=> console.error(e));
    }
}