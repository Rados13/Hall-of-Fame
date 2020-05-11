import axios from 'axios';

const registerURL = 'http://127.0.0.1:8000/api/users/';
const tokenURL = 'http://127.0.0.1:8000/api/token';
const refreshURL = 'http://127.0.0.1:8000/api/token/refresh';


export default class Entry {
    $router = null;

    constructor(router) {
        this.$router = router;
    }

    register(email, first_name, last_name, password) {
        axios.post(registerURL, {
            email: email, first_name: first_name,
            last_name: last_name, password: password
        }).then(() => {
            this.login(email, password);
        }).catch(error => {
            console.log(error);
            this.text = 'Bad email or password';
        });
    }

    login(email, password) {
        localStorage.setItem("email", email);
        localStorage.setItem("password", password);
        axios.post(tokenURL, {email: email, password: password}).then(response => {
            localStorage.setItem("accessToken", response.data.access);
            localStorage.setItem("refreshToken", response.data.refresh);
            this.$router.push('/students');
        }).catch(error => {
            console.log(error);
        });
    }

    // static async refreshToken() {
    //     axios.post(refreshURL, {refresh: localStorage.getItem("refreshToken")}).then(response => {
    //         localStorage.setItem("accessToken", response.data.access);
    //     }).catch(error => {
    //         console.log(error);
    //     });
    // }

    static async refreshToken() {
        console.log("refresh\n");
        return axios.post(refreshURL, {refresh: localStorage.getItem("refreshToken")}).then(response => {
            localStorage.setItem("accessToken", response.data.access);
        });
    }

    // static async refreshToken() {
    //     try {
    //         const response =  await axios.post(refreshURL, {refresh: localStorage.getItem("refreshToken")});
    //         localStorage.setItem("accessToken", response.data.access);
    //         return response;
    //     }catch (error) {
    //         console.error(error);
    //         return error;
    //     }
    // }

    static invalidateAccessToken() {
        localStorage.setItem("accessToken", null);
    }


    //TODO:
    //add protection from recursion

    static async sendGet(url) {
        return new Promise((resolve, reject) => {
            axios.get(url, {
                headers: {Authorization: `Bearer ${localStorage.getItem("accessToken")}`}
            }).then(
                async response => {
                    resolve(response)
                },
                async e => {
                    if ((((Error)(e)).message).localeCompare("Error: Request failed with status code 401\n")) {
                        return this.refreshToken().then(async () => this.sendGet(url))
                    } else {
                        reject(e)
                    }
                }
            );
            }
        );
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