<template>
  <div class="hello">
    <h1>This is the chart interface</h1>

    
    <line-chart :data="chartData"></line-chart>
    <pie-chart :data="[['Blueberry', 44], ['Strawberry', 23],['Nokia', 150],['Samsung', 120]]"></pie-chart>
    <column-chart :data="[['Sun', 32], ['Mon', 46], ['Tue', 28]]"></column-chart>
    <bar-chart :data="[['X-Small', 5], ['Small', 27]]"></bar-chart>
  </div>

</template>

<script>
import axios from 'axios'

export default {
  name: 'Chart',
  data() {
      return {
          chartData : {
              "2017-05-13":2,
              "2017-06-13":5,
              "2017-10-13":7
          }
      }
  }
  
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
