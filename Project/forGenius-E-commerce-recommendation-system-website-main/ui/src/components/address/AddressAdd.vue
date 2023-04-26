<!--ADD Address Page   -->

<template>
    <div class="add_container">
     <div class="fix">
      <img class="logo" src=../../assets/2.png alt="logo" v-on:click="jumpAddress">
      <div class="add_box">
            <h1>ADD&nbsp;ADDRESS</h1>
      <el-form ref="add_FormRef" :rules="addRules" :model="addForm" class="add_form" label-position="left" label-width="225px">
          <el-form-item label="NAME" class="username_change" prop="name">
            <el-input v-model="addForm.name" autocomplete="off">
            </el-input>
          </el-form-item>
          <el-form-item label="PHONE NUMBER" class="username_change" prop="phone_number">
            <el-input v-model="addForm.phone_number" autocomplete="off">
            </el-input>
          </el-form-item>
           <el-form-item label="COUNTRY" class="username_change" prop="country">
            <el-input v-model="addForm.country" autocomplete="off">
            </el-input>
          </el-form-item>
          <el-form-item label="STATE" class="username_change" prop="state">
            <el-input v-model="addForm.state" autocomplete="off">
            </el-input>
          </el-form-item>
          <el-form-item label="SUBURB" class="username_change" prop="suburb">
            <el-input v-model="addForm.suburb" autocomplete="off">
            </el-input>
          </el-form-item>
          <el-form-item label="POSTAL CODE" class="username_change" prop="post_code">
            <el-input v-model="addForm.post_code" autocomplete="off">
            </el-input>
          </el-form-item>
          <el-form-item label="ADDRESS" class="username_change" prop="address_line">
            <el-input v-model="addForm.address_line" autocomplete="off">
            </el-input>
          </el-form-item>
          <div class="block"></div>
          <el-form-item>
          <el-button type="brown" @click="submitAdd" class="submit">CONFIRM</el-button>
          </el-form-item>
      </el-form>
      </div>
     </div>
    </div>
</template>

<script>
import { address_add } from '../../api/user'
export default {
  data () {
    // The rules for input data validation
    var checkName = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('Username cannot be empty'))
      } else {
        callback()
      }
    }
    var checkAddress = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('Address cannot be empty'))
      } else {
        callback()
      }
    }
    var checkPhone = (rule, value, callback) => {
      const mailReg = /^\d+$/
      if (!value) {
        return callback(new Error('Phonenumber cannot be empty'))
      }
      setTimeout(() => {
        if (mailReg.test(value)) {
          callback()
        } else {
          callback(new Error('Phonenumber should be number'))
        }
      }, 100)
    }
    var checkState = (rule, value, callback) => {
      const mailReg = /^[A-Za-z]+$/
      if (!value) {
        return callback(new Error('State cannot be empty'))
      }
      setTimeout(() => {
        if (mailReg.test(value)) {
          callback()
        } else {
          callback(new Error('State should all be letters'))
        }
      }, 100)
    }
    var checkSuburb = (rule, value, callback) => {
      const mailReg = /^[A-Za-z]+$/
      if (!value) {
        return callback(new Error('Suburb cannot be empty'))
      }
      setTimeout(() => {
        if (mailReg.test(value)) {
          callback()
        } else {
          callback(new Error('Suburb should all be letters'))
        }
      }, 100)
    }
    var checkCountry = (rule, value, callback) => {
      const mailReg = /^[A-Za-z]+$/
      if (!value) {
        return callback(new Error('Country cannot be empty'))
      }
      setTimeout(() => {
        if (mailReg.test(value)) {
          callback()
        } else {
          callback(new Error('Country should all be letters'))
        }
      }, 100)
    }
    var checkCode = (rule, value, callback) => {
      const mailReg = /^\d+$/
      if (!value) {
        return callback(new Error('Postal code cannot be empty'))
      }
      setTimeout(() => {
        if (mailReg.test(value)) {
          callback()
        } else {
          callback(new Error('Postal code should be number'))
        }
      }, 100)
    }
    return {
      addForm: {
        token: '',
        name: '',
        address_line: '',
        phone_number: '',
        country:'',
        state:'',
        suburb:'',
        post_code:''
      },
      // Input data validation
      addRules: {
        name: [
          { validator: checkName, trigger: 'blur' }
        ],
        address_line: [
          { validator: checkAddress, trigger: 'blur' }
        ],
        phone_number: [
          { validator: checkPhone, trigger: 'blur'  }
        ],
        post_code: [
          { validator: checkCode, trigger: 'blur'  }
        ],
        suburb: [
          { validator: checkSuburb, trigger: 'blur'  }
        ],
        state: [
          { validator: checkState, trigger: 'blur'  }
        ],
        country: [
          { validator: checkCountry, trigger: 'blur'  }
        ]
      }
    }
  },
  methods: {
    jumpAddress () {
        if (sessionStorage.getItem('from') == 1) {
            sessionStorage.removeItem('from');
            this.$router.push('/order');
        }
        else {
          this.$router.push('/address');
        }
    },
    // Submit address
    submitAdd () {
        this.$refs.add_FormRef.validate(async (valid) => {
          if (valid) {
            this.addForm.token = sessionStorage.getItem('token');
            // Main operation for submit address user want to add
            address_add(this.addForm).then( res => {
              this.$message({message: 'Add Address Sucess!',type: 'success'});
              // If the page is from order page
              // After sucess, page will back to order
              if (sessionStorage.getItem('from') == 1) {
                sessionStorage.removeItem('from');
                this.$router.push('/order');
              } 
              // Otherwise, page will redirect to address page
              else {
                this.$router.push('/address');
              }          
            }).catch( error => {
                this.$message.error('Add Address Failed');
            })
              } else {
                console.log('error submit!!');
                return false;
              }
        });
    }
  }
}
</script>

<style lang="less" scoped>
.fix{
    margin:0 auto;
    margin-top:-30px;
    width:800px;
    text-align: center;
}
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
    height: 630 px;
    width: 750px;
    margin:0 auto;
    border-radius: 30px;
    margin-top:-60px;
}
.logo{
    position: relative;
    height: 300px;
    left:-250px;
    cursor: pointer;
}
.add_form{
    width: 530px;
    margin:0 100px;
    border-radius: 80px;
    padding-top: 50px;
}
.el-form-item{
    margin-bottom:15px
}
.submit{
    position: relative;
    height:50px;
    width:200px;
    transform: translate(-50%,-75%);
    border-radius: 10px;
    background: #786662;
    color: #fefefe;
    letter-spacing:10px;
    padding-left: 30px;
    border-color: #786662;
}

/*deep style for el in scoped*/
.username_change /deep/ .el-form-item__label{
    font-family: 'segUi';
    letter-spacing:.1em;
    font-size: 18px;
}
.add_form /deep/.timr.el-form .el-form-item__error {
    top: 30%;
    right: 25% !important;
    left: unset;
}
.el-input /deep/ .el-input__inner {
    border-radius:50px;
    height:30px;
}
</style>

