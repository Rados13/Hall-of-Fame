<template>
    <div>
        <div class='item-list' v-for="(item,key) in stats" :key="key">
            <p>
                {{key}}: {{item}}
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