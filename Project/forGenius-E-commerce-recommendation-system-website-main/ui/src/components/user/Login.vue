<!--  Login Page  -->

<template>
    <div class="login_container">
      <div class="fix">
        <img class="logo" src=../../assets/2.png alt="logo" v-on:click="jumpHome">
        <div class="login_box">
            <h1>LOGIN</h1>
        <el-form ref="loginForm" :model="loginForm" :rules="loginRules" label-position="left" label-width="225px" class="login_form">
            <el-form-item label="EMAIL ADDRESS"  class="email_change" prop="email">
              <el-input v-model="loginForm.email" placeholder="contains “@” and end with “.com”">
              </el-input>
            </el-form-item>
            <el-form-item label="PASSWORD" class="password_change" prop="password">
              <el-input v-model="loginForm.password" type = "password">
              </el-input>
            </el-form-item>
            <div class="block"></div>
            <el-form-item>
              <el-button class='submit' @click="submitForm('loginForm')" type="brown">SUBMIT</el-button>
            </el-form-item>
        </el-form>
        <a  text-decoration:underline href="#/forgotpassword" class="forget">FORGET MY PASSWORD</a>
        </div>
          <a  class="signup_1">DON'T HAVE AN ACCOUNT YET? PLEASE <a style="color:black" href="#/signup" text-decoration:underline>SIGN UP </a></a>
      </div>
    </div>
</template>

<script>
// Page for log in
import '../../assets/css/form.css'
import { login } from '../../api/user'

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
    var checkpassword = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('password cannot be empty'))
      } else {
         callback()
      }
    }
    return {
      dialogVisible: false,
      loginForm: {
        email: '',
        password: ''
      },
      //Input data validation
      loginRules: {
        email: [
          { validator: checkEmail, trigger: 'blur' }
        ],
        password: [
          { validator: checkpassword, trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    jumpHome () {
      this.$router.push('/home')
    },
    submitForm(formName) {
        this.$refs[formName].validate(async (valid) => {
          if (valid) {
            // Main operation for login
            login(this.loginForm).then( res => {
              this.$message({message: 'Log in Sucess!',type: 'success'});
              // When return status code is 255
              // It means log in from admin
              if (res.status == 255) {
                sessionStorage.clear();
                sessionStorage.setItem('adtoken',res.data.token);
                sessionStorage.setItem('adusername',res.data.username);
                this.$router.push('/admin');
              } else {
                // else will be normal login
                sessionStorage.setItem('token',res.data.token);
                sessionStorage.setItem('username',res.data.username);
                // When page is from product
                // After login, page will back to product page
                if (sessionStorage.getItem('fromPro') != null) {
                  this.$router.push('/product');
                  sessionStorage.removeItem('fromPro');
                } else {
                  // Otherwise, page will redirect to userprofile page
                  this.$router.push('/userprofile');
                }
              }
            }).catch( error => {
              this.$message.error('Incorrect email or password');
            })
          } else {
            // user cannot submit if input did not pass the rules
            return false;
          }
        });
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
.block {
    width: 1000px;
    height: 65px;
}
.forget{
    position: relative;
    left: 15%;
    bottom:32%;
    color:black;
    transform: translate(-50%,0%);
    font-size: 15px;
    letter-spacing:.2em;
}
.signup_1{
    position: relative;
    bottom:50px;
    color:black;
    margin:0 auto;
    font-size: 15px;
    letter-spacing:.2em;
}
.submit{
    position: relative;
    height:50px;
    width:200px;
    top:10px;
    transform: translate(-50%,-50%);
    border-radius: 10px;
    background: #786662;
    color: #fefefe;
    letter-spacing:10px;
    padding-left: 30px;
    border-color: #786662;
}
.login_container {
    background-color: #d1dbda;
    height: 100%;
}
.login_box{
    background-color:#e7eae8;
    height: 425px;
    width: 750px;
    margin:0 auto;
    border-radius: 30px;
    margin-top:-30px;
}
.logo{
    position: relative;
    height: 300px;
    left:-250px;
    cursor: pointer;
}
.login_form{
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
.fix{
    margin:0 auto;
    margin-top:-30px;
    width:800px;
    text-align: center;
}
/*deep style for el in scoped*/
.el-input /deep/ .el-input__inner {
    border-radius:50px;
    height:30px;
}
.email_change /deep/ .el-form-item__label{
    font-family: 'segUi';
    letter-spacing:.1em;
    font-size: 18px;
}
.password_change /deep/ .el-form-item__label{
    font-family: 'segUi';
    letter-spacing:.1em;
    font-size: 18px;
}
</style>

