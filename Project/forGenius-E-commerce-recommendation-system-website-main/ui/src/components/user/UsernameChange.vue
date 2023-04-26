<!--  Change Username Page  -->

<template>
    <div class="usernamechange_container">
      <div class="fix">
        <img class="logo" src=../../assets/2.png alt="logo" v-on:click="jumpProfile"> 
        <div class="usernamechange_box">
            <h1>USERNAME&nbsp;CHANGE</h1>
        <el-form ref="usernamechangeFormRef" :model="usernamechangeForm" :rules="usernamechangeRules" label-position="left" label-width="225px" class="usernamechange_form">
            <el-form-item label="NEW USER NAME"  class="username_change" prop="newname">
              <el-input v-model="usernamechangeForm.newname" placeholder="6-12 characters">
              </el-input>
        </el-form-item>
        </el-form>
        <el-button class='send' @click="usernamechange" type="brown">CONFIRM</el-button>
        </div>
      </div>
    </div>
</template>

<script>
import { change_username } from '../../api/user'
export default {
  data () {
    // The rules for input value
    var checkUsername = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('username cannot be empty'));
      } else {
        callback()
      }
    }
    return {
      usernamechangeForm: {
        token: '',
        newname: ''
      },
      usernamechangeRules: {
        newname: [
          { min: 6, max: 12, message: 'the username should be 6-12 characters', trigger: 'blur' },
          { validator: checkUsername, trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    usernamechange () {
      this.$refs.usernamechangeFormRef.validate(valid => {
        if (valid) {
          // Main operation for change user name
          this.usernamechangeForm.token = sessionStorage.getItem('token');
          change_username(this.usernamechangeForm).then( res => {
            this.$message({message: 'User Name Changed',type: 'success'});
            sessionStorage.setItem('username',this.usernamechangeForm.newname);
            this.$router.push('/userprofile')
          }).catch( error => {
              this.$message.error('Change User Name Failed');
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

.send{
    position: relative;
    bottom:-15%;
    height:50px;
    width:180px;
    border-radius: 10px;
    background: #786662;
    color: #fefefe;
    letter-spacing:10px;
    padding-left: 27px;
    border-color: #786662;
}
.usernamechange_container {
    background-color: #d1dbda;
    height: 100%;
}
.usernamechange_box{
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
.usernamechange_form{
    width: 530px;
    margin:0 100px;
    border-radius: 80px;
    padding-top: 50px;
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
.usernamechange_form /deep/.timr.el-form .el-form-item__error {
    top: 30%;
    right: 25% !important;
    left: unset;
}
.username_change /deep/ .el-form-item__label{
    font-family: 'segUi';
    letter-spacing:.1em;
    font-size: 18px;
}
.el-input /deep/ .el-input__inner {
    border-radius:50px;
    height:30px;
}
</style>

