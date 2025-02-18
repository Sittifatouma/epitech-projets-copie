<template>
  <div class="top_crypto">
      <h1>Top Crypto</h1>
      <div class="crypto_content">
          <div v-for="crypto in cryptos" :key="crypto.id" class="crypto">
                <div class="crypto_info">
                    <h3 class="name">{{crypto.name}}</h3>
                    <div class="variation" v-bind:style= "[crypto.variation_direction ? {color : 'green'} : {color: 'red'}]">{{crypto.variation_pourcentage}}</div>
                    <Icon icon="ant-design:up-circle-outlined" color="green" v-if="crypto.variation_direction" class="up_down"/>
                    <Icon icon="ant-design:down-circle-outlined" color="red" v-if="!crypto.variation_direction" class="up_down"/>
                </div>
          </div>
      </div>
      
  </div>
</template>

<script>
import { Icon } from '@iconify/vue2';

export default {
    components: {
        Icon,
    },
    data: function () {
    return {
      cryptos: [
        {id:1, name:'Bitcoin', variation_pourcentage: '+ 1.5%', variation_direction: true},
        {id:2, name:'BNB' , variation_pourcentage: '- 1.5%', variation_direction: false},
        {id:3, name:'Bitcoin', variation_pourcentage: '+ 1.5%', variation_direction: true},
        {id:4, name:'Bitcoin', variation_pourcentage: '+ 1.5%', variation_direction: true},
        {id:5, name:'Bitcoin', variation_pourcentage: '+ 1.5%', variation_direction: true},
      ]
    }
  },
}
</script>

<style scoped>

.top_crypto {
    width: 100%;
}

.top_crypto h1 {
    margin-bottom: 35px;
}

.top_crypto .crypto_content {
    display: flex;
    gap: 50px;
    width: 100%;
    overflow-x: scroll;
}

.wrapper {
    padding: 20px;
}

.top_crypto .crypto_content .crypto {
    display: flex;
    flex: 0 0 auto;
    justify-content: center;
    flex-direction: column;
    height: 100px;
    width: 300px;
    padding: 10px;
}

.top_crypto .crypto_content .crypto .crypto_info {
    display: flex; 
    justify-content: space-between;
    align-items: center;
    border-radius: 5px;
    box-shadow: 0px 2px 15px 5px #ebebeb;
    height: 100%;
    width: 100%;
    padding: 20px;
}

.top_crypto .crypto_content .crypto .crypto_info h3 {
    margin-right: 10px;
    font-size: 24px;
    font-weight: 300;
}

.top_crypto .crypto_content .crypto .crypto_info .up_down {
    width: 30px;
    height: 30px;
}

</style>