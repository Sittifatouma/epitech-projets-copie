import Vue from 'vue'
import VueRouter from 'vue-router'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import VueSession from 'vue-session'
import VueLocalStorage from 'vue-localstorage'

import App from './App.vue'

import Home from './components/views/Home'
import Favorite from './components/views/Favorite'
import List from './components/views/List'
import Signin from './components/views/Signin'  
import Signup from './components/views/Signup'

import GAuth from 'vue-google-oauth2'
const gauthOption = {
  clientId: '851128142395-1m3miol992fnpfrmpvk1fgnvf8rid8ai.apps.googleusercontent.com',
  scope: 'profile email',
  prompt: 'consent',
  fetch_basic_profile:true
}
Vue.use(GAuth, gauthOption)

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(VueRouter)
Vue.use(VueSession)

Vue.use(VueLocalStorage)
// Or you can specify any other name and use it via this.$ls, this.$whatEverYouWant
Vue.use(VueLocalStorage, {
  name: 'ls',
  bind: true //created computed members from your variable declarations
})

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/Home',
    name: 'Home',
    component: Home
  },
  {
    path: '/Favorite',
    name: 'Favorite',
    component: Favorite
  },
  {
    path: '/List',
    name: 'List',
    component: List
  },
  {
    path: '/Signin',
    name: 'Signin',
    component: Signin
  },
  {
    path: '/Signup',
    name: 'Signup',
    component: Signup
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
