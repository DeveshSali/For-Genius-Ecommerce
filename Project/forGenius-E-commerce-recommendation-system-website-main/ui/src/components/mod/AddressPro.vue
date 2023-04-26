<!--Address Mod For Address Main Page   -->

<template>
  <div class="my-address">
  <el-descriptions title="Address Detail" :column="2" border>
    <el-descriptions-item label="Name" label-class-name="table-label" content-class-name="table-content">{{userName}}</el-descriptions-item>
    <el-descriptions-item label="Phone Number" label-class-name="table-label" content-class-name="table-content">{{phoneNumber}}</el-descriptions-item>
    <el-descriptions-item label="Country" label-class-name="table-label" content-class-name="table-content">{{country}}</el-descriptions-item>
    <el-descriptions-item label="State" label-class-name="table-label" content-class-name="table-content">{{state}}</el-descriptions-item>
    <el-descriptions-item label="Suburb" label-class-name="table-label" content-class-name="table-content">{{suburb}}</el-descriptions-item>
    <el-descriptions-item label="Postal Code" label-class-name="table-label" content-class-name="table-content">{{post_code}}</el-descriptions-item>
    <el-descriptions-item label="Address" label-class-name="table-label" >{{addressDe}}</el-descriptions-item>
  </el-descriptions>
    <el-button type="white" icon="el-icon-delete" @click="delFn" style="float:right; margin-top:20px">Delete</el-button>
    <el-button type="white" icon="el-icon-edit" @click="dialogFormVisible = true" style="float:right; margin-top:20px">Edit</el-button>
    <div style="clear:both"></div>
    <!-- Edit Form with dialog -->
    <el-dialog title="Address Book" :visible.sync="dialogFormVisible" @close="closeDialog" class="editf" width="30%" append-to-body>
      <el-form :model="editForm" ref="edit_FormRef" :rules="editRules">
           <el-form-item label="NAME" class="username_change" prop="name">
            <el-input v-model="editForm.name" autocomplete="off">
            </el-input>
          </el-form-item>
          <el-form-item label="PHONE NUMBER" class="username_change" prop="phone_number">
            <el-input v-model="editForm.phone_number" autocomplete="off">
            </el-input>
          </el-form-item>
           <el-form-item label="COUNTRY" class="username_change" prop="country">
            <el-input v-model="editForm.country" autocomplete="off">
            </el-input>
          </el-form-item>
          <el-form-item label="STATE" class="username_change" prop="state">
            <el-input v-model="editForm.state" autocomplete="off">
            </el-input>
          </el-form-item>
          <el-form-item label="SUBURB" class="username_change" prop="suburb">
            <el-input v-model="editForm.suburb" autocomplete="off">
            </el-input>
          </el-form-item>
          <el-form-item label="POSTAL CODE" class="username_change" prop="post_code">
            <el-input v-model="editForm.post_code" autocomplete="off">
            </el-input>
          </el-form-item>
          <el-form-item label="ADDRESS" class="username_change" prop="address_line">
            <el-input v-model="editForm.address_line" autocomplete="off">
            </el-input>
          </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button type="white" @click="dialogFormVisible = false" icon="el-icon-circle-close">Cancel</el-button>
        <el-button type="white" @click="submitEdit" icon="el-icon-circle-check">Confim</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import { address_edit } from '../../api/user'
