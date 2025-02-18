// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import "bootstrap/dist/css/bootstrap.min.css"
import {Chart} from 'chart.js'
import Chartkick from 'vue-chartkick'
import moment from 'moment'
import VueSession from 'vue-session'



Vue.prototype.moment = moment
Vue.use(Chartkick.use(Chart));
Vue.use(VueSession)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
