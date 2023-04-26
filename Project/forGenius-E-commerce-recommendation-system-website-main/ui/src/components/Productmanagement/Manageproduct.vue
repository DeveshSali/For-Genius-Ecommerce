<!--  Manage Product Main Page  -->

<template>
  <div class="manage_container">
    <div class="fix">
    <header>
        MANAGE&nbsp;PRODUCT
    </header>
      <img class="logo" src=../../assets/2.png alt="logo" v-on:click="jumpAdmin">
      <el-button type="brown" class="addProduct" v-on:click="jumpAddproduct">ADD PROCDUCT</el-button>
    <div class="sort">
      <el-select v-model="value" clearable placeholder="Sort by Sales data" class="choose">
        <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value">
        </el-option>
      </el-select>
      <el-button class="apply" type="white" v-on:click="reset_sort" icon="el-icon-thumb"> Apply</el-button>
    </div>
    <div class="manage-container">
      <Manage v-for="(obj,ind) in product" :key="ind"
      :id="obj.product_id"
      :name="obj.name"
      :warr="obj.warranty"
      :description="obj.description"
      :sales="obj.sales_data"
      :price="obj.price"
      :pic="obj.picture"
      :delivery="obj.delivery_date"
      :features="obj.features"
      :index = "ind"
      @delPro = "del"
      >

      </Manage>
    </div>
    </div>
  </div>
</template>

<script>
import Manage from '../mod/Manageproductpro.vue'
import { admin_view } from '../../api/admin'
import { admin_sort } from '../../api/admin'
import { product_delete } from '../../api/admin'
export default {
    inject:['reload'],
    data () {
      return {
        view_form: {},
        sort_form: {
          sorting: ""
        },
        product: [],
        deleteForm : {
            product_id: ''
        },
        options: [{
            value: 'low_to_high',
            label: 'From Low to High'
          },{
            value: 'high_to_low',
            label: 'From High to Low'
          }],
        value: ''
      }
    },
    created () {
      this.loadPro(),
      this.checkStat()
    },
    components: {
        Manage
    },
    watch: {
      value(newVal, oldVal) {
        sessionStorage.setItem('adsort',newVal);
      }
    },
    methods: {
      // Load all exist product
      async loadPro() {
        // Get sort method when sort already inside of sessionStorage
        // For admin
        if (sessionStorage.getItem('adsort') != null) {
          this.sort_form.sorting = sessionStorage.getItem('adsort');
          this.value = sessionStorage.getItem('adsort');
          admin_sort(this.sort_form).then( res => {
            console.log(res.data.data.product_details);
            this.product = res.data.data.product_details;
          }).catch( error => {
              this.$message.error('Failed');
          })
        } else {
          // Defulat will be normal null sort
          admin_view(this.view_form).then( res => {
            console.log(res.data.data.product_details);
            this.product = res.data.data.product_details.slice().reverse();
          }).catch( error => {
              this.$message.error('Failed');
          })
        }
        
      },
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
      jumpAddproduct () {
        sessionStorage.removeItem('adsort');
        this.$router.push('/addproduct');
      },
      jumpAdmin () {
        sessionStorage.removeItem('adsort');
        this.$router.push('/admin');
        
      },
      reset_sort () {
        if ( this.value != "") {
        } else {
          sessionStorage.removeItem('adsort');
        }
        this.reload();
      },
      // Delete a product 
      del(index) {
        this.deleteForm.product_id = this.product[index].product_id;
        this.product.splice(index, 1);
        // Main operation to delete
        product_delete(this.deleteForm).then( res => {
            this.$message({message: 'Delete Sucess!',type: 'success'});
            this.reload();
        }).catch( error => {
            this.$message.error('Delete Failed');
        })
      },
    }
}
</script>


<style lang="less" scoped>
.manage-container {
    margin:15px auto;
    padding-top:30px;
    width:1500px;
    clear: both;
}
.manage_container{
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
.addProduct{
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
.sort{
    float:right;
    margin-right:120px;
    margin-top:30px;  
}
.apply{
    margin-left:30px;
}
</style>