<!--Cart Mod For Cart Main Page   -->

<template>
  <div class="my-cartpro">
    <div class="img" v-for="fit in fits" :key="fit" @click="goProduct">
     <span class="demonstration">{{ fit }}</span>
        <el-image
          style="width: 100px; height: 100px"
          :src="proPic"
          :fit="fit"><div slot="error" > <div slot="placeholder" style="background:rgb(243, 243, 243);height:100px">
        <div style="background:rgb(243, 243, 243);height:100px"><div style="padding-top:40%; padding-left:35%; font-size:30%; ">Failed</div></div>
      </div></div></el-image>
    </div>
    <p class="plink" @click="goProduct"> {{proName}}  </p> 
    <p> $ {{proPrice}}</p>
    <p> Quantity: {{qua}}</p>
    <el-button class="el-icon-minus" circle @click="subFn" type="white"></el-button>
    <el-button class="el-icon-plus" circle @click="addFn" type="white"></el-button>
    <el-button class="el-icon-close" circle @click="delFn" type="white"></el-button>
    <div class="line"></div>
  </div>
</template>

<script>
export default {
    data() {
      return{
          fits: [''],
      }
    },
    props: ['index', 'proName', 'proPrice', 'qua', 'proPic', 'proId'],
    methods: {
      addFn(){
        this.$emit("addQua", this.index)
      },
      subFn(){
        this.$emit("subQua", this.index)
      },
      delFn(){
        this.$emit("delPro", this.index)
      },
      // Go to corresponding product page
      goProduct () {
        sessionStorage.setItem('product',this.proId);
        this.$router.push('/product')
      }
    },

}
</script>


<style lang="less" scoped>
.my-cartpro {
    width: 475px;
    padding: 20px;
    border-radius: 5px;
    margin: 10px;
    font-family: 'segUi';
    word-break:break-all;
}
.img{
    cursor: pointer;
    float: right;
    margin-right:-10px;
}
.plink {
    cursor: pointer;
    width:340px;
}
p{
    letter-spacing: 1.5px;
    word-break: keep-all;
}
.line{
    margin-top: 20px;
    position: relative;
    left:-145px;
    width: 750px;
    height:2px;
    background-color: black;
  }
</style>