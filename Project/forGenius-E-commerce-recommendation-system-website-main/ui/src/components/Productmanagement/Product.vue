<!--  Product Detail Page  -->

<template>
    <div class="fix">
    <header>
        PRODUCT&nbsp;DETAIL
    </header>
    <img class="logo" src=../../assets/2.png alt="logo" v-on:click="jumpHome">
    <main>
    <div class="product_box">
        <div class="img" v-for="fit in fits" :key="fit">
          <span class="demonstration">{{ fit }}</span>
          <el-image
            style="width: 550px; height: 550px"
            :src="product.picture"
            :fit="fit"><div slot="error" > <div slot="placeholder" style="background:rgb(243, 243, 243);height:550px">
        <div style="background:rgb(243, 243, 243);height:550px"><div style="padding-top:45%; padding-left:45%; ">Failed</div></div>
      </div></div></el-image>
        </div>
        <div class="inf_box">
        <div class="inf">
        <h2 style=" word-break: keep-all;">{{product.name}}</h2>
        <h3>Warranty: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span> {{product.warranty}} year(s)</span></h3>
        <h3>Delivery date: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span>{{product.delivery_date}}</span></h3>
        <p class="price">$ {{product.price}}</p>
        <h3>Feature: 
          <el-button class="feature" v-for="feature in features" :key="feature" @click='searchFe(feature)' type="white">
          {{feature}}
          </el-button>
        </h3>
        <el-form :model="numberValidateForm" ref="numberValidateForm" label-width="100px" class="demo-ruleForm">
          <el-form-item
            label="Quantity"
            prop="quantity"
            :rules="[
            { required: true, message: 'Quantity cannot be null'},
            { type: 'number', min: 1, message: 'Quantity need to be number and larger than 0'},
            ]"
          >
          <el-button class="el-icon-remove-outline" @click='deleteOne' circle type="white"></el-button>
          <el-input class="quaBox" type="quantity" v-model.number="numberValidateForm.quantity" autocomplete="off"></el-input>
          <el-button class="el-icon-circle-plus-outline" @click='addOne' circle type="white"></el-button>
          </el-form-item>
            <el-button icon="el-icon-s-goods" class="addcart" @click="submitForm('numberValidateForm')" type="black">Add Cart</el-button>
            <el-button icon="el-icon-refresh-right" class="reset" @click="resetForm('numberValidateForm')" type="white">Reset </el-button>
        </el-form>
      </div>
    </div>
       <div class="block"></div>
        <div class="description">
      <h2>Description</h2>
      <p>{{product.description}}</p></div>
    </div>
    
    </main>
    <div class="block"></div>

    <div class="line"></div>
    <footer>
 <div class="recommendation_container">
          <div>
            <div class="tittle_container">
              <div class="tittle2">
              <p>RECOMMENDATION</p>
              </div>
            </div>
            <div class="product_container">
              <Home v-for="(obj,ind) in products" :key="obj.product_id"
              :proName="obj.name"
              :proDescription="obj.description"
              :proPrice="obj.price"
              :proPic="obj.picture"
              :proId="obj.product_id"
              :index="ind"
              > </Home>
            </div>
            <div class="blockk">
            </div>
          </div>
        </div>
    </footer>
   </div>
   
</template>

