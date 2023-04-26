<!--Home Mod For Home Main Page   -->

<template>
  <div class="home-pro">
    <div class="img" v-for="fit in fits" :key="fit" @click="goProduct">
    <span class="demonstration" >{{ fit }}</span>
        <el-image
        style="width: 250px; height: 250px"
        :src="proPic"
        :fit="fit" @click="goProduct"><div slot="error" > <div slot="placeholder" style="background:rgb(243, 243, 243);height:250px">
        <div style="background:rgb(243, 243, 243);height:250px"><div style="padding-top:45%; padding-left:42%; ">Failed</div></div>
      </div></div></el-image>
    </div>
    <p @click="goProduct"> {{proName}}</p>
    <p @click="goProduct"> <span>${{proPrice}}</span></p>
  </div>
</template>

<script>
export default {
    props: ['index', 'proName', 'proDescription', 'proSales_data', 'proPrice', 'proPic','proId'],
    methods: {
    },
    data(){
        return {
            fits: [''],
    }
    },
    methods: {
      // Go to corresponding product page
      goProduct () {
        sessionStorage.setItem('product',this.proId);
        this.$router.push('/product');
        sessionStorage.setItem('fromHome', 1);
      }
    }
}
</script>

<style lang="less" scoped>
.home-pro {
    width: 300px;
    padding: 20px;
    border-radius: 5px;
    margin: 10px;
    font-family: 'segUi';
    word-break:break-all;
    border: 4px solid bisque;
    border-style:groove;
}
p {
    cursor: pointer;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-weight: 20px;
}
span{
    color:rgb(255, 115, 0);
    font-size: 20px ;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
.img{
    cursor: pointer;
    position: relative;
    left:9%;
}

</style>