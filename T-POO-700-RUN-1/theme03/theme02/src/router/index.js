import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import User from '@/components/User'
import Postuser from '@/components/Postuser'
import Chart from '@/components/Chart'
import Viewuser from '@/components/Viewuser'
import WorkingTimes from '@/components/WorkingTimes'
import ClockManager from '@/components/ClockManager'
import Logout from '@/components/Logout'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/User',
      name: 'User',
      component: User
    },
    {
      path: '/Postuser/:name',
      name: 'Postuser',
      component: Postuser
    }
    ,
    {
      path: '/Chart',
      name: 'Chart',
      component: Chart
    }
    ,
    {
      path: '/Viewuser',
      name: 'Viewuser',
      component: Viewuser
    },
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
      path: '/Logout',
      name: 'Logout',
      component: Logout
    }
  ]
})
