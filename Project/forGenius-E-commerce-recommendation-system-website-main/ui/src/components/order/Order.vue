<!--  Order Main Page  -->

<template>
  <div >
    <div class="fix">
    <header>
        ORDER&nbsp;
    </header>
    <img class="logo" src=../../assets/2.png alt="logo">
    <el-button @click="jumpCart" class='return' type="brown">Return Cart</el-button>
    <div class="order_contain">
    <h2>Address</h2>
      <div v-show="isEmpty">
          <p> <span>Recipient's Name:</span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{create_form.name}} </p> 
          <p> <span>Phone Number:</span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{create_form.phone_number}}</p>
          <p> <span>Address:</span> </p>
          <p> {{create_form.address_line}}</p>
          <el-button type="white" @click="chooseDialogFormVisible = true" align="left" style="float:left">Choose</el-button>
          <el-dialog title="Address Book" :visible.sync="chooseDialogFormVisible" width="40%" class="editf" append-to-body>
            <div v-for="(item,ind) in addressbook" :key="ind">
                    <div class="block1"></div>
                    <p> Recipient's name: {{item.name}} </p> 
                    <p> Address: </p>
                    <p> {{item.address_line}}</p>
                    <p> Country: {{item.country}}</p>
                    <p> State: {{item.state}}</p>
                    <p> Suburb: {{item.suburb}}</p>
                    <p> Postal Code:{{item.post_code}}</p>
                    <p> Phone Number: {{item.phone_number}} </p> 
                    <el-button type="white" @click="chooseAdd(ind)" class="choose_in">Choose</el-button>
                    <div class="block"></div>
                    <div class="line-in"></div>
              </div>
            <div slot="footer" class="dialog-footer">
              <el-button type="white" @click="chooseDialogFormVisible = false">Cancel</el-button>
            </div>
          </el-dialog>
      </div>
      <el-button type="white" @click="jumpAdd" align="right">Add</el-button>
      <div class="cart-container">
        <h2 class="infor">Product information</h2>
        <Product v-for="(obj,ind) in cart" :key="obj.id"
        :proName="obj.name"
        :proPrice="obj.price"
        :qua="obj.quantity"
        :proId="obj.product_id"
        :proPic="obj.picture"
        :index = "ind"
        @addQua = 'add'
        @subQua = 'sub'
        @delPro = 'del'>
        </Product>
        <div class="price">
        <p>Total Price: </p>
        <p>$ &nbsp;{{total_price}}</p>
        </div>
      </div>
    </div>
    <el-button type="brown" @click="jumpPay" class="submit">Submit Order</el-button>
  </div>
  </div>
</template>

