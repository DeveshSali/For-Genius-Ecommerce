<!--  Add Product Page  -->

<template>
    <div class="add_container">
     <div class="fix">
      <img class="logo" src=../../assets/2.png alt="logo" v-on:click="jumpManage">
      <div class="add_box">
            <h1>ADD&nbsp;PRODUCT</h1>
      <el-form ref="add_FormRef" :rules="addRules" :model="addForm" class="add_form" label-position="left" label-width="225px">
          <el-form-item label="NAME" class="change" prop="name">
            <el-input v-model="addForm.name" autocomplete="off">
            </el-input>
          </el-form-item>
          <el-form-item label="FEATURE" class="change" prop="features" >
            <el-input v-model="addForm.features" autocomplete="off" placeholder="Separate with space eg. phone computer">
            </el-input>
          </el-form-item>
          <el-form-item label="DESCRIPTION" class="change_description" prop="description">
            <el-input type="textarea" v-model="addForm.description" autocomplete="off">
            </el-input>
          </el-form-item>
          <el-form-item label="WARRANTY" class="change" prop="warranty" >
            <el-input v-model="addForm.warranty" autocomplete="off" placeholder="The warranty time (years)">
            </el-input>
          </el-form-item>
          <el-form-item label="DELIVERY DATE" class="change" prop="delivery_date">
            <el-input v-model="addForm.delivery_date" autocomplete="off" placeholder="The number of days it takes for delivery">
            </el-input>
          </el-form-item>
          <el-form-item label="PRICE" class="change" prop="price">
            <el-input v-model="addForm.price" autocomplete="off" placeholder="more than 0 and at most two decimal">
            </el-input>
          </el-form-item>
          <el-form-item label="PICTURE" class="change" prop="picture" >
            <el-input v-model="addForm.picture" autocomplete="off" placeholder="Please input the url of picture">
            </el-input>
          </el-form-item>
          <div class="block"></div>
          <el-form-item>
          <el-button type="brown" @click="submitAdd" class="submit" >CONFIRM</el-button>
          <el-button type="brown" @click="jumpManage" class="cancel">CANCEL</el-button>
          </el-form-item>

      </el-form>
      </div>
     </div>
    </div>
</template>

