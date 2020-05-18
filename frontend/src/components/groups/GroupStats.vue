<template>
    <div>
        <div class='item-list' v-for="(item,key) in stats" :key="key">
            <p>
                {{key}}: {{item.val}}/{{item.max_points}}
            </p>
        </div>
    </div>
</template>
<script>

export default {
    name: "GroupStats",
    props: ['stats'],
}
</script>

<style scoped>
@import './stylesheet.css';    
</style>