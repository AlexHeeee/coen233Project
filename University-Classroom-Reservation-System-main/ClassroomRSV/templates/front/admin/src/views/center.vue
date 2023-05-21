<template>
  <div>
    <el-form
      class="detail-form-content"
      ref="ruleForm"
      :model="ruleForm"
      label-width="80px"
	  style="background: transparent;"
    >  
     <el-row>

      <el-col :span="12">
        <el-form-item   v-if="flag=='xuesheng'"  label="username" prop="yonghuzhanghao">
          <el-input v-model="ruleForm.yonghuzhanghao" readonly              placeholder="username" clearable></el-input>
        </el-form-item>
      </el-col>
      <el-col :span="12">
        <el-form-item   v-if="flag=='xuesheng'"  label="name" prop="xingming">
          <el-input v-model="ruleForm.xingming"               placeholder="name" clearable></el-input>
        </el-form-item>
      </el-col>
      <el-col :span="12">
        <el-form-item v-if="flag=='xuesheng'"  label="gender" prop="xingbie">
          <el-select v-model="ruleForm.xingbie"  placeholder="Please choose gender">
            <el-option
                v-for="(item,index) in xueshengxingbieOptions"
                v-bind:key="index"
                :label="item"
                :value="item">
            </el-option>
          </el-select>
        </el-form-item>
      </el-col>
      <el-form-item v-if="flag=='users'" label="username" prop="username">
        <el-input v-model="ruleForm.username" 
        placeholder="username"></el-input>
      </el-form-item>
      <el-col :span="24">
      <el-form-item>
        <el-button type="primary" @click="onUpdateHandler">update</el-button>
      </el-form-item>
      </el-col>
      </el-row>
    </el-form>
  </div>
</template>
<script>


export default {
  data() {
    return {
      ruleForm: {},
      flag: '',
      usersFlag: false,
      xueshengxingbieOptions: [],
    };
  },
  mounted() {
    var table = this.$storage.get("sessionTable");
    this.flag = table;
    this.$http({
      url: `${this.$storage.get("sessionTable")}/session`,
      method: "get"
    }).then(({ data }) => {
      if (data && data.code === 0) {
        this.ruleForm = data.data;
      } else {
        this.$message.error(data.msg);
      }
    });
    this.xueshengxingbieOptions = "male,female".split(',')
  },
  methods: {
    onUpdateHandler() {

      if((!this.ruleForm.yonghuzhanghao)&& 'xuesheng'==this.flag){
        this.$message.error('username can not be null');
        return
      }
      if('users'==this.flag && this.ruleForm.username.trim().length<1) {
	this.$message.error(`username can not be null`);
        return	
      }
      this.$http({
        url: `${this.$storage.get("sessionTable")}/update`,
        method: "post",
        data: this.ruleForm
      }).then(({ data }) => {
        if (data && data.code === 0) {
          this.$message({
            message: "update successfully",
            type: "success",
            duration: 1500,
            onClose: () => {
            }
          });
        } else {
          this.$message.error(data.msg);
        }
      });
    }
  }
};
</script>
<style lang="scss" scoped>
</style>
