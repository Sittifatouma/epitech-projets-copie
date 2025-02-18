<template>
    <div class="list_crypto_view">
        <h1>{{title}}</h1>
        <div class="title_line">
            <h3>Name</h3>
            <h3>Last Price</h3>
            <h3>Variation</h3>
            <h3>Favorite</h3>
        </div>
        <div  v-for="crypto in cryptos" :key="crypto.id" class="crypto_list">
            <div class="crypto"  @click="fav(crypto.id)" > 
                <p>{{crypto.name}}</p>
                <p>{{crypto.last_price}}</p>
                <p class="variation_pourcentage">{{crypto.variation_pourcentage}}</p>
                <Icon icon="akar-icons:heart" color="black"  class="icon"/>
            </div>
        </div>
    </div>
</template>

<script>
import { Icon } from '@iconify/vue2';
import axios from "axios"
export default {
    
    components: {
        Icon
    },
    props: ['title'],
    data: function () {
    return {
      cryptos: [
        {id:1, name:'Bitcoin', variation_pourcentage: '+ 1.5%', variation_direction: true, last_price:'3241.13$'},
        {id:2, name:'BNB' , variation_pourcentage: '- 1.5%', variation_direction: false, last_price:'3241.13$'},
        {id:3, name:'Bitcoin', variation_pourcentage: '+ 1.5%', variation_direction: true, last_price:'3241.13$'},
        {id:4, name:'Bitcoin', variation_pourcentage: '+ 1.5%', variation_direction: true, last_price:'3241.13$'},
        {id:5, name:'Bitcoin', variation_pourcentage: '+ 1.5%', variation_direction: true, last_price:'3241.13$'},
      ],
      colorFav:"false",
      tab:[]
    }
  },
  methods:{
      fav  : function (id) {
          //alert(localStorage.getItem('id'))
          //alert(id)
            axios.post('http://51.210.40.154:4000/api/fav',
            {
                "user": localStorage.getItem('id'),
                "crypto": id
            })
          .then(function (response) {
            if (response.status === 200) {
              //alert("bien enregistré dans les favoris")
              //self.$router.push({name: "Home"})
            } 
          })
          .catch(function (error) {
              alert("Pensez à vous connecter pour ajouter des élément en favoris"),
            console.log(error.message);
          });
         
         // this.tab.push(id)
          //console.log(this.tab.find(e => e === 20))
          //for (var i = 0; i <this.tab.length; i++){
              //console.log(this.tab[i])
          //}

          //this.colorFav = go
          //if(this.colorFav){
            //  alert("color = true")
          //}
      }
  }
}
</script>

<style scoped>

.list_crypto_view {
    flex: 4;
    display: flex;
    padding: 60px 60px;
    flex-direction: column;
}

.list_crypto_view h1 {
    margin-bottom: 60px;
    font-size: 50px;
}

.list_crypto_view h3,
.list_crypto_view .crypto_list .crypto > *{
    flex: 1;
    font-size: 30px;
    font-weight: 500;
}


.list_crypto_view .title_line {
    display: flex;
    margin-bottom: 20px;
}

 

.list_crypto_view .crypto_list {
    display: flex;
    flex: 1;
    flex-direction: column;
}

.list_crypto_view .crypto_list .crypto {
    display: flex;
    margin: 20px 0;
}

.list_crypto_view .crypto_list .crypto .variation_pourcentage {
    color: green;
}

.list_crypto_view .crypto_list .crypto .icon {
    display: flex;
    width: 30px;
}

</style>