import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../components/user/Login.vue'
import Signup from '../components/user/Signup.vue'
import Home from '../components/Home.vue'
import Userprofile from '../components/user/Userprofile.vue'
import Resetpassword from '../components/user/Resetpassword.vue'
import Forgotpassword from '../components/user/Forgotpassword.vue'
import ResetpasswordForgot from '../components/user/Resetpassword_forgot.vue'
import Interest from '../components/user/Interest.vue'
import Product from '../components/Productmanagement/Product.vue'
import AddressBook from '../components/address/AddressBook.vue'
import AddressAdd from '../components/address/AddressAdd.vue'
import Cart from '../components/order/Cart.vue'
import AdminPage from '../components/user/AdminPage'
import Addproduct from '../components/Productmanagement/Productadd'
import Manageproduct from '../components/Productmanagement/Manageproduct'
import Manageorder from '../components/order/Manageorder'
import OrderHistory from '../components/order/OrderHistory'
import Order from '../components/order/Order'
import Payment from '../components/order/Payment'
import Usernamechange from '../components/user/UsernameChange.vue'
import Search from '../components/Productmanagement/Search.vue'
Vue.use(VueRouter)

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err)
}

const routes = [
  {
    // Default root will be home
    path: '/', redirect: 'home'
  },
  {
    path: '/login',
    component: Login
  },
  {
    path: '/signup',
    component: Signup
  },
  {
    path: '/home',
    component: Home
  },
  {
    path: '/userprofile',
    component: Userprofile
  },
  {
    path: '/resetpassword',
    component: Resetpassword
  },
  {
    path: '/forgotpassword',
    component: Forgotpassword
  },
  {
    path: '/resetpassword/forgot',
    component: ResetpasswordForgot
  },
  {
    path: '/interest',
    component: Interest
  },
  {
    path: '/product',
    component: Product
  }, {
    path: '/address',
    component: AddressBook
  }, {
    path: '/addressadd',
    component: AddressAdd
  },{
    path: '/cart',
    component: Cart
  },{
    path: '/admin',
    component: AdminPage
  },{
    path: '/addproduct',
    component: Addproduct
  },{
    path: '/manageproduct',
    component: Manageproduct
  },{
    path: '/manageorder',
    component: Manageorder
  },{
    path: '/user/order',
    component: OrderHistory
  },{
    path: '/order',
    component: Order
  },{
    path: '/payment',
    component: Payment
  },{
    path: '/usernamechange',
    component: Usernamechange
  }
  ,{
    path: '/search',
    component: Search
  }
]

const router = new VueRouter({
  routes
})

export default router
