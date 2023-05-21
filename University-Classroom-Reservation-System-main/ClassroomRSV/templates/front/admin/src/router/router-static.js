import Vue from 'vue';
import VueRouter from 'vue-router'
Vue.use(VueRouter);

import Index from '@/views/index'
import Home from '@/views/home'
import Login from '@/views/login'
import NotFound from '@/views/404'
import UpdatePassword from '@/views/update-password'
import register from '@/views/register'
import center from '@/views/center'
    import xueshengquxiaoyuyue from '@/views/modules/xueshengquxiaoyuyue/list'
    import jiaoshixinxi from '@/views/modules/jiaoshixinxi/list'
    import xuesheng from '@/views/modules/xuesheng/list'
    import xueshengshenqing from '@/views/modules/xueshengshenqing/list'


const routes = [{
    path: '/index',
    name: 'Front Page',
    component: Index,
    children: [{

      path: '/',
      name: 'Front Page',
      component: Home,
      meta: {icon:'', title:'center'}
    }, {
      path: '/updatePassword',
      name: 'update password',
      component: UpdatePassword,
      meta: {icon:'', title:'updatePassword'}
    }, {
      path: '/center',
      name: 'personal information',
      component: center,
      meta: {icon:'', title:'center'}
    }
      ,{
	path: '/xueshengquxiaoyuyue',
        name: 'student cancel',
        component: xueshengquxiaoyuyue
      }
      ,{
	path: '/xuesheng',
        name: 'student',
        component: xuesheng
      }
      ,{
	path: '/xueshengshenqing',
        name: 'student application',
        component: xueshengshenqing
      }
    ]
  },
  {
    path: '/login',
    name: 'login',
    component: Login,
    meta: {icon:'', title:'login'}
  },
  {
    path: '/register',
    name: 'register',
    component: register,
    meta: {icon:'', title:'register'}
  },
  {
    path: '/',
    name: 'Front Page',
    redirect: '/index'
  },
  {
    path: '*',
    component: NotFound
  }
]

const router = new VueRouter({
  mode: 'hash',
  routes
})

export default router;
