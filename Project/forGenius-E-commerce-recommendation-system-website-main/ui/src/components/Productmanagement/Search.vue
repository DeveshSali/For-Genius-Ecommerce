<!--  Search Result Page  -->

<template>
  <div class="search_container">
    <div class="fix">
    <header>
        SEARCH&nbsp;RESULT
    </header>
    <img class="logo" src=../../assets/2.png alt="logo" v-on:click="jumpHome">
    <div class="search">
      <form action="" class="parent">
        <input type="text" v-model="keywords" placeholder="search keywords">
        <input type="submit" v-on:click="jumpResult" value="SEARCH">
      </form>
    </div>
    <div>
      <el-select v-model="value" placeholder="Select sort method" class="choose">
        <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value">
        </el-option>
      </el-select>
      <el-button class="apply" type="white" icon="el-icon-thumb" v-on:click="reload()"> Apply</el-button>
    </div>
      
    <div class="search-container">
        <Search v-for="(obj,ind) in product" :key="obj.product_id"
        :proName="obj.name"
        :proDescription="obj.description"
        :proPrice="obj.price"
        :proPic="obj.picture"
        :proId="obj.product_id"
        :index="ind"
        >
        </Search>
        <h2 v-show="isRes">NO RESULT</h2>
    </div>
    </div>
  </div>
</template>

<script>
import Search from '../mod/Searchpro.vue'
import { ser_res } from '../../api/product' 
export default {
    inject:['reload'],
    data () {
      return {
        view_form: {
          token: '',
          search: '',
          sorting: ''
        },
        product: [],
        product_id: '',
        options: [{
            value: 'price_low',
            label: 'Price Low'
          },{
            value: 'price_high',
            label: 'Price High'
          },{
            value: 'best_sell',
            label: 'Best Sales'
          },{
            value: 'a_to_z',
            label: 'From A to Z'
          },{
            value: 'z_to_a',
            label: 'From Z to A'
          },{
            value: 'relevance',
            label: 'Recommendation'
          }],
        value: '',
        keywords: '',
        isRes: false
        }
    },
    created () {
      this.loadRes()
    },
    components: {
        Search
    },
    watch: {
      value(newVal, oldVal) {
        sessionStorage.setItem('sort',newVal);
      }
    },
    methods: {
      // Load search result
      async loadRes() {
        // Store token if user logged in
        if (sessionStorage.getItem('token') != null) {
          this.view_form.token = sessionStorage.getItem('token');
        }
        // Get search word from sessionStorage
        this.keywords = sessionStorage.getItem('word');
        this.view_form.search = sessionStorage.getItem('word');
        // Get sort method when sort already inside of sessionStorage
        if (sessionStorage.getItem('sort') != null) {
          this.view_form.sorting = sessionStorage.getItem('sort');
          this.value = sessionStorage.getItem('sort');
        } else {
          // if no pre-setted sort method
          // Defulat will be 'relevance'
          this.view_form.sorting = 'relevance';
          this.value = 'relevance';
        }
        // Main operation to get search result
        ser_res(this.view_form).then( res => {
          this.product = res.data;
          // Figure out whether search operation find products
          if (this.product.length == 0) {
            this.isRes = true;
          } else {
            this.isRes = false;
          }
        }).catch( error => {
          this.$message.error('Get Search Result Failed');
        })
      },
      jumpHome () {
        this.$router.push('/home')
      },
      // extra search in search result page
      jumpResult () {
        sessionStorage.setItem('word',this.keywords);
        this.reload();
      },
    }
}
</script>


<style lang="less" scoped>
.search-container {
    position: relative;
    top:10px;
    left:8%;
    width:1500px;
    display: flex;
    flex-wrap: wrap;
}
.search_container{
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
.choose{
    position: relative;
    left: 1220px;
}

.search {
    width: 1000px;
    height: 50px;
    margin: 0px auto;
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

.apply {
    float: right;
    margin-right:210px;
}
</style>
