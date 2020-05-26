

import axios from 'axios';
const baseURL = 'http://127.0.0.1:8000/api/groups/';
const statsURL = 'http://127.0.0.1:8000/api/groups/stats/';
const lectureURL = 'http://127.0.0.1:8000/api/lectures/';
const studentURL = 'http://127.0.0.1:8000/api/students/';

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
    static async getGroup(id){
      return await axios.get(baseURL+id+'/',{
        headers: {Authorization: `Bearer ${localStorage.getItem("accessToken")}`}
      }).then(response =>{
        return response.data;
      }).catch(e =>{
      console.error(e);
    });  
    }
  
    
    static async signFor(id){
        await axios.post(baseURL+id+"/student/",{
          headers: {Authorization: `Bearer ${localStorage.getItem("accessToken")}`},
        }).catch(e => console.error(e));
    }

    static async deleteGroup(id){
      await axios.delete(baseURL+id+'/',{
        headers: {Authorization: `Bearer ${localStorage.getItem("accessToken")}`}
      }).catch(e=> console.error(e));
    }

    static async updateGroup(group){
      await axios.patch(baseURL+group.pk+'/',{
        headers: {Authorization: `Bearer ${localStorage.getItem("accessToken")}`},
        group: {course: group.course, date_time: group.date_time, 
        lectures_list: group.lectures_list, enrolled_list: group.enrolled_list, course_end: group.course_end}
      }).catch(e=> console.error(e));
    }

    static async addMarkAllStudent(id,marks,markName,maxPoints){
      await axios.post(baseURL+id+"/markAll/",{
        headers: {Authorization: `Bearer ${localStorage.getItem("accessToken")}`},
        student_marks: marks, mark_name: markName, max_points: maxPoints
      }).catch(e => console.log(e));
    }

    static async getStats(groupID){
      return await axios.get(statsURL,{
        headers: {Authorization: `Bearer ${localStorage.getItem("accessToken")}`},
        params: {groups_id: [groupID,] },
      }).then(response=> {return response.data;}).catch(e => console.log(e));
    }
    static async calculateAllFinalGrade(groupID){
      await axios.post(baseURL+groupID+'/finalGrade/',{
        headers: {Authorization: `Bearer ${localStorage.getItem("accessToken")}`},});
    }
}