<template>
  <div>
        <div class="container loginIn">

      <div :class="2 == 1 ? 'left' : 2 == 2 ? 'left center' : 'left right'">
        <el-form class="login-form" label-position="left" :label-width="1 == 3 || 1 == 2 ? '30px': '0px'">
          <div class="title-container"><h3 class="title">Sign In</h3></div>
          <el-form-item :style='{"padding":"0","boxShadow":"0 0 6px rgba(0,0,0,0)","margin":"0 0 12px 0","borderColor":"rgba(0,0,0,0)","backgroundColor":"rgba(0,0,0,0)","borderRadius":"0","borderWidth":"0","width":"100%","borderStyle":"solid","height":"auto"}' :label="1 == 3 ? 'username' : ''" :class="'style'+1">
            <span v-if="1 != 3" class="svg-container" style="
			color:rgba(183, 131, 59, 1);
			line-height:30px;
			font-size:14px;
			width:30px;
			padding:0;
			margin:0;
			radius:0;
			border-width:0;
			border-style:solid;
			border-color:rgba(0,0,0,0);
			background-color:rgba(0,0,0,0);
			box-shadow:0 0 6px rgba(0,0,0,0);
			}"><svg-icon icon-class="user" /></span>
            <el-input placeholder="username" name="username" type="text" v-model="rulesForm.username" />
          </el-form-item>
          <el-form-item :style='{"padding":"0","boxShadow":"0 0 6px rgba(0,0,0,0)","margin":"0 0 12px 0","borderColor":"rgba(0,0,0,0)","backgroundColor":"rgba(0,0,0,0)","borderRadius":"0","borderWidth":"0","width":"100%","borderStyle":"solid","height":"auto"}' :label="1 == 3 ? 'password' : ''" :class="'style'+1">
            <span v-if="1 != 3" class="svg-container" style="color:rgba(183, 131, 59, 1);
			line-height:30px;
			font-size:14px;
			width:30px;
			padding:0;
			margin:0;
			radius:0;
			border-width:0;
			border-style:solid;
			border-color:rgba(0,0,0,0);
			background-color:rgba(0,0,0,0);
			box-shadow:0 0 6px rgba(0,0,0,0);"><svg-icon icon-class="password" /></span>
            <el-input placeholder="password" name="password" type="password" v-model="rulesForm.password" />
          </el-form-item>
         <el-form-item label="Role" prop="loginInRole" class="role" style="display: flex;align-items: center;">
            <el-radio
              v-for="item in menus"
	      v-if="item.hasBackLogin=='yes'"
              v-bind:key="item.roleName"
              v-model="rulesForm.role"
              :label="item.roleName"
            >{{item.roleName}}</el-radio>
          </el-form-item>
          <el-button type="primary" @click="login()" class="loginInBt">{{'1' == '1' ? 'login' : 'login'}}</el-button>
          <el-form-item class="setting">
            <div class="register" @click="register('xuesheng')">Students Sign Up</div>
          </el-form-item>
        </el-form>
      </div>

    </div>
  </div>
</template>
<script>

import menu from "@/utils/menu";

