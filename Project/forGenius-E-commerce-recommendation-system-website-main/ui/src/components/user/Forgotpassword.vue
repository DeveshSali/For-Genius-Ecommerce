<!--  Send Code To User E-mail Page For Forgot Password  -->

<template>
    <div class="fogot_container">
      <div class="fix">
        <img class="logo" src=../../assets/2.png alt="logo" v-on:click="jumpProfile"> 
        <div class="fogot_box">
            <h1>FORGOT&nbsp;PASSWORD</h1>
        <el-form ref="forgotFormRef" :model="forgotForm" :rules="forgotRules" label-position="left" label-width="225px" class="forgot_form">
            <el-form-item label="EMAIL ADDRESS"  class="email_change" prop="email">
              <el-input v-model="forgotForm.email" placeholder="contains “@” and end with “.com”">
              </el-input>
        </el-form-item>
        </el-form>
        <el-button class='send' @click="forgot" type="brown">SEND CODE</el-button>
        </div>
      </div>
    </div>
</template>

<script>
// Send code page when user forgot password 
import { send_code } from '../../api/user'
export default {
  data () {
    // The rules for Input data validation
    var checkEmail = (rule, value, callback) => {
      const mailReg = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+\.com/
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
      forgotForm: {
        email: ''
      },
      //Input data validation
      forgotRules: {
        email: [
          { validator: checkEmail, trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    forgot () {
      this.$refs.forgotFormRef.validate(valid => {
        console.log(valid);
        if (valid) {
          // Main operation for send code for forgot password
          send_code(this.forgotForm).then( res => {
          this.$message({message: 'Code sent',type: 'success'});
          this.$router.push('/resetpassword/forgot')
          }).catch( error => {
            this.$message.error('Send Code For Forgot Password Failed');
          })
        }
      })
    },
    jumpProfile () {
      this.$router.push('/login')
    }
  }
}
</script>

<style lang="less" scoped>

h1{
    position: relative;
    top:50px;
    font-size: 40px;
    font-weight:normal;
    font-family: 'segUi';
    letter-spacing:.2em;
}

.send{
    position: relative;
    bottom:-15%;
    height:50px;
    width:200px;
    border-radius: 10px;
    background: #786662;
    color: #fefefe;
    letter-spacing:10px;
    padding-left: 20px;
    border-color: #786662;
}
.fogot_container {
    background-color: #d1dbda;
    height: 100%;
}
.fogot_box{
    background-color:#e7eae8;
    height: 300px;
    width: 750px;
    margin:0 auto;
    border-radius: 30px;
    left:40px;
    margin-top:-30px;
}
.logo{
    position: relative;
    height: 300px;
    left:-250px;
    cursor: pointer;
}
.forgot_form{
    width: 530px;
    margin:0 100px;
    border-radius: 80px;
    padding-top: 50px;
}
.username{
    border-radius: 40px;
}
.email{
    border-radius: 30px;
}
.el-form-item{
    margin-bottom:15px
}
.fix{
    margin:0 auto;
    margin-top:-30px;
    width:800px;
    text-align: center;
}
/*deep style for el in scoped*/
.forgot_form /deep/.timr.el-form .el-form-item__error {
    top: 30%;
    right: 25% !important;
    left: unset;
}
.email_change /deep/ .el-form-item__label{
    font-family: 'segUi';
    letter-spacing:.1em;
    font-size: 18px;
}
.el-input /deep/ .el-input__inner {
    border-radius:50px;
    height:30px;
}
</style>

