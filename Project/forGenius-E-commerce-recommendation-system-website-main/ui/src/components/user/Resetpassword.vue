<!--  Reset Password Page For When User Logged in  -->

<template>
    <div class="reset_container">
      <div class="fix">
      <img class="logo" src=../../assets/2.png alt="logo" v-on:click="jumpProfile">
        <div class="reset_box">
            <h1>RESET&nbsp;PASSWORD</h1>
        <el-form ref="resetFormRef" :model="resetForm" :rules="resetpasswordRule" label-position="left" label-width="225px" class="reset_form">
            <el-form-item label="OLD PASSWORD"  class="oldpassword_change" prop="old_password">
              <el-input v-model="resetForm.old_password">
              </el-input>
        </el-form-item>
            <el-form-item label="NEW PASSWORD" class="newpassword_change" prop="new_password">
              <el-input v-model="resetForm.new_password" type = "password" placeholder="6-12 characters contain uc,lc and number">
              </el-input>
        </el-form-item>
            <el-form-item label="CONFIRM PASSWORD" class="password_change" prop="confirm_password">
              <el-input v-model="resetForm.confirm_password" type = "password" placeholder="input password again">
              </el-input>
        </el-form-item>
        </el-form>
        <el-button class='submit' @click="reset" type="brown">SUBMIT</el-button>
        </div>
      </div>
    </div>
</template>

<script>
import { change_password } from '../../api/user'
export default {
  data () {
    // The rules for input data validation
    var checkOldpassword = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('password cannot be empty'))
      } else {
         callback()
      }
    }
    var checkPassword = (rule, value, callback) => {
      const mailReg = /^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])/
      if (!value) {
        return callback(new Error('password cannot be empty'))
      }
      setTimeout(() => {
        if (mailReg.test(value)) {
          callback()
        } else {
          callback(new Error('Invalid password'))
        }
      }, 100)
    }
    var confirmPassword = (rule, value, callback) => {
        if (!value) {
          callback(new Error('password cannot be empty'));
        } else if (value !== this.resetForm.new_password) {
          callback(new Error('Two inputs don\'t match!'));
        } else {
          callback();
        }
    }
    return {
      resetForm: {
        token: '',
        old_password: '',
        new_password: ''
      },
      //Input data validation
      resetpasswordRule: {
        old_password: [
          { min: 6, max: 12, message: 'the password should be 6-12 characters', trigger: 'blur' },
          { validator: checkOldpassword, trigger: 'blur' }
        ],
        new_password: [
          { min: 6, max: 12, message: 'the password should be 6-12 characters', trigger: 'blur' },
          { validator: checkPassword, trigger: 'blur' }
        ],
        confirm_password: [
          { validator: confirmPassword, trigger: 'blur'}
       ]
      }
    }
  },
  methods: {
    reset () {
      // Main operation for reset password
      this.$refs.resetFormRef.validate(async valid => {
        this.resetForm.token = sessionStorage.getItem('token');
        if (valid) {
          change_password(this.resetForm).then( res => {
            this.$message({message: 'Updated Successfully!',type: 'success'});
            this.$router.push('/userprofile');
          }).catch( error => {
             this.$message.error('Incorrect old password or new password invalid');
          })
        }
      })
    },
    jumpProfile () {
      this.$router.push('/userprofile')
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

.submit{
    position: relative;
    height:50px;
    width:200px;
    border-radius: 10px;
    background: #786662;
    color: #fefefe;
    letter-spacing:10px;
    padding-left: 30px;
    border-color: #786662;
    top:30px;
}
.reset_container {
    background-color: #d1dbda;
    height: 100%;
}
.reset_box{
    background-color:#e7eae8;
    height: 425px;
    width: 750px;
    margin:0 auto;
    border-radius: 30px;
    left:40px;
    margin-top:-60px;
}
.logo{
    position: relative;
    height: 300px;
    left:-250px;
    cursor: pointer;
}
.reset_form{
    width: 530px;
    margin:0 100px;
    border-radius: 80px;
    padding-top: 50px;
}
.fix{
    margin:0 auto;
    margin-top:-80px;
    width:800px;
    text-align: center;
}
/*deep style for el in scoped*/
.reset_form /deep/.timr.el-form .el-form-item__error {
    top: 30%;
    right: 25% !important;
    left: unset;
}
.oldpassword_change /deep/ .el-form-item__label{
    font-family: 'segUi';
    letter-spacing:.1em;
    font-size: 18px;
}
.newpassword_change /deep/ .el-form-item__label{
    font-family: 'segUi';
    letter-spacing:.1em;
    font-size: 18px;
}

.password_change /deep/ .el-form-item__label{
    font-family: 'segUi';
    letter-spacing:.1em;
    font-size: 18px;
}
.el-input /deep/ .el-input__inner {
    border-radius:50px;
    height:30px;
}
</style>
