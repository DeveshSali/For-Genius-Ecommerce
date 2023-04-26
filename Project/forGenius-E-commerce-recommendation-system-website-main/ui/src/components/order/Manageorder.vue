<!--  OrderHistory Admin Main Page  -->

<template>
  <div >
    <div class="fix">
    <header>
        ADMIN&nbsp;ORDER&nbsp;HISTORY
    </header>
    <img class="logo" src=../../assets/2.png alt="logo" v-on:click="jumpUser">
  <div class="order_container">
      <Orderad v-for="(obj,ind) in order_list.slice().reverse()" :key="obj.order_id"
      :ordId="obj.order_id"
      :payStat="obj.paid"
      :ordItem="obj.item"
      :ordTotal="obj.total"
      :orderDate ="obj.order_date"
      :name="obj.name"
      :address_line="obj.address_line"
      :phone_number="obj.phone_number"
      :email="obj.email"
      :suburb="obj.suburb"
      :state="obj.state"
      :country="obj.country"
      :post_code="obj.post_code"
      :index = "ind"
      @checker = 'check'
      >
      </Orderad>
  </div>
 </div>
</div>
</template>

<script>
import Orderad from '../mod/OrdAdminCom.vue'
import { admin_ord } from '../../api/admin'
export default {
    data () {
        return {
            order_list : [],
            tokenForm: {},
            total_price: ''
        }
    },created () {
        this.checkStat(),
        this.loadOrd() 
    },
    components: {
        Orderad
    },
    methods: {
        async checkStat () {
            await this.check();
        },
        check () {
            // Simple Navigation Guards
            if (sessionStorage.getItem("adtoken") != null) {
            } else {
                this.$router.push('/login')
            }
        },
        // Load admin view's order history
        async loadOrd() {
            // Main operation to get order history for admin
            admin_ord(this.tokenForm).then( res => {
                console.log(res);
                this.order_list = res.data.order_list;
            }).catch( error => {
                this.$message.error('No order exists');
            })
        },
        // When prder is not paid yet
        // "Fail" will be shown
        // Oterwise will be "Success"
        check(index) {
            if (this.order_list[index].paid == 1) {
                this.order_list[index].paid = "Success";
            } else {
                this.order_list[index].paid = "Fail";
            }
        },
        jumpUser () {
            this.$router.push('/admin');
        },
    }
}
</script>

<style lang="less" scoped>
.fix{
    margin:0 auto;
    width:1750px;
}
header{
    height: 100px;
    width: 100%;
    margin:0 auto;
    left:0;
    top:0;
    z-index: 999;
    border-bottom:3px solid #ccc;
    text-align: center;
    line-height: 130px;
    font-weight:normal;
    font-family: 'segUi';
    font-size: 50px;
    overflow: hidden;
}
.logo{
    height: 230px;
    cursor: pointer;
    margin-top:-170px ;
    z-index:100;
    overflow: hidden;
}
.order_container{
    position: relative;
    left:50%;
    top:-60px;
    transform: translate(-50%);
    width:300px;
}
.title{
    height:100px;
    width:200x;
    margin:0 auto;
    text-align: center;
}
</style>