<script>
import Home from '.././mod/PruCom.vue'
import { cart_add } from '../../api/order'
import { product_view } from '../../api/product'
import { rec_guest } from '../../api/product'
import { rec_user } from '../../api/product'
export default {
     components: {
        Home
    },
    data () {
        return {
            tokenForm: {
              token: ''
            },
            fits: [''],
            product: {},
            numberValidateForm: {
              token: '',
              product_id:'',
              quantity: 1
            },
            product_id_form:{
              product_id: 1
            },
            features: [],
            products: []
        }
    },
    created () {
        this.loadProduct(),
        this.loadRec()
    },
    methods: {
      // Load product
      async loadProduct () {
          // Get target product id from sessionStorage
          this.product_id_form.product_id = sessionStorage.getItem('product');
          // Main operation to get prodcut information
          product_view(this.product_id_form).then ( res => {
            this.product = res.data.data;
            this.features = this.product.features.split(" ");
          }).catch( error => {
            console.log(error);
          })
      },
      // Load recommendation product for product page
      async loadRec () {
        // Have user log in
        if (sessionStorage.getItem('token' != null)) {
          this.tokenForm.token = sessionStorage.getItem('token');
          rec_user(this.tokenForm).then ( res => {
            this.products = res.data.products;
            this.products = this.products.slice(0, 3);
          }).catch( error => {
          })
        } 
        // When no user log in
        else {
          rec_guest(this.tokenForm).then ( res => {
            this.products = res.data.products;
            this.products = this.products.slice(0, 3);
          }).catch( error => {
          })
        }
      },
      // Add to cart
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            // Operation only sucess with user login
            if (sessionStorage.getItem('token') != null) {
              this.numberValidateForm.product_id = this.product_id_form.product_id;
              this.numberValidateForm.token = sessionStorage.getItem('token');
              cart_add(this.numberValidateForm).then( res => {
                this.$message({message: 'Added to Cart!',type: 'success'});
                this.$router.push('/cart');
              }).catch( error => {
                this.$message.error('Add to Cart Failed');
              })
            } else {
              // without login, page will redirect to log in page 
              this.$router.push('/login');
              sessionStorage.setItem('fromPro', 1);
            }
          } else {
            // user cannot submit if input did not pass the rules
            return false;
          }
        });
      },
      // reset quantity
      resetForm(formName) {
        this.$refs[formName].resetFields();
      },
      // quantity - 1
      // cannot less than 1
      deleteOne () {
        this.numberValidateForm.quantity > 1 && (this.numberValidateForm.quantity -= 1)
      },
      // quantity + 1
      addOne () {
        this.numberValidateForm.quantity += 1;
      },
      jumpHome () {
        if (sessionStorage.getItem('fromHome') == 1) {
            sessionStorage.removeItem('fromHome');
            this.$router.push('/home');
        }
        else {
          this.$router.push('/search');
        }
      }, 
      // Click feature buttom
      // Search result of feature will be redirect
      searchFe(feature) {
        sessionStorage.setItem('word',feature);
        this.$router.push('/search')
      }
    }
}
</script>

<style lang="less" scoped>
.fix{
    margin:0 auto;
    width:1750px;
}
.picture {
    position: relative;
    height: 200px;
    width: 200px;
}
.el-icon-remove-outline {
  cursor: pointer;
}
.el-icon-circle-plus-outline{
  cursor: pointer;
}
.quaBox {
  margin-left: 20px;
  margin-right:20px;
  width: 260px;
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

.product_box{
    margin-top:-20px;
    width:1500px;
    word-break:break-all;
    margin-left: 25px;
}
.img{
    float:left;
    margin-left:200px;
}
.inf{
    margin:0 auto;
    word-break:break-all;
    width:500px;
    padding-bottom: 30px;
}
.title{
    height:100px;
    width:200x;
    margin:0 auto;
    text-align: center;
}
.feature{
    border-radius: 20px;
}
span{
    font-size: 14px;
    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}
.addcart{
    margin-top:20px;
    position: relative;
    left:10px;
    width:480px;
    letter-spacing: 4px;
    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
    background-color:black;
    color:white
}
.reset{
    position: relative;
    margin-top:10px;
    width:480px;
    letter-spacing: 4px;
    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
  
}
.price{
    color:red;
    font-size: 20px ;
    font-family: 'Courier New', Courier, monospace;
}
.inf_box{
    float:right;
    background-color: #e7eae8;
    width:600px;
  
}
.recommendation_container{
    width:1300px;
    clear: both;
    position: relative;
    left:20%;
}
.tittle_container{
    padding-top:20px;
    width:500px;
    margin:0 auto;
}
.product_container{
    position: relative;
    left:-30px;
    display: flex;
    flex-wrap: wrap;
}
.tittle2{
    top:40%;
    transform:translate(0,-50%) ;
    font-size: 25px;
}
.example{
    margin-top:-300px;
}
footer{
    padding-top:20px;
}
.blockk{
    clear:both;
}
.line{
    background-color: black;
    width:1300px;
    height:2px;
    clear:both;
    margin:0 auto;
}
.block{  
    width:1200px;
    height:80px;
    clear:both;
}
p{
    white-space:pre-wrap;
    word-break: keep-all;
}
.description{
    border: 2px solid black;
    padding-left:30px;
    border-radius: 20px;
    clear:both;
    width:1275px;
    position: relative;
    left:13%;
    h2{
      margin-left:41%;
    }
}
</style>
