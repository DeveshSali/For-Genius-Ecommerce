<!--  Home Page  -->

<template>
    <div id="home_container">
      <div class="fix">
        <header>
            <img id="logo" src=../assets/logoThin.png alt="logo" v-on:click="addFn">
            <div class="button_position">
            <el-button icon="el-icon-user" class="signUp" v-on:click="jumpSign" v-show="isGuest" type="white">Sign up</el-button>
            <el-button icon= "el-icon-user-solid" class="logIn" v-on:click="jumpLog" v-show="isGuest" type="white" >Log in</el-button>
            <el-button v-on:click="jumpHome" @click="logOut" v-show="isUser" type="white" icon="el-icon-switch-button">Log out</el-button>
            <el-button id="usern" v-show="isUser" @click="jumpProfile" icon="el-icon-user-solid" type="white">{{ username }}</el-button>
            <a href="http://127.0.0.1:8000/admin/login/?next=/admin/">
            <el-button class="logIn" v-show="isOk">Admin Log in</el-button>
            </a>
            </div>
        </header>
        <main>
          <div>
            <img id="logo" src=../assets/logoThin.png alt="logo">
          </div>
          <span id="slogon">DISCOVER YOUR PRODUCT</span>
          <div class="search">
            <form action="" class="parent">
              <input type="text" v-model="keywords" placeholder="search keywords">
              <input type="submit" v-on:click="jumpResult" value="SEARCH">
            </form>
          </div>
        </main>
        <div class="recommendation_container">
          <div>
            <div class="tittle_container">
              <div class="tittle">
              <p>RECOMMENDATION</p>
              </div>
              <div class="l_tittle">
              <p>THE PRODUCTS</p>
              <div class="line">
              </div>
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
            <div style="clear:both">
            </div>
          </div>
        </div>
        </div>
        <footer>
        <img src=../assets/home_foot.jpeg alt="foot">
        </footer>
    </div> 
</template>

<script>
import { logout } from '../api/user'
import { rec_guest } from '../api/product'
import { rec_user } from '../api/product'
import Home from './mod/Homepro.vue'
export default {
   components: {
        Home
    },
  inject:['reload'],
  data () {
    return {
      tokenForm: {
            token: ''
      },
      keywords: '',
      counter: 1,
      isOk: false,
      isUser: false,
      isGuest: false,
      username: '',
      products: []
    }
  },
  created () {
    this.checkStat()
  },
  methods: {
    async checkStat () {
      // Wait check() complete
      await this.check();
    },
    check () {
      // Judging the current situation
      // Have user log in
      if (sessionStorage.getItem("username") != null) {
        this.isUser = true;
        this.isGuest = false;
        this.username = sessionStorage.getItem('username');
        this.tokenForm.token = sessionStorage.getItem('token');
        // Load recommendation product for homepage
        rec_user(this.tokenForm).then ( res => {
          this.products = res.data.products;
        }).catch( error => {
        })
        return this.username;
      } 
      // When no user log in
      else {
        this.isGuest = true;
        this.isUser = false;
        sessionStorage.clear();
        // Load recommendation product for guest
        rec_guest(this.tokenForm).then ( res => {
          this.products = res.data.products;
        }).catch( error => {
        })
        return this.isGuest;
      }
    },
    jumpSign () {
      this.$router.push('/signup')
    },
    jumpLog () {
      this.$router.push('/login')
    },
    jumpResult () {
      // Fucntion for search
      // When search box has no input
      if(!this.keywords){
        this.$message.error("Please input search keywords");
      }
      // When search box only has space
      else if(this.keywords.match(/^[ ]*$/)){
        this.$message.error("Please input search keywords");
      }
      // Real search trigger
      else{
        sessionStorage.setItem('word',this.keywords);
        this.$router.push('/search')
      }},
    jumpProfile () {
      this.$router.push('/userprofile')
    },
    jumpProduct () {
      this.$router.push('/product')
    },
    addFn(){
      if (this.counter == 5) {
        this.isOk = true;
      } else {
        this.counter++;
      }
    },
    jumpHome () {
      this.$router.push('home')
    },
    async logOut () {
      // Function for log out
      logout(this.tokenForm).then ( res => {
          this.$message({message: 'Log out Sucess!',type: 'success'});
          sessionStorage.clear();
          this.tokenForm.token = "";
          this.reload();
      }).catch( error => {
          this.$message.error('Log out Failed');
      })
    }
  }
}
</script>

<!--CSS with scoped and less this parameter is valid only for the current page-->
<style lang="less" scoped>
*{
    font-family: 'segUi';
}
#home_container {
    background-color: #d1dbda;
    height: 100%;
}
.fix{
    width:1800px;
    margin:0 auto;

}
header {
    height: 100px;
    width: 1800px;
    margin: 0 auto;
}
header #logo {
    height: 50px;
    float: left;
    margin-top: 25px;
    margin-left:400px;
}
.button_position{
  float: right;
  margin-right:400px;
}
button {
    float: right;
    // border-radius: 4px;
    padding: 2px 15px;
    margin-left: 16px;
    margin-top: 35px;
    // border-color: grey;
    // color: grey;
    height: 30px;
    border-radius: 10px;
    border-color: #786662;
    background-color: #e7eae8;
    cursor: pointer;
}
main {
    width: 1000px;
    margin: 0 auto;
}
main #logo {
    width: 800px;
    margin-left: 100px;
}
#slogon {
    float: left;
    margin-left: 300px;
    letter-spacing:10px;
}
.search {
    width: 1000px;
    height: 50px;
    margin: 50px auto;
}
.parent {
    width: 100%;
    height: 50px;
    top: 4px;
    position: relative;
}
.parent>input:first-of-type {
    width: 550px;
    height: 40px;
    border: 1px solid #ccc;
    font-size: 16px;
    outline: none;
    border-radius: 20px;
    margin-left: 150px;
    background-color:rgb(238, 238, 236);
    padding-left: 10px;
    margin-right: 5px;
}
.parent>input:first-of-type:focus {
    border: 1px solid #786662;
}
.parent>input:last-of-type {
    width: 100px;
    height: 40px;
    position: absolute;
    background:#786662;
    color: #fff;
    font-size: 16px;
    outline: none;
    border-radius: 20px;
    border-color: #786662;
    cursor: pointer;
}
.recommendation_container{
    background-color: white;
    margin:0 auto;
    width:1700px;
}
.tittle_container{
    float: left;
    width:500px;
    height:600px;
    overflow: hidden;
}
.product_container{
    float: right;
    width:1200px;
    display: flex;
    flex-wrap: wrap;
}
.tittle{
    position: relative;
    left:30%;
    top:40%;
    transform:translate(0,-50%) ;
    font-size: 25px;
}
.example{
    margin-top:-300px;
}
.l_tittle{
    font-size: 5px;
    position: relative;
    left:34%;
    top:40%;
    transform:translate(0,-50%) ;
}
.line{
    height:2px;
    width:89px;
    position: relative;
    left:-1%;
    top:40%;
    transform:translate(0,-50%) ;
    background-color:rgb(0, 217, 255);
}
footer{
    position: relative;
    left:50%;
    transform: translate(-50%);
    height:375px;
    width:100%;
    background:#2f2a29;
    margin-top:20px;
    bottom:0%;
    img{
          height:375px;
          width:1800px;
          margin:0 auto;
          display:block;
    }
}
</style>