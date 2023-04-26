<!--OrderHistory Mod For Order Admin Page   -->

<template>
  <div class="order_item" style="width:400px">
      <div class="block"></div>
      <p><span> User:</span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{email}}</p>
      <p><span> Order Id:</span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{ordId}}</p>
      <p><span> Pay State:</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{payStat}}</p>
      <p><span> Order Date: </span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{orderDate}}</p>
      <el-dialog :title="order_id" :visible.sync="dialogFormVisible" class="editf" width="800px" append-to-body>
        <h2><span> User: </span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{email}}</h2>
        <div class="line-in"></div>
        <div class="item" v-for="item in ordItem" :key="item.product_id">
        
        <span class="demonstration">{{ fit }}</span>
          <el-image
            style="width: 100px; height: 100px"
            :src="item.picture"
            :fit="fit"><div slot="error" > <div slot="placeholder" style="background:rgb(243, 243, 243);height:400px">
        <div style="background:rgb(243, 243, 243);height:400px"><div style="padding-top:40%; padding-left:30%; ">Failed</div></div>
      </div></div></el-image>
        <div class="inf">
        <p>{{item.name}} </p>
        <p>${{item.price}} </p>
        <p>Quantity: {{item.quantity}} </p>
        </div>
        <div class="line-in"></div>
        </div>
        <div class="item1">
         <el-descriptions title="Address Detail" :column="2" border>
          <el-descriptions-item label="Name" label-class-name="table-label" content-class-name="table-content">{{name}}</el-descriptions-item>
          <el-descriptions-item label="Phone Number" label-class-name="table-label" content-class-name="table-content">{{phone_number}}</el-descriptions-item>
          <el-descriptions-item label="Country" label-class-name="table-label" content-class-name="table-content">{{country}}</el-descriptions-item>
          <el-descriptions-item label="State" label-class-name="table-label" content-class-name="table-content">{{state}}</el-descriptions-item>
          <el-descriptions-item label="Suburb" label-class-name="table-label" content-class-name="table-content">{{suburb}}</el-descriptions-item>
          <el-descriptions-item label="Postal Code" label-class-name="table-label" content-class-name="table-content">{{post_code}}</el-descriptions-item>
          <el-descriptions-item label="Address" label-class-name="table-label" >{{address_line}}</el-descriptions-item>
        </el-descriptions>
        </div>
        <div class="block"></div>
        Order Date: {{orderDate}}
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Total Price: {{ordTotal}}
        <div slot="footer" class="dialog-footer">
            <el-button type="white" @click="dialogFormVisible = false" icon="el-icon-error">Close</el-button>
        </div>
      </el-dialog>
      <el-button type="white" @click="dialogFormVisible = true" class="detail" icon="el-icon-reading">Detail</el-button>
      <div class="block"></div>
      <div class="line-top"></div>
  </div>
</template>

<script>
export default {
    props: ['index', 'ordId', 'payStat', 'ordItem','ordTotal','orderDate','name','address_line','phone_number', 'email', 'suburb', 'post_code', 'state', 'country'],
    data () {
        return {
            dialogFormVisible: false,
        }
    },
    created () {
        this.$emit('checker',this.index);
        this.order_id =  "Order Number: " + this.ordId.toString();
    },
    methods: {
        
    }
}
</script>

<style lang="less" scoped>
.line-top {
    position: relative;
    width: 300%;
    height: 1px;
    left:40%;
    transform: translate(-50%);
    border-top: solid #0b0b0f 1px;
}
.line-in {  
    margin-top:35px;
    width: 100%;
    height: 1px;
    border-top: solid #0b0b0f 1px;
}
.block {
    height: 20px;
}
.detail{
    position: relative;
    left:80%;

}
.editf{
    position: fixed;
} 
.img{
    cursor: pointer;
    float:right;
    margin-right:20px;
    margin-top:-5px;
}
.item1{
    letter-spacing: 1.5px;
}
.inf{
    letter-spacing: 1.5px;
    width:500px;
    float:left;
    word-break: keep-all;
}

span{
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size:17px;
}
p{
    font-family: 'segUi';
    word-break: keep-all;
}
</style>