<script>
// Without admin login, this page cannot be reached
import { product_add } from '../../api/admin'
export default {
  data () {
    // The rules for input input data validation
    var checkName = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('name cannot be empty'))
      } else {
        callback()
      }
    }
    var checkDes = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('name cannot be empty'))
      } else {
        callback()
      }
    }
    var checkFeature= (rule, value, callback) => {
      if (!value) {
        return callback(new Error('feature cannot be empty'))
      } else {
        callback()
      }
    }
    var checkWarranty = (rule, value, callback) => {
      const mailReg = /^\d+$/
      if (!value) {
        return callback(new Error('warranty cannot be empty'))
      }
      setTimeout(() => {
        if (mailReg.test(value)) {
          callback()
        } else {
          callback(new Error('the warranty should be number'))
        }
      }, 100)
    }
    var checkDelivery= (rule, value, callback) => {
      const mailReg = /^\d+$/
      if (!value) {
        return callback(new Error('number of day cannot be empty'))
      }
      setTimeout(() => {
        if (mailReg.test(value)) {
          callback()
        } else {
          callback(new Error('the data should be number of day'))
        }
      }, 100)
    }
    var checkSales= (rule, value, callback) => {
      const mailReg = /^\d+$/
      if (!value) {
        return callback(new Error('Sales cannot be empty'))
      }
      setTimeout(() => {
        if (mailReg.test(value)) {
          callback()
        } else {
          callback(new Error('the sales should be number'))
        }
      }, 100)
    }
    var checkPrice= (rule, value, callback) => {
      const mailReg =  /^((0{1}\.\d{1,2})|([1-9]\d*\.{1}\d{1,2})|([1-9]+\d*))$/
      if (!value) {
        return callback(new Error('Price cannot be empty'))
      }
      setTimeout(() => {
        if (mailReg.test(value) & value != 0) {
          callback()
        } else {
          callback(new Error('Should more than 0 and at most two decimal'))
        }
      }, 100)
    }
    return {
      addForm: {
        name: '',
        features:'',
        description:'',
        warranty: '',
        delivery_date:'',
        price:'',
        picture: '',
      },
      //Input data validation
      addRules: {
        name: [
          { validator: checkName, trigger: 'blur' }
        ],
        warranty:[
          { validator: checkWarranty, trigger: 'blur'}
        ],
        delivery_date:[
          { validator: checkDelivery, trigger: 'blur'}
        ],
        sales:[
          { validator: checkSales, trigger: 'blur'}
        ],
        price:[

          { validator: checkPrice, trigger: 'blur'}
        ],
        description:[
          { validator: checkDes, trigger: 'blur'}
        ],
        features:[
          { validator: checkFeature, trigger: 'blur'}
        ]
      }
    }
  },
  created () {
    this.checkStat()
  },
  methods: {
    async checkStat () {
        console.log(await this.check());
    },
      check () {
        // Simple Navigation Guards
        if (sessionStorage.getItem("adtoken") != null) {
        } else {
          this.$router.push('/login')
        }
    },
    jumpManage () {
      this.$router.push('/manageproduct')
    },
    submitAdd () {
        this.$refs.add_FormRef.validate(async (valid) => {
        if (valid) {
          // Main operation for add prodcut
          product_add(this.addForm).then( res => {
            this.$message({message: 'Add product Sucess!',type: 'success'});
            this.$router.push('/manageproduct');
          }).catch( error => {
            this.$message.error('Add Prodcut Failed');
          })
          } else {
            // admin cannot submit if input did not pass the rules
            return false;
          }
        });
    }
  }
}
</script>

<style lang="less" scoped>
.block{
    height: 60px;
}
h1{
    position: relative;
    top:50px;
    font-size: 40px;
    font-weight:normal;
    font-family: 'segUi';
    letter-spacing:.2em;
}
.add_container {
    background-color: #d1dbda;
    height: 100%;
}
.add_box{
    background-color:#e7eae8;
    height: 630px;
    width: 750px;
    margin:0 auto;
    margin-top:-60px;
    border-radius: 30px;
    left:40px;
}
.logo{
    position: relative;
    height: 300px;
    left:-250px;
    cursor: pointer;
}
.add_form{
    width: 530px;
    margin:0 110px;
    border-radius: 80px;
    padding-top: 50px;
}
.el-form-item{
    margin-bottom:15px
}
.submit{
    position: relative;
    left:50%;
    height:50px;
    top:-5px;
    width:200px;
    transform: translate(-50%,-50%);
    border-radius: 10px;
    background: #786662;
    border-color: #786662;
    color: #fefefe;
    letter-spacing:10px;
    padding-left: 30px;
}
.cancel{
    position: relative;
    top:-55px;
    left:-60%;
    height:50px;
    width:200px;
    transform: translate(-50%,-50%);
    border-radius: 10px;
    background: #786662;
    border-color: #786662;
    color: #fefefe;
    letter-spacing:10px;
    padding-left: 30px;
}
.fix{
    margin:0 auto;
    margin-top:-100px;
    width:800px;
    text-align: center;
}
/*deep style for el in scoped*/
.add_form /deep/.timr.el-form .el-form-item__error {
    top: 30%;
    right: 25% !important;
    left: unset;
}
.el-input /deep/ .el-input__inner {
    border-radius:50px;
    height:30px;
}
.change /deep/ .el-form-item__label{
    font-family: 'segUi';
    letter-spacing:.1em;
    font-size: 18px;
}
.change_description /deep/ .el-form-item__label{
    font-family: 'segUi';
    letter-spacing:.1em;
    font-size: 18px;
}
.change_description /deep/ .el-form-item__input{
    height: 100%;
}
</style>

