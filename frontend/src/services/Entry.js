import axios from 'axios';

const registerURL = 'http://127.0.0.1:8000/api/users/';
const userInfoURL = 'http://127.0.0.1:8000/api/users/info';
const tokenURL = 'http://127.0.0.1:8000/api/token';
const refreshURL = 'http://127.0.0.1:8000/api/token/refresh';


export default class Entry {
    $router = null;

    constructor(router) {
        this.$router = router;
    }

    async register(email, first_name, last_name, password) {
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

    async login(email, password) {
        await axios.post(tokenURL, {email: email, password: password}).then(response => {
            localStorage.setItem("accessToken", response.data.access);
            localStorage.setItem("refreshToken", response.data.refresh);
            this.$router.push('/studentsGroups');
        }).catch(error => {
            console.log(error);
        });
    }

    static async getUserInfo() {
        let x = await axios.get(userInfoURL, {
            headers: {Authorization: `Bearer ${localStorage.getItem("accessToken")}`}
        }).then(data => {
            return data.data;
        }).catch(error => console.log(error));
        console.log(x);
        return x
    }

    static async refreshToken() {
        return axios.post(refreshURL, {refresh: localStorage.getItem("refreshToken")}).then(response => {
            localStorage.setItem("accessToken", response.data.access);
        });
    }

    static invalidateAccessToken() {
        localStorage.setItem("accessToken", null);
    }

    static async getUsers() {
        return await axios.get(registerURL, {
            headers: {Authorization: `Bearer ${localStorage.getItem("accessToken")}`}
        }).then(response => {

            return response.data;
        }).catch(e => {
            console.error(e);
        });
    }

    static async getUser(firstName, lastName) {
        var users;
        await this.getUsers().then(data => users = data);
        users = users.filter(user => (user.first_name === firstName && user.last_name === lastName));
        if (users.length > 0) {
            users = users[0];
            delete users['password'];
            delete users['email'];
        } else {
            users = null
        }
        return users;
    }
}