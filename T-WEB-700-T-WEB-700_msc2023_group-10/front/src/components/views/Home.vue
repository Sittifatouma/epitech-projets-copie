<template>
    <div class="home">
        <Navigation class="nav"/>
        <div class="main_content">
            <SearchBar/>
            <TopCrypto/>
            <ArticleBox title="Recent Article"/>
            
        </div>
    </div>
</template>

<script>
import Navigation from '../box/Navigation'
import SearchBar from '../box/SearchBar'
import ArticleBox from '../box/ArticleBox'
import TopCrypto from '../box/TopCrypto'

export default {
    components: {
        Navigation,
        SearchBar,
        ArticleBox,
        TopCrypto
    },
}
</script>

<style scoped>

.home {
    width: 100%;
    height: 100%;
    display: flex;
    overflow: hidden;
}

.home .main_content {
    flex: 4;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    padding: 40px;
    overflow: hidden;
}


</style>