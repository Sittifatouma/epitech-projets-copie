import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import User from '@/components/User'
//import Postuser from '@/components/Postuser'
import Chart from '@/components/Chart'
//import Viewuser from '@/components/Viewuser'
import WorkingTimes from '@/components/WorkingTimes'
import ClockManager from '@/components/ClockManager'
import PointForHim from '@/components/PointForHim'
//import Profile from '@/components/Profile'
import Register from '@/components/Register'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/Register',
      name: 'Register',
      component: Register
    },
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/User',
      name: 'User',
      component: User
    }
    ,
    {
      path: '/Chart',
      name: 'Chart',
      component: Chart
    }
    ,
   
    {
      path: '/WorkingTimes/:id/:name/:mail',
      name: 'WorkingTimes',
      component: WorkingTimes
    },
    {
      path: '/ClockManager/:id',
      name: 'ClockManager',
      component: ClockManager
    },
    {
      path: '/PointForHim/:id/:name/:mail',
      name: 'PointForHim',
      component: PointForHim
    },
   
    
  ]
})
