<!--OrderHistory Mod For OrderHistory Main Page   -->

<template>
  <div class="order_item" style="width:400px">
      <div class="block"></div>
      <p><span> Order Id:</span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{ordId}}</p>
      <p><span> Pay State:</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{payStat}}</p>
      <p><span> Order Date: </span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{orderDate}}</p>
      <el-dialog :title="order_id" :visible.sync="dialogFormVisible" class="editf" width="30%" append-to-body>
        <div class="item" v-for="item in items" :key="item.product_id">
        <div class="img" v-for="fit in fits" :key="fit" @click="goProduct(item)">
        <span class="demonstration">{{ fit }}</span>
          <el-image
            style="width: 100px; height: 100px"
            :src="item.picture"
            :fit="fit"><div slot="error" > <div slot="placeholder" style="background:rgb(243, 243, 243);height:400px">
        <div style="background:rgb(243, 243, 243);height:400px"><div style="padding-top:45%; padding-left:30%; ">Failed</div></div>
      </div></div></el-image>
        </div>
        <div class="item1">
        <p>{{item.name}} </p>
        <p>${{item.price}} </p>
        <p>Quantity: {{item.quantity}} </p>
        </div>
        <div class="line-in"></div>
        </div>
        <div class="item1">
        <p> Buyer Name: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{name}}</p>
        <p> Phone Number: &nbsp;&nbsp;&nbsp;{{phone_number}}</p>
        <p> Address: </p>
        <p> {{address_line}}</p>
        </div>
        <div class="block"></div>
        Order Date: {{orderDate}}
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Total Price: {{ordTotal}}
        <div slot="footer" class="dialog-footer">
            <el-button type="white" @click="dialogFormVisible = false" icon="el-icon-error">Close</el-button>
        </div>
      </el-dialog>
      <div>
        <el-image v-for="(item,index) in shows" :key="index"
            style="width: 100px; height: 100px; margin-right:10px"
            :src="item.picture"
            :fit="fit"><div slot="error" > <div slot="placeholder" style="background:rgb(243, 243, 243);height:100px">
        <div style="background:rgb(243, 243, 243);height:100px"><div style="padding-top:40%; padding-left:35%; font-size:30%; ">Failed</div></div>
      </div></div></el-image>
      </div>
      <el-button type="white" @click="orderFn" class="detail" icon="el-icon-reading">Detail</el-button>
      <el-button type="white" @click="orderShare" class="detail" icon="el-icon-message">Share</el-button>
      <el-dialog title="Share Order" :visible.sync="sharedialogFormVisible" class="editf"  width="25%" append-to-body>
      <el-form :model="shareForm" ref="share_FormRef" :rules="shareRules">
        <el-form-item label="Receiver Name" prop="receiver_name">
          <el-input v-model="shareForm.receiver_name" autocomplete="off" ></el-input>
        </el-form-item>
        <el-form-item label="Email" prop="to_email">
          <el-input v-model="shareForm.to_email" autocomplete="off" ></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button type="white" @click="resetShare" icon="el-icon-error">Cancel</el-button>
        <el-button type="white" @click="submit" icon="el-icon-success">Confim</el-button>
      </div>
      </el-dialog>
      <div class="block"></div>
      <div class="line-top"></div>
  </div>
</template>

<script>
import { ord_share } from '../../api/order'
import { ord_sin_view } from '../../api/order'
export default {
    props: ['index', 'ordId', 'payStat', 'ordItem','ordTotal','orderDate','name','address_line','phone_number'],
    data () {
      // The rules for input value
      var checkEmail = (rule, value, callback) => {
        const mailReg = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+\.com/
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
          return callback(new Error('Username cannot be empty'));
        } else {
          callback()
        }
      }
        return {
            fits: [''],
            dialogFormVisible: false,
            sharedialogFormVisible: false,
            order_id: '###',
            viewForm: {
              token: "",
              order_id: ""
            },
            shareForm: {
              token: "",
              order_id: "",
              to_email: "",
              receiver_name: ""
            },
            shareRules: {
            to_email: [
              { validator: checkEmail, trigger: 'blur' }
            ],
            receiver_name:[
              { validator: checkUsername, trigger: 'blur'}
            ]
            },
            items: [],
            shows: []
        }
    },
    created () {
        this.$emit('checker',this.index);
        this.order_id =  "Order Number: " + this.ordId.toString();
        this.getPro();
    },
    methods: {
        // Show picture for three product of order
        async getPro() {
          this.viewForm.token = sessionStorage.getItem('token');
          this.viewForm.order_id = this.ordId;
          ord_sin_view(this.viewForm).then( res => {
              this.items = res.data.item;
              this.shows = this.items.slice(0, 3);
          }).catch( error => {
              this.$message.error('Failed');
          })
        },
        
        orderFn() {
            // If pay stat is "Fail"
            if (this.payStat === "Fail") {
                // page will redirect to payment page
                this.$router.push('/payment');
                // keep order information
                sessionStorage.setItem('order', this.ordId);
            } else {
                this.dialogFormVisible = true
            }
        },
        orderShare() {
            this.sharedialogFormVisible = true
        },
        closeDialog(){
            this.$refs['share_FormRef'].resetFields();
        },
        // Reset share form
        resetShare () {
          this.shareForm.to_email = "";
          this.shareForm.receiver_name = "";
          this.sharedialogFormVisible = false;
        },
        // Share corresponding order
        submit () {
          this.$refs.share_FormRef.validate(async (valid) => {
          if (valid) {
            this.shareForm.order_id = this.ordId;
            this.shareForm.token = sessionStorage.getItem('token');
            // Main operation to share order
            ord_share(this.shareForm).then ( res => {
            this.$message({message: 'Share Sucess!',type: 'success'});
                this.sharedialogFormVisible = false;
                this.shareForm.to_email = "";
                this.shareForm.receiver_name = "";
            }).catch( error => {
                this.$message.error('Share Failed');
            })
          }
          else {
            // user cannot submit if input did not pass the rules
            return false;
          }
          })
        },
        // Go to corresponding product page
        goProduct (item) {
          sessionStorage.setItem('product',item.product_id);
          this.$router.push('/product')
      }
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
span{
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size:17px;
}
p{
    font-family: 'segUi';
    word-break: keep-all;
}
</style>
