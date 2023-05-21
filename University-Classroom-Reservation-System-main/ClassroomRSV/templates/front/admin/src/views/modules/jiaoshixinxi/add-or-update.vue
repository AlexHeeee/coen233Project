<template>
  <div class="addEdit-block">
    <el-form
      class="detail-form-content"
      ref="ruleForm"
      :model="ruleForm"
      :rules="rules"
      label-width="80px"
	  :style="{backgroundColor:addEditForm.addEditBoxColor}"
    >
      <el-row>
      <el-col :span="12">
        <el-form-item class="input" v-if="type!='info'"  label="classroom number" prop="jiaoshibianhao">
          <el-input v-model="ruleForm.jiaoshibianhao" 
              placeholder="classroom number" clearable  :readonly="ro.jiaoshibianhao"></el-input>
        </el-form-item>
        <div v-else>
          <el-form-item class="input" label="classroom number" prop="jiaoshibianhao">
              <el-input v-model="ruleForm.jiaoshibianhao" 
                placeholder="classroom number" readonly></el-input>
          </el-form-item>
        </div>
      </el-col>
      <el-col :span="12">
        <el-form-item class="input" v-if="type!='info'"  label="seats" prop="rongnarenshu">
          <el-input v-model="ruleForm.rongnarenshu" 
              placeholder="seats" clearable  :readonly="ro.rongnarenshu"></el-input>
        </el-form-item>
        <div v-else>
          <el-form-item class="input" label="seats" prop="rongnarenshu">
              <el-input v-model="ruleForm.rongnarenshu" 
                placeholder="seats" readonly></el-input>
          </el-form-item>
        </div>
      </el-col>
      <el-col :span="12">
        <el-form-item class="select" v-if="type!='info'"  label="classroom status" prop="jiaoshizhuangtai">
          <el-select :disabled="ro.jiaoshizhuangtai" v-model="ruleForm.jiaoshizhuangtai" placeholder="please choose classroom status">
            <el-option
                v-for="(item,index) in jiaoshizhuangtaiOptions"
                v-bind:key="index"
                :label="item"
                :value="item">
            </el-option>
          </el-select>
        </el-form-item>
        <div v-else>
          <el-form-item class="input" label="classroom status" prop="jiaoshizhuangtai">
	      <el-input v-model="ruleForm.jiaoshizhuangtai"
                placeholder="classroom status" readonly></el-input>
          </el-form-item>
        </div>
      </el-col>
      </el-row>
          <el-row>
            <el-col :span="24">
              <el-form-item class="textarea" v-if="type!='info'" label="classroom device" prop="jiaoshishebei">
                <el-input
                  style="min-width: 200px; max-width: 600px;"
                  type="textarea"
                  :rows="8"
                  placeholder="classroom device"
                  v-model="ruleForm.jiaoshishebei" >
                </el-input>
              </el-form-item>
              <div v-else>
                <el-form-item v-if="ruleForm.jiaoshishebei" label="classroom device" prop="jiaoshishebei">
                    <span>{{ruleForm.jiaoshishebei}}</span>
                </el-form-item>
              </div>
            </el-col>
          </el-row>
      <el-form-item class="btn">
        <el-button v-if="type!='info'" type="primary" class="btn-success" @click="onSubmit">commit</el-button>
        <el-button v-if="type!='info'" class="btn-close" @click="back()">cancel</el-button>
        <el-button v-if="type=='info'" class="btn-close" @click="back()">back</el-button>
      </el-form-item>
    </el-form>
    

  </div>
</template>
<script>

</script>
<style lang="scss">
.editor{
  height: 500px;
  
  & /deep/ .ql-container {
	  height: 310px;
  }
}
.amap-wrapper {
  width: 100%;
  height: 500px;
}
.search-box {
  position: absolute;
}
.addEdit-block {
	margin: -10px;
}
.detail-form-content {
	padding: 12px;
	background-color: transparent;
}
.btn .el-button {
  padding: 0;
}
</style>
