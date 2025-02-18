<template>
    <div class="favorite_page">
        <Navigation/>
        <ListFavoris title="Your favorite are here"/>
    </div>
    
</template>

<script>
import Navigation from '../box/Navigation'
import ListFavoris from '../box/ListFavoris'
//import axios from 'axios'

export default {
    components: {
        Navigation,
        ListFavoris
    }
}
</script>

<style scoped>

.favorite_page {
    display: flex;
    width: 100%;
    height: 100%;
}

</style>