<!--  Admin Page  -->

<template>
    <div id="admin_container">
        <div class="fix">
        <header>
            <img id="logo" src=../../assets/logoThin.png alt="logo" v-on:click="jumpHome">
            <div class="button_position">
            <el-button @click="logOut" type="white" icon="el-icon-switch-button">Log out</el-button>
            <el-button id="usern" type="white" icon="el-icon-user-solid">{{ username }}</el-button>
            </div>
        </header>
        <main>
            <img id="logo" src=../../assets/logoThin.png alt="logo">
            <button class="manageProduct" v-on:click="jumpManageproduct">MANAGE PRODUCT</button>
            <button class="manageProduct" v-on:click="jumpOrder">VIEW ORDER</button>
        </main>
        <div style="clear:both; height:20px"></div>
        </div>
        <footer>
         <img src=../../assets/home_foot.jpeg alt="foot">
        </footer>
    </div>
</template>

<script>
// Page for admin
// Without admin login, this page cannot be reached
import { logout } from '../../api/user'
export default {
    data () {
        return {
            tokenForm: {
                token: ''
            },
        }
    },
    created () {
        this.checkStat(),
        this.username = sessionStorage.getItem('adusername')
    },
    methods: {
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
        logOut () {
            this.tokenForm.token = sessionStorage.getItem('adtoken');
            // Main operation for log out
            logout(this.tokenForm).then ( res => {
                this.$message({message: 'Log out Sucess!',type: 'success'});
                sessionStorage.clear();
                this.$router.push('home')
            }).catch( error => {
                this.$message.error('Log out Failed');
            })
        },
        jumpManageproduct () {
            this.$router.push('/manageproduct')
        },
        jumpOrder () {
            this.$router.push('/manageorder')
        },
        jumpHome () {
        this.$router.push('/admin')
    },
  }
}
</script>

<style lang="less" scoped>
*{
    font-family: 'segUi';
}
#admin_container {
    background-color: #d1dbda;
    height: 100%;
}
.fix{
    width:1800px;
    margin:0 auto;
}
header {
    height: 100px;
    width: 1800px;
    margin: 0 auto;
}
header #logo {
    height: 50px;
    float: left;
    margin-top: 25px;
    margin-left:400px;
}
.button_position{
  float: right;
  margin-right:400px;
}
button {
    float: right;
    // border-radius: 4px;
    padding: 2px 15px;
    margin-left: 16px;
    margin-top: 35px;
    // border-color: grey;
    // color: grey;
    height: 30px;
    border-radius: 10px;
    border-color: #786662;
    background-color: #e7eae8;
    cursor: pointer;
}
main {
    width: 1000px;
    margin: 0 auto;
}
main #logo {
    width: 800px;
    margin-left: 100px;
    margin-top: 0px;
}
footer{
    position: relative;
    left:50%;
    transform: translate(-50%);
    height:375px;
    width:100%;
    background:#2f2a29;
    margin-top:20px;
    bottom:0%;
    img{
          height:375px;
          width:1800px;
          margin:0 auto;
          display:block;
    }
}
</style>