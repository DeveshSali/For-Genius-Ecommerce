<!--  SignUp Page -->

<template>
    <div class="signup_container">
      <div class="fix">
      <img class="logo" src=../../assets/2.png alt="logo" v-on:click="jumpHome">
        <div class="signup_box">
            <h1>REGISTER</h1>
        <el-form ref="signupFormRef" :model="signupForm" :rules="signupRules" label-position="left" label-width="225px" class="signup_form">
            <el-form-item label="USERNAME"  class="change" prop="name">
              <el-input v-model="signupForm.name" placeholder="6-12 characters">
              </el-input>
        </el-form-item>
            <el-form-item label="EMAIL ADDRESS"  class="change" prop="email">
              <el-input v-model="signupForm.email" placeholder="contains “@” and end with “.com”">
              </el-input>
        </el-form-item>
            <el-form-item label="PASSWORD" class="change" prop="password">
              <el-input v-model="signupForm.password" type = "password" placeholder="6-12 characters contain uc,lc and number">
              </el-input>
        </el-form-item>
            <el-form-item label="CONFIRM PASSWORD" class="change" prop="confirm_password">
              <el-input v-model="signupForm.confirm_password" type = "password" placeholder="input password again">
              </el-input>
        </el-form-item>
            <el-form-item label="EMAIL CODE" class="code_change" prop="code">
              <el-input v-model="signupForm.code" >
              </el-input>
        </el-form-item>
        <div class="block"></div>
        <el-form-item>
        <el-button class='send' @click="send" type="brown">SEND</el-button>
        <el-button class='submit' @click="signup" type="brown">SUBMIT</el-button>
        </el-form-item>
        </el-form>
        <a  class="login_1">ALREADY REGISTERED, PLEASE <a style="color:black" href="#/login" text-decoration:underline >LOG IN</a></a>
        </div>
      </div>
    </div>
</template>

<script>
import { signup } from '../../api/user'
import { signup_code } from '../../api/user'
export default {
  data () {
    // The rules for input data validation
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
    var checkUsername = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('username cannot be empty'));
      } else {
        callback()
      }
    }
    var checkCode = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('code cannot be empty'));
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
        if (value === '') {
          callback(new Error('password cannot be empty'));
        } else if (value !== this.signupForm.password) {
          callback(new Error('Two inputs don\'t match!'));
        } else {
          callback();
        }
    }
    return {
      signupForm: {
        email: "",
	      name : "",
	      password: "",
        code: ""
      },
      code_form: {
        name: "",
        email: ""
      },
      //Input data validation
      signupRules: {
        email: [
          { validator: checkEmail, trigger: 'blur' }
        ],
        name: [
          { min: 6, max: 12, message: 'the username should be 6-12 characters', trigger: 'blur' },
          { validator: checkUsername, trigger: 'blur' }
        ],
        password: [
          { min: 6, max: 12, message: 'the password should be 6-12 characters', trigger: 'blur' },
          { validator: checkPassword, trigger: 'blur' }
        ],
        confirm_password: [
          { validator: confirmPassword, trigger: 'blur'}
       ],
        code: [
          { validator: checkCode, trigger: 'blur'}
        ]
      }
    }
  },
  methods: {
    signup () {
      this.$refs.signupFormRef.validate(async valid => {
        if (valid) {
          // Main operation for sign up
          signup(this.signupForm).then ( res => {
            this.$message({message: 'Sign up Sucess!',type: 'success'});
            sessionStorage.clear();
            console.log(res.data);
            sessionStorage.setItem('token',res.data.token);
            sessionStorage.setItem('username',res.data.username);
            this.$router.push('/interest');
          }).catch( error => {
            this.$message.error('Sign up failed. Please try again!');
          })
        } else {
          // user cannot submit if input did not pass the rules
          return false;
        }
      })
    },
    send() {
      // Fucntion for send code request
      const mailReg = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+\.com/;
      // Code cannot be sent when no email input
      if (this.signupForm.email == "") {
        this.$message.error('Email cannot be null');
      } else {
        if (mailReg.test(this.signupForm.email)) {
          // Get ready to send code
          this.code_form.name = this.signupForm.name;
          this.code_form.email = this.signupForm.email;
          // Main operation for send code
          signup_code(this.code_form).then ( res => {
            this.$message({message: 'Code Send Sucessfully!',type: 'success'});
          }).catch( error => {
            this.$message.error('Code Send Failed');
        })
        } else {
            // Code cannot be sent when email format is not right
            this.$message.error('Email form is not right');
        }
      }
    },
    jumpHome () {
      this.$router.push('Home');
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

.block{
    height: 50px;
}

.login_1{
    position: relative;
    bottom: 20px;
    color:black;
    transform: translate(-50%,0%);
    font-size: 15px;
    letter-spacing:.2em;
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
.send{
    position: absolute;
    left:80%;
    height:30px;
    top:-86px;
    width:100px;
    transform: translate(-50%,-50%);
    border-radius: 10px;
    background: #786662;
    color: #fefefe;
    border-radius: 20px;
    letter-spacing:7px;
    padding-left: 22px;
    padding-top:8px;
    font-size:13px;
}
.signup_container {
    background-color: #d1dbda;
    height: 100%;
}
.signup_box{
    background-color:#e7eae8;
    height: 550px;
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
.signup_form{
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
.code_change{
    width: 400px
}
.fix{
    margin:0 auto;
    margin-top:-30px;
    width:800px;
    text-align: center;
}
.el-form-item{
    margin-bottom:15px
}
/*deep style for el in scoped*/
.signup_form /deep/.timr.el-form .el-form-item__error {
    top: 30%;
    right: 25% !important;
    left: unset;
}
.change /deep/ .el-form-item__label{
    font-family: 'segUi';
    letter-spacing:.1em;
    font-size: 18px;
}
.code_change /deep/ .el-form-item__label{
    font-family: 'segUi';
    letter-spacing:.1em;
    font-size: 18px;
}
.el-input /deep/ .el-input__inner {
    border-radius:50px;
    height:30px;
}

</style>

