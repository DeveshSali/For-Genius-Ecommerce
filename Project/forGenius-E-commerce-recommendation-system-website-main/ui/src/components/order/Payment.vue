<!--  Payment Page  -->

<template>
  <div class="manage_container">
    <div class="fix">
    <header>
        PAYMENT
    </header>
    <img class="logo" src=../../assets/2.png alt="logo" v-on:click="jumpHome">
    <div class="payment-container">
      <el-select v-model="value" clearable placeholder="Choose payment method" class="choose">
        <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value">
        </el-option>
      </el-select>
    </div>
      <el-button type="brown" class="Pay" @click="submitForm()">Pay</el-button>
   </div>
  </div>
</template>

<script>
import { ord_pay } from '../../api/order'
export default {
  data () {
    return {
      pay_from: {
        token: '',
        order_id: ''
      },
      options: [{
          value: 'paypal',
          label: 'Paypal'
        }, {
          value: 'debit',
          label: 'Debit Card'
        }, {
          value: 'credit',
          label: 'Credit Card'
        }, {
          value: 'gift',
          label: 'Gift Card'
        }],
        value: ''
      }
  },
  created () {
    this.checkStat(),
    this.loadOrder()
  },
  methods: {
    async checkStat () {
        console.log(await this.check());
    },
      check () {
        // Simple Navigation Guards
        if (sessionStorage.getItem("token") != null) {
        } else {
          this.$router.push('/login');
          this.$message.error('You Need to Login First');
      }
    },
    // Get user and order information
    loadOrder() {
      this.pay_from.token = sessionStorage.getItem('token');
      this.pay_from.order_id = sessionStorage.getItem('order');
      this.pay_from.order_id = parseInt(this.pay_from.order_id);
      sessionStorage.removeItem('/order');
    },
    jumpHome () {
      this.$router.push('/home')
    },
    submitForm() {
      // Main operation to pay
      // Payment method caanot be null
      if (this.value != '') {
        ord_pay(this.pay_from).then( res => {
          this.$message({message: 'Payment Done',type: 'success'});
          this.$router.push('/user/order')
        }).catch( error => {
            this.$message.error('Payment Failed');
        })
      } else {
        this.$message.error('You Need to Choose a method First');
      }
      
    }
  },
  
}
</script>


<style lang="less" scoped>
.payment-container {
    position: relative;
    top: 100px;
    left:50%;
    transform: translate(-50%);
    width:500px;
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

.Pay{
    position: relative;
    width:130px;
    font-size: 16px;
    height:40px;
    left:55%;
    top:200px;
    border-radius: 10px;
    background: #786662;
    color: #fefefe;
    padding-left: 19px;
    padding-top: 11px;
    border-color: #786662;
    transform: translate(-50%);
}
.choose{
  position: relative;
  left:50%;
  width:300px;
  transform: translate(-50%);
}
.fix{
    margin:0 auto;
    width:1750px;
}
.title{
    height:100px;
    width:200x;
    margin:0 auto;
    text-align: center;
}
</style>
