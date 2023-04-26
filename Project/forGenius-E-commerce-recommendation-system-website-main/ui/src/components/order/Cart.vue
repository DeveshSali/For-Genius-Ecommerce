<!--  Cart Main Page  -->

<template>
  <div class="cart_container">
    <div class="fix">
    <header>
        MY&nbsp;CART
    </header>
    <img class="logo" src=../../assets/2.png alt="logo" v-on:click="jumpHome">
    <div class="cart-container">
        <Product v-for="(obj,ind) in cart" :key="ind"
        :proName="obj.name"
        :proPrice="obj.price"
        :qua="obj.quantity"
        :proPic="obj.picture"
        :proId="obj.product_id"
        :index = "ind"
        @addQua = 'add'
        @subQua = 'sub'
        @delPro = 'del'>
        </Product>
        <p>&nbsp;&nbsp;Total Price: </p>
        <p>&nbsp;&nbsp;${{total_price}}</p>
        <el-button type="brown" class="checkout" @click="submitForm()" icon="el-icon-check">Check Out</el-button>
    </div>
  </div>
  </div>
</template>

<script>
// Without user login, this page cannot be reached
import Product from '../mod/CartPro.vue'
import { cart_view } from '../../api/order'
import { cart_qua } from '../../api/order'
import { cart_del } from '../../api/order'


export default {
    data () {
        return {
            cart : [],
            tokenForm: {
                token: ''
            },
            total_price: '',
            qua_form: {
                token: '',
                product_id: '',
                quantity: ''
            },
            del_form: {
                token: '',
                product_id: ''
            },
            
        }
    },
    created () {
        this.checkStat(),
        this.loadCart()
    },
    components: {
        Product
    },
    methods: {
        async checkStat () {
            console.log(await this.check());
        },
        check () {
            // Simple Navigation Guards
            if (sessionStorage.getItem("token") != null) {
            } else {
            this.$router.push('/login')
            }
        },
        // Load all cart products
        async loadCart() {
            this.tokenForm.token = sessionStorage.getItem('token');
            // Main operation to get cart
            cart_view(this.tokenForm).then( res => {
                this.cart = res.data.data.cart;
                this.cart = this.cart.slice().reverse();
                this.total_price = res.data.data.total;
                this.qua_form.token = sessionStorage.getItem('token');
                this.del_form.token = sessionStorage.getItem('token');
            }).catch( error => {
                this.$message.error('You Need to Login First');
            })
        },
        // Submmit the cart
        submitForm() {
            // Make sure cart is not empty
            if (this.cart.length > 0) {
                this.$router.push('order');
            } else {
                this.$message.error('The cart is empty');
            }
        },
        // quantity + 1 for corresponding product
        add(index) {
            // Operation to quantity + 1 in frontend
            this.cart[index].quantity += 1;
            this.total_price = parseFloat(this.total_price);
            this.cart[index].price = parseFloat(this.cart[index].price);
            this.total_price = this.total_price + this.cart[index].price;
            this.total_price = this.total_price.toFixed(2);
            this.qua_form.quantity = this.cart[index].quantity;
            this.qua_form.product_id = this.cart[index].product_id
            // Operation to quantity + 1 in backend
            cart_qua(this.qua_form).then( res => {
            }).catch( error => {
                this.$message.error('Failed to add quantity');
            })
        },
        // quantity - 1 for corresponding product
        sub(index) {
            // Operation to quantity - 1 in frontend
            this.total_price = parseFloat(this.total_price);
            this.cart[index].price = parseFloat(this.cart[index].price);
            this.cart[index].quantity > 1 && (this.cart[index].quantity -= 1) && (this.total_price = this.total_price - this.cart[index].price);
            this.total_price = this.total_price.toFixed(2);
            this.qua_form.quantity = this.cart[index].quantity;
            this.qua_form.product_id = this.cart[index].product_id;
            // Operation to quantity - 1 in backend
            cart_qua(this.qua_form).then( res => {
            }).catch( error => {
                this.$message.error('Failed to sub quantity');
            })
        },
        // delete corresponding product
        del(index) {
            // Operation to delete product in frontend
            this.total_price = parseFloat(this.total_price);
            this.cart[index].price = parseFloat(this.cart[index].price);
            this.del_form.product_id = this.cart[index].product_id;
            // Operation to delete product in backend
            cart_del(this.del_form).then( res => {
            }).catch( error => {
                this.$message.error('Failed to delete');
            })
            // Recal the total price
            this.total_price = this.total_price - (this.cart[index].quantity * this.cart[index].price)
            this.total_price = this.total_price.toFixed(2);
            // Delete the product in frontend
            this.cart.splice(index, 1);
        },
        jumpHome () {
            this.$router.push('Home');
        }

    }
}
</script>


<style lang="less" scoped>
.cart-container {
    position: relative;
    left:50%;
    top:-40px;
    transform: translate(-50%);
    width:500px;
}

.cart_container{
    background-color: #d1dbda;
    height: 100%;
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
.checkout{
    position: relative;
    top:20px;
    left:83%;
    width: 130px;
    background: #786662;
    border-radius: 10px;
    color: #fefefe;
    letter-spacing:2px;
    padding-left: 10px;
    border-color: #786662;
    z-index: 200;
}
.title{
    height:100px;
    width:200x;
    margin:0 auto;
    text-align: center;
}
.fix{
    margin:0 auto;
    width:1750px;
}
p{
    letter-spacing: 1.5px;
    word-break: keep-all;
}
</style>