<template>
    <div class="listFavoris">
        <h1>{{title}}</h1>
        
        <div class="favoris">
            <p>BNB</p>
            <img src="../../assets/lion.png" width="50">
            <p style="color: green;">+1,34</p>
            <p>3672$</p>
            <p>&star;</p>
        </div>
    </div>
    
</template>
<script>
//import { defineComponent } from '@vue/composition-api'


export default {
    props: ['title']
}
</script>
<style scoped>
    .favoris{
        border-radius: 5px; 
        background: #f6f6f6; 
        height: 80px; 
        box-shadow: 0 .125rem .25rem rgba(0,0,0,.075); 
        margin: 1rem;
        display: flex; 
        align-items: center; 
        justify-content: space-between; 
        padding: 0 1rem;
    }
    .h1 {
        margin-bottom: 60px;
        font-size: 50px;
        margin-left: 50px;
    }
    .listFavoris{
        max-width:100vmax; 
        width: 80% ; 

    }

</style>