<script>
// After submit cart
// Without user login, this page cannot be reached
import { address_view } from '../../api/user'
import { cart_view } from '../../api/order'
import Product from '../mod/CartPro.vue'
import { cart_qua } from '../../api/order'
import { cart_del } from '../../api/order'
import { cart_create } from '../../api/order'
export default {
    inject:['reload'],
    data () {
        // The rules for input value
        var checkEmail = (rule, value, callback) => {
        const mailReg = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+.com/
        if (!value) {
            return callback(new Error('email address cannot be empty'))
        }
        setTimeout(() => {
            if (mailReg.test(value)) {
            callback()
            } else {
            callback(new Error('Please enter the correct email format'))
            }
        }, 100)
        }
        return {
            cart : [],
            addressbook : [],
            tokenForm: {
                token: ''
            },
            create_form: {
                token: '',
                name: '',
                address_line: '',
                phone_number: '',
                post_code: '',
                suburb: '',
                state: '',
                country: ''
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
            chooseDialogFormVisible: false,
            isEmpty: true,
            share_form: {
                token: '',
                email: ''
            },
            share_formRules:{
               email: [
                    { validator: checkEmail, trigger: 'blur' }
                ]
            }
        }
    },
    components: {
        Product
    },
    created () {
        this.checkStat(),
        this.loadCart(),
        this.loadAddressBook()
    },
    methods: {
        async checkStat () {
            await this.check();
        },
        check () {
            // Simple Navigation Guards
            if (sessionStorage.getItem("token") != null) {
            } else {
            this.$router.push('/login')
            }
        },
        // Load products in cart
        async loadCart() {
            this.tokenForm.token = sessionStorage.getItem('token');
            // Main operation to get cart
            cart_view(this.tokenForm).then( res => {
                this.cart = res.data.data.cart;
                this.total_price = res.data.data.total;
                this.qua_form.token = sessionStorage.getItem('token');
                this.del_form.token = sessionStorage.getItem('token');
                this.create_form.token = sessionStorage.getItem('token');
            }).catch( error => {
                this.$message.error('You Need to Login First');
            })
        },
        // Load address
        async loadAddressBook() {
            // Main operation to get address
            address_view(this.tokenForm).then( res => {
                // if address book is not empty
                if (res.data.data.address_book.length > 0) {
                    this.isEmpty = true;
                    // load result data into this window data 
                    this.addressbook = res.data.data.address_book;
                    this.addressbook = this.addressbook.slice().reverse();
                    this.create_form.name = this.addressbook[0].name;
                    this.create_form.address_line = this.addressbook[0].address_line;
                    this.create_form.phone_number = this.addressbook[0].phone_number;
                    this.create_form.post_code = this.addressbook[0].post_code;
                    this.create_form.suburb = this.addressbook[0].suburb;
                    this.create_form.state = this.addressbook[0].state;
                    this.create_form.country = this.addressbook[0].country;
                } else {
                    // if address book is empty
                    this.isEmpty = false;
                }
            }).catch( error => {
            })
        },
        // quantity + 1 for corresponding product
        add(index) {
            // Operation to quantity + 1 in frontend
            this.cart[index].quantity += 1;
            this.total_price = parseFloat(this.total_price);
            this.cart[index].price = parseFloat(this.cart[index].price);
            this.total_price = this.total_price + this.cart[index].price;
            this.total_price = this.total_price.toFixed(2)
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
            this.total_price = this.total_price.toFixed(2)
            this.qua_form.quantity = this.cart[index].quantity;
            this.qua_form.product_id = this.cart[index].product_id;
            // Operation to quantity - 1 in backend
            cart_qua(this.qua_form).then( res => {
            }).catch( error => {
                this.$message.error('Failed to sub quantity');
            })
        },
        del(index) {
            // Operation to delete product in frontend
            this.total_price = parseFloat(this.total_price);
            this.cart[index].price = parseFloat(this.cart[index].price);
            this.del_form.product_id = this.cart[index].product_id;
            // Operation to delete product in backend
            cart_del(this.del_form).then( res => {
            }).catch( error => {
                this.$message.error('Failed to Delete');
            })
            // Recal the total price
            this.total_price = this.total_price - (this.cart[index].quantity * this.cart[index].price)
            this.total_price = this.total_price.toFixed(2);
            // Delete the product in frontend
            this.cart.splice(index, 1);
        },
        // Choose address from address book
        chooseAdd(index) {
            this.create_form.name = this.addressbook[index].name;
            this.create_form.address_line = this.addressbook[index].address_line;
            this.create_form.phone_number = this.addressbook[index].phone_number;
            this.chooseDialogFormVisible = false;
        },
        jumpCart () {
            this.$router.push('/cart');
        },
        // Create order
        jumpPay () {
            // Main operation to create order
            cart_create(this.create_form).then( res => {
                this.$message({message: 'Order Placed',type: 'success'});
                sessionStorage.setItem('order', res.data.order_id);
                this.$router.push('/payment');
            }).catch( error => {
                this.$message.error('Create Order Failed');
            })
        },
        // When address book is empty
        // Move to add address page
        jumpAdd () {
            sessionStorage.setItem('from', 1);
            this.$router.push('/addressadd');
        }
    }  
}
</script>

<style lang="less" scoped>
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
    margin-top:-170px ;
    z-index:100;
    overflow: hidden;
}
.order_contain{
    position: relative;
    left:53%;
    top:-40px;
    transform: translate(-50%);
    width:500px;
    word-break:break-all;
}
.share_form{
    width:300px;
}
.return{
    height: 43px;
    margin-top:-63px;
    float:right;
    border-radius: 4px;
    padding: 2px 20px;
    background: #786662;
    border-radius: 10px;
    color: #fefefe;
    border-color:#786662;
    cursor: pointer;

}
.submit{
    position: relative;
    left:53%;
    top:-20px;
    width:130px;
    font-size: 16px;
    height:40px;
    margin-top: 50px;
    margin-left: 80px;
    border-radius: 10px;
    background: #786662;
    color: #fefefe;
    padding-left: 19px;
    padding-top: 11px;
    border-color: #786662;
}
.cart-container{
    position: relative;
    left:43%;
    transform: translate(-50%);
    width:500px;
}
.price{
    position: relative;
    left: 75%;
}
.infor{
    position: relative;
    left: 30px;
}
.email_change{
    position: relative;
    width:500px;
}
.email_change /deep/ .el-form-item__label{
    font-family: 'segUi';
    position: relative;
    letter-spacing:.1em;
    top:2px;
    font-size: 18px;
}

.line-in {
    position: relative;
    width: 100%;
    height: 1px;
    border-top: solid #0b0b0f 1px;
}
.block {
    height: 20px;
}
.block1 {
    height: 10px;
}
.choose_in{
    position: relative;
    left:80%;
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
span{
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size:17px;
}
p{
    font-family: 'segUi';
    word-break: keep-all;
}
</style>

