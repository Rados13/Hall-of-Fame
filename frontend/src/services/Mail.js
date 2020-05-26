import axios from 'axios';

const mailURL = 'http://127.0.0.1:8000/api/mail/';


export default class MailSender {

    static async sendMail(to,title,message){
        await axios.post(mailURL,{
            headers: {Authorization: `Bearer ${localStorage.getItem("accessToken")}`, 
            to: to, message: message,title: title}}).then(data =>{
                console.log(data);
            }).catch(error => console.log(error));
    }
}