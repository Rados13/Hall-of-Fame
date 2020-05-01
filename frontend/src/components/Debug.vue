<template>
    <div id='app'>
    <ul> <p v-on:click="invalidateAccessToken">invalidate</p> </ul>
    <ul> <p v-on:click="refreshToken">refresh</p> </ul>
    </div>
</template>

<script>

import Entry from "../services/Entry";

export default {
    name: 'DebugApp',
    components:{
    },
    methods:{
        invalidateAccessToken: function() {
            Entry.invalidateAccessToken();
        },
        refreshToken: function() {
            Entry.refreshToken();
        }
    }
}
</script>

<style scoped>
    * {
        display: flex;
        margin: 0 10px 0 0;
        padding: 0;
        list-style: none;
        justify-content: flex-start;
        flex-wrap: wrap;
    }
</style>

