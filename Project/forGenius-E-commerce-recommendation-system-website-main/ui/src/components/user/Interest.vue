<!--  Choose User Interest Field Page  -->

<template>
  <div class="interest_container">
    <div class="fix">
    <header>
        PLEASE CHOOSE YOUR INTEREST FIELD
    </header>
    <img class="logo" src=../../assets/2.png alt="logo">
    <div class="checkBox">
      <el-checkbox-group v-model="interestForm.interest" class="checkbox">
        <el-checkbox-button v-for="int in tags" :label="int" :key="int">{{int}}</el-checkbox-button>
      </el-checkbox-group>
      <el-button class='submit' @click="submitForm()">SUBMIT</el-button>
      </div>
   </div>
  </div>


</template>
<script>
// Page for user to choose their interest
import { interest_add } from '../../api/user'
const tagOptions = ['Fashion', 'Toys', 'Health', 'Pet', 'Electronics', 'Sports', 'Furniture', 'Game', 'Food', 'Personal Care']
export default {
  data () {
    return {
      tags: tagOptions,
      intest: [],
      interestForm: {
        token : '',
        interest: []
      }
    }
  },
  methods: {
    submitForm() {
      this.interestForm.token = sessionStorage.getItem('token');
      // Main operation for choose interest
      interest_add(this.interestForm).then ( res => {
          this.$message({message: 'Sucess!',type: 'success'});
          this.$router.push('userprofile');
      }).catch( error => {
          this.$message.error('Choose Interest Failed');
      })
    }
  }
}
</script>

<style lang="less" scoped>
.submit{
    position: relative;
    left:50%;
    height:50px;
    width:200px;
    transform: translate(-50%,-50%);
    border-radius: 10px;
    background: #786662;
    color: #fefefe;
    letter-spacing:10px;
    padding-left: 30px;
}
.interest_container{
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
.checkbox{
  position: relative;
}
.choose{
    position: relative;
    top:160px;
    background-color:#e7eae8;
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
.checkbox {
    height: 200px;
    position: relative;
    left:23%;
    margin-top: 100px;
}
</style>
