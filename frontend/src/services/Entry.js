

import axios from 'axios';
const registerURL = 'http://127.0.0.1:8000/api/users/';
const tokenURL = 'http://127.0.0.1:8000/api/token';
    

export default class Entry{
    $router = null;
    constructor(router){
        this.$router = router;
    }
    register(email,first_name,last_name,password){
        axios.post(registerURL,{email: email,first_name: first_name,
        last_name:last_name,password: password}).then(() =>{
            this.login(email,password);
        }).catch(error => {
            console.log(error);
            this.text = 'Bad email or password';
        });
    }
    login(email,password){
      localStorage.setItem("email", email);
      localStorage.setItem("password", password);
        axios.post(tokenURL,{email: email,password: password}).then(response =>{
            localStorage.setItem("accessToken", response.data.access);      
            localStorage.setItem("refreshToken", response.datarefresh);
            this.$router.push('/students');
        }).catch(error => {
            console.log(error);
        });  
    }
    refreshToken(){
        axios.post()
    }

    async getUsers(){
        return await axios.get(registerURL,{
            headers: {Authorization: `Bearer ${localStorage.getItem("accessToken")}`}
        }).then(response =>{
            return response.data;
        }).catch(e => {
        console.error(e);
        });  
    }
    async getUser(firstName,lastName){
        var users;
        await this.getUsers().then(data => users = data);
        return users.filter(user => (user.first_name === firstName && user.last_name===lastName));    
    }
}