export default {
  data() {
    return {
      rulesForm: {
        username: "",
        password: "",
        role: "",
        code: '',
      },
      menus: [],
      tableName: "",
      codes: [{
        num: 1,
        color: '#000',
        rotate: '10deg',
        size: '16px'
      },{
        num: 2,
        color: '#000',
        rotate: '10deg',
        size: '16px'
      },{
        num: 3,
        color: '#000',
        rotate: '10deg',
        size: '16px'
      },{
        num: 4,
        color: '#000',
        rotate: '10deg',
        size: '16px'
      }],
    };
  },
  mounted() {
	let menus = menu.list();
	this.menus = menus;
	  },
  created() {
    this.getRandCode()
	
  },
  methods: {
    register(tableName){
      this.$storage.set("loginTable", tableName);
      this.$router.push({path:'/register'})
    },
    login() {
      let code = ''
      for(let i in this.codes) {
        code += this.codes[i].num
      }
      if (!this.rulesForm.username) {
         this.$message.error("Please input username");
        return;
      }
      if (!this.rulesForm.password) {
         this.$message.error("Please input password");
        return;
      }
      if (!this.rulesForm.role) {
         this.$message.error("Please choose your role");
        return;
      }
      let menus = this.menus;
      for (let i = 0; i < menus.length; i++) {
        if (menus[i].roleName == this.rulesForm.role) {
          this.tableName = menus[i].tableName;
        }
      }
      this.$http({
        url: `${this.tableName}/login?username=${this.rulesForm.username}&password=${this.rulesForm.password}`,
        method: "post"
      }).then(({ data }) => {
        if (data && data.code === 0) {
          this.$storage.set("Token", data.token);
          this.$storage.set("role", this.rulesForm.role);
          this.$storage.set("sessionTable", this.tableName);
          this.$storage.set("adminName", this.rulesForm.username);
          this.$router.replace({ path: "/index/" });
        } else {
          this.$message.error(data.msg);
        }
      });
    },
  }
};
</script>
<style lang="scss" scoped>
.loginIn {
  min-height: 100vh;
  position: relative;
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
      background-image: url(https://www.scu.edu/media/offices/umc/Fountain-01-1160x652.png);
    

  .loginInBt {
    width: 100%;
    height: 44px;
    line-height: 44px;
    margin: 0;
    padding: 0;
    color: rgba(47, 43, 43, 1);
    font-size: 16px;
    border-radius: 20px;
    border-width: 0;
    border-style: solid;
    border-color: rgba(64, 158, 255, 1);
    background-color: rgba(203, 185, 86, 1);
    box-shadow: 0 0 6px rgba(255,0,0,.1);
  }
  .register {
    width: 70%;
    height: 24px;
    line-height: 24px;
    margin: 10px 0 0 15%;
    padding: 0;
    color: rgba(153, 153, 153, 1);
    font-size: 12px;
    border-radius: 0;
    border-width: 0;
    border-style: solid;
    border-color: rgba(64, 158, 255, 1);
    background-color: rgba(255, 255, 255, 0);
    box-shadow: 0 0 6px rgba(255,0,0,0);
	cursor: pointer;
  }
  .reset {
    width: auto;
    height: 24px;
    line-height: 24px;
    margin: 0;
    padding: 0;
    color: rgba(153, 153, 153, 1);
    font-size: 12px;
    border-radius: 0;
    border-width: 0;
    border-style: solid;
    border-color: rgba(64, 158, 255, 1);
    background-color: rgba(255, 255, 255, 0);
    box-shadow: 0 0 6px rgba(255,0,0,0);
  }


  .left {
    position: absolute;
    left: 0;
    top: 0;
	box-sizing: border-box;
	width: 442px;
	height: auto;
	margin: 0;
	padding: 0 12px;
	border-radius: 0;
	border-width: 0;
	border-style: solid;
	border-color: rgba(0,0,0,.3);
	background-color: rgba(244, 244, 239, 0.95);
	box-shadow: 0 0 0px rgba(30, 144, 255, .8);

    .login-form {
      background-color: transparent;
      width: 100%;
      right: inherit;
      padding: 0;
      box-sizing: border-box;
      display: flex;
	  position: initial;
      justify-content: center;
      flex-direction: column;
    }

    .title-container {
      text-align: center;
      font-size: 24px;

      .title {
        width: 100%;
        height: auto;
        line-height: auto;
        margin: 16px auto;
        padding: 0;
        color: rgba(21, 21, 20, 1);
        font-size: 22px;
        border-radius: 0;
        border-width: 0;
        border-style: solid;
        border-color: rgba(0,0,0,.3);
        background-color: rgba(0,0,0,0);
        box-shadow: 0 0 6px rgba(0,0,0,0);
      }
    }

    .el-form-item {
      position: relative;

      & /deep/ .el-form-item__content {
        line-height: initial;
      }

	  & /deep/ .el-radio__label {
	    width: auto;
	    height: 14px;
	    line-height: 14px;
	    margin: 0;
	    padding: 0 0 0 10px;
	    color: rgba(19, 18, 18, 1);
	    font-size: 14px;
	    border-radius: 0;
	    border-width: 0;
	    border-style: solid;
	    border-color: rgba(255, 255, 255, 0);
	    background-color: rgba(255, 255, 255, 0);
	    box-shadow: 0 0 6px rgba(255,0,0,0);
	    text-align: left;
	  }
	  & /deep/ .el-radio.is-checked .el-radio__label {
	    width: auto;
	    height: 14px;
	    line-height: 14px;
	    margin: 0;
	    padding: 0 0 0 10px;
	    color: #00c292;
	    font-size: 14px;
	    border-radius: 0;
	    border-width: 0;
	    border-style: solid;
	    border-color: rgba(255, 255, 255, 0);
	    background-color: rgba(255, 255, 255, 0);
	    box-shadow: 0 0 6px rgba(255,0,0,0);
	    text-align: left;
	  }
	  & /deep/ .el-radio__inner {
	    width: 14px;
	    height: 14px;
	    margin: 0;
	    padding: 0;
	    border-radius: 100%;
	    border-width: 1px;
	    border-style: solid;
	    border-color: #dcdfe6;
	    background-color: rgba(255, 255, 255, 1);
	    box-shadow: 0 0 6px rgba(255,0,0,0);
	  }
	  & /deep/ .el-radio.is-checked .el-radio__inner {
	    width: 14px;
	    height: 14px;
	    margin: 0;
	    padding: 0;
	    border-radius: 100%;
	    border-width: 1px;
	    border-style: solid;
	    border-color: #00c292;
	    background-color: #00c292;
	    box-shadow: 0 0 6px rgba(255,0,0,0);
	  }

      .svg-container {
        padding: 6px 5px 6px 15px;
        color: #889aa4;
        vertical-align: middle;
        display: inline-block;
        position: absolute;
        left: 0;
        top: 0;
        z-index: 1;
        padding: 0;
        line-height: 40px;
        width: 30px;
        text-align: center;
      }

      .el-input {
        display: inline-block;
        // height: 40px;
        width: 100%;

        & /deep/ input {
          background: transparent;
          border: 0px;
          -webkit-appearance: none;
          padding: 0 15px 0 30px;
          color: #fff;
          height: 40px;

		  width: 100%;
		  height: 44px;
		  line-height: 44px;
		  margin: 0;
		  padding: 0 30px;
		  color: rgba(120, 118, 118, 1);
		  font-size: 16px;
		  border-radius: 20px;
		  border-width: 0;
		  border-style: solid;
		  border-color: rgba(0,0,0,0);
		  background-color: rgba(211, 204, 204, 0.26);
		  box-shadow: 0 0 6px rgba(255,0,0,0);
        }
      }

    }


  }

  .center {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate3d(-50%,-50%,0);
  }

  .right {
    position: absolute;
    left: inherit;
    right: 0;
    top: 0;
  }

  .code {
    .el-form-item__content {
      position: relative;

      .getCodeBt {
        position: absolute;
        right: 0;
        top: 0;
        line-height: 40px;
        width: 100px;
        background-color: rgba(51,51,51,0.4);
        color: #fff;
        text-align: center;
        border-radius: 0 4px 4px 0;
        height: 40px;
        overflow: hidden;

        height: 44px;
        line-height: 44px;
        border-radius: 0;
        border-width: 0;
        border-style: solid;
        border-color: rgba(64, 158, 255, 1);
        background-color: rgba(51, 51, 51, 0.4);
        box-shadow: 0 0 6px rgba(255,0,0,0);

        span {
          padding: 0 5px;
          display: inline-block;
          font-size: 16px;
          font-weight: 600;
        }
      }

      .el-input {
        & /deep/ input {
          padding: 0 130px 0 30px;
        }
      }
    }
  }

  .setting {
    & /deep/ .el-form-item__content {

      box-sizing: border-box;
      line-height: 32px;
      height: 32px;
      font-size: 14px;
      color: #999;
      margin: 0 !important;
	  display: flex;

      .register {

		text-align: center;
      }

      .reset {
        float: right;
        width: 50%;
        text-align: right;
      }
    }
  }

  .style2 {
    padding-left: 30px;

    .svg-container {
      left: -30px !important;
    }

    .el-input {
      & /deep/ input {
        padding: 0 15px !important;
      }
    }
  }

  .code.style2, .code.style3 {
    .el-input {
      & /deep/ input {
        padding: 0 115px 0 15px;
      }
    }
  }

  .style3 {
    & /deep/ .el-form-item__label {
      padding-right: 6px;
      height: 44px;
      line-height: 44px;
    }

    .el-input {
      & /deep/ input {
        padding: 0 15px !important;
      }
    }
  }
  
  & /deep/ .el-form-item__label {
	width: 30px;
	height: 30px;
	line-height: 30px;
	margin: 0;
	padding: 0;
	color: rgba(183, 131, 59, 1);
	font-size: 14px;
	border-radius: 0;
	border-width: 0;
	border-style: solid;
	border-color: rgba(0,0,0,0);
	background-color: rgba(0,0,0,0);
	box-shadow: 0 0 6px rgba(0,0,0,0);
  }

  .role {
    & /deep/ .el-form-item__label {
      width: 56px !important;
      height: 38px;
      line-height: 38px;
      margin: 0;
      padding: 0;
      color: rgba(183, 131, 59, 1);
      font-size: 14px;
      border-radius: 0;
      border-width: 0;
      border-style: solid;
      border-color: rgba(64, 158, 255, 1);
      background-color: rgba(255, 255, 255, 0);
      box-shadow: 0 0 6px rgba(255,0,0,0);
      text-align: left;
    }

    & /deep/ .el-radio {
      margin-right: 12px;
    }
  }
}
</style>
