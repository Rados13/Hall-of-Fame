<template>
    <div class='item-list'>
        <form action='#' @submit.prevent = "sendMail()">
            <button @click="selectAll" class="button">{{btnText}}</button>
            <div class="item-list" v-bind:key="user.pk" v-for="user in usersList">
                <p>{{user.first_name}}   {{user.last_name}} 
                    <input type='checkbox' value="users[user.pk]" v-model='users[user.id]'/>
                </p>
            </div>
            <input type='text' value="title" v-model='title'/>
            <textarea rows="10" cols="100" v-bind:text=text v-model=text></textarea>
            <p><input class='button' type='submit' value='Send mail' ></p>
        </form>
            
    </div>
</template>
<script>

import MailSender from '../../services/Mail.js';

export default {
    name: "MailForm",
    props: ['usersList'],
        data(){
        return {
            users: {},
            title:"Mail title",
            text:"",
            btnText:"Select all",
        }
    },
    created(){
        for(const elem of this.usersList){
            this.users[elem.id] = false;
        }
    },
    methods:{
        sendMail(){
            MailSender.sendMail(this.users,this.title,this.text);
            this.$emit('sended');
        },
        selectAll(){
            var newValue = this.btnText==="Select all"?true:false;
            for(var elem in this.users){
                this.users[elem]=newValue;
            }
            this.btnText = (this.btnText=="Select all")?"Discard all":"Select all";
        }
    }
}
</script>

<style scoped>
@import './stylesheet.css';    
</style>