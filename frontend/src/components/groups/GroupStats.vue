<template>
    <div>
        <div class='item-list' v-for="(item,key) in stats" :key="key">
            <p>
                {{key}}: {{item.val}}/{{item.max_points}}
            </p>
        </div>
        <p><img v-bind:src='"http://"+link' alt="stats plot" ></p>
    </div>
</template>
<script>

export default {
    name: "GroupStats",
    props: ['stats','link'],
}
</script>

<style scoped>
@import './stylesheet.css';    
</style>