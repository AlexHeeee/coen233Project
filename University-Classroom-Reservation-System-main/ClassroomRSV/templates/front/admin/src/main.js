import Vue from 'vue'
import App from '@/App.vue'
import ElementUI from 'element-ui'
import '@/assets/css/element-variables.scss'
import '@/assets/css/style.scss'

import router from '@/router/router-static.js';

import BreadCrumbs from '@/components/common/BreadCrumbs'

import echarts from 'echarts'

import 'echarts/theme/macarons.js'

import http from '@/utils/http.js'

import base from '@/utils/base'

import { isAuth, getCurDate, getCurDateTime } from '@/utils/utils'

import Editor from "@/components/common/Editor";

import api from '@/utils/api'


Vue.prototype.$http = http
Vue.prototype.$echarts = echarts
Vue.prototype.$base = base.get()
Vue.prototype.$project = base.getProjectName()
Vue.prototype.$api = api

Vue.prototype.isAuth = isAuth
Vue.prototype.getCurDateTime = getCurDateTime
Vue.prototype.getCurDate = getCurDate

Vue.use(ElementUI, { size: 'medium', zIndex: 3000 });
Vue.config.productionTip = false

Vue.component('bread-crumbs', BreadCrumbs)

Vue.component('editor', Editor)

new Vue({
  render: h => h(App),
  router
}).$mount('#app')
