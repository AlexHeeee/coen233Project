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
        <el-form-item class="input" v-if="type!='info'"  label="username" prop="username">
          <el-input v-model="ruleForm.username" 
              placeholder="username" clearable  :readonly="ro.username"></el-input>
        </el-form-item>
        <div v-else>
          <el-form-item class="input" label="username" prop="username">
              <el-input v-model="ruleForm.username" 
                placeholder="username" readonly></el-input>
          </el-form-item>
        </div>
      </el-col>
      <el-col :span="12">
        <el-form-item class="input" v-if="type!='info'"  label="password" prop="password">
          <el-input v-model="ruleForm.password" 
              placeholder="password" clearable  :readonly="ro.password"></el-input>
        </el-form-item>
        <div v-else>
          <el-form-item class="input" label="password" prop="password">
              <el-input v-model="ruleForm.password" 
                placeholder="password" readonly></el-input>
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