export default {
    inject:['reload'],
    props: ['index', 'userName', 'addressId', 'addressDe', 'phoneNumber', 'suburb', 'post_code', 'state', 'country'],
    data () {
    // The rules for input data validation
          var checkName = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('username cannot be empty'))
      } else {
        callback()
      }
    }
    var checkAddress = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('address cannot be empty'))
      } else {
        callback()
      }
    }
    var checkPhone = (rule, value, callback) => {
      const mailReg = /^\d+$/
      setTimeout(() => {
        if (mailReg.test(value)) {
          callback()
        } else {
          callback(new Error('Phonenumber should be number'))
        }
      }, 100)
    }
    var checkState = (rule, value, callback) => {
      const mailReg = /^[A-Za-z]+$/
      if (!value) {
        return callback(new Error('State cannot be empty'))
      }
      setTimeout(() => {
        if (mailReg.test(value)) {
          callback()
        } else {
          callback(new Error('State should all be letters'))
        }
      }, 100)
    }
    var checkSuburb = (rule, value, callback) => {
      const mailReg = /^[A-Za-z]+$/
      if (!value) {
        return callback(new Error('Suburb cannot be empty'))
      }
      setTimeout(() => {
        if (mailReg.test(value)) {
          callback()
        } else {
          callback(new Error('Suburb should all be letters'))
        }
      }, 100)
    }
    var checkCountry = (rule, value, callback) => {
      const mailReg = /^[A-Za-z]+$/
      if (!value) {
        return callback(new Error('Country cannot be empty'))
      }
      setTimeout(() => {
        if (mailReg.test(value)) {
          callback()
        } else {
          callback(new Error('Country should all be letters'))
        }
      }, 100)
    }
    var checkCode = (rule, value, callback) => {
      const mailReg = /^\d+$/
      setTimeout(() => {
        if (mailReg.test(value)) {
          callback()
        } else {
          callback(new Error('Postal code should be number'))
        }
      }, 100)
    }
      return {
        dialogFormVisible: false,
        editForm: {
          token: '',
          address_id: this.addressId,
          address_line: this.addressDe,
          country: this.country,
          name: this.userName,
          phone_number: this.phoneNumber,
          post_code: this.post_code,
          state: this.state,
          suburb: this.suburb
        },
      //Input data validation
      editRules: {        
        name: [
          { validator: checkName, trigger: 'blur' }
        ],        
        address_line: [
          { validator: checkAddress, trigger: 'blur' }
        ],
        phone_number: [
          { validator: checkPhone, trigger: 'blur'  }
        ],
        post_code: [
          { validator: checkCode, trigger: 'blur'  }
        ],
        suburb: [
          { validator: checkSuburb, trigger: 'blur'  }
        ],
        state: [
          { validator: checkState, trigger: 'blur'  }
        ],
        country: [
          { validator: checkCountry, trigger: 'blur'  }
        ]
       }    
      }
    },
    watch: {
      userName:function(newVal,oldVal){
        this.userName = newVal;
      },
      addressDe:function(newVal,oldVal){
        this.addressDe = newVal;
      },
      phoneNumber:function(newVal,oldVal){
        this.phoneNumber = newVal;
      },
      addressId:function(newVal,oldVal){
        this.addressId = newVal;
      }
    },
    methods: {
      delFn(){
        this.$emit("delAdd", this.index)
      },
      editFn(){
        this.$emit("editAdd", this.index)
      },
      closeDialog(){
        this.$refs['edit_FormRef'].resetFields();
      },
      // submit editted address
      submitEdit() {  
        this.$refs.edit_FormRef.validate(async (valid) =>{
        if(valid){
          this.editForm.token = sessionStorage.getItem('token');
          this.editForm.phone_number = this.editForm.phone_number.toString();
          // Main operation for edit
          address_edit(this.editForm).then( res => {
              this.$message({message: 'Edit Sucess!',type: 'success'});
              this.dialogFormVisible = false;
              this.reload();
          }).catch( error => {
              this.$message.error('Edit Failed');
          })
          }
        else{
          // user cannot submit if input did not pass the rules
          return false;
        }
    })
}}}
</script>

<style lang="less" scoped>
.my-address {
    width: 700px;
    padding: 30px;
    border-radius: 30px;
    margin-top: 30px;
    word-break:break-all;
    background-color:#e7eae8;
}
.editf{
    position: fixed;
}
span{
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size:17px;
}

</style>
