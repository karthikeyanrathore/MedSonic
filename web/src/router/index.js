import Vue from 'vue'
import Router from 'vue-router'
import Heart from '@/components/Heart'
import Diabetes from '@/components/Diabetes'
import Pneumonia from '@/components/Pneumonia'

Vue.use(Router)

export default new Router({
  routes: [
    // {
    //   path: '/',
    //   name: 'HelloWorld',
    //   component: HelloWorld
    // },
    {
      path: '/Heart',
      component: Heart
    },
    {
      path: '/Diabetes',
      component: Diabetes
    },
    {
      path: '/Pneumonia',
      component: Pneumonia
    }

  ]
})
