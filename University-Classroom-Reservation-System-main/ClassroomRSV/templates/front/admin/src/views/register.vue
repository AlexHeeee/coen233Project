<template>
  <div>
        <div class="container">
      <div class="login-form">
        <h1 class="h1">Sign Up</h1>
		<el-form ref="rgsForm" class="rgs-form" :model="rgsForm">
			<el-form-item label="username" class="input" v-if="tableName=='xuesheng'">
			  <el-input v-model="ruleForm.yonghuzhanghao" autocomplete="off" placeholder="username"  />
			</el-form-item>

			<el-form-item label="name" class="input" v-if="tableName=='xuesheng'">
			  <el-input v-model="ruleForm.xingming" autocomplete="off" placeholder="name"  />
			</el-form-item>

			<el-form-item label="password" class="input" v-if="tableName=='xuesheng'">
			  <el-input v-model="ruleForm.mima" autocomplete="off" placeholder="password" type="password"#elsetype="text" />
			</el-form-item>
			<div style="display: flex;flex-wrap: wrap;width: 100%;justify-content: center;">
				<el-button class="btn" type="primary" @click="login()">sign up</el-button>
				<el-button class="btn close" type="primary" @click="close()">cancel</el-button>
			</div>
		</el-form>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      ruleForm: {
      },
      tableName:"",
      rules: {},
    };
  },
  mounted(){
    let table = this.$storage.get("loginTable");
    this.tableName = table;
      },
  created() {
    
  },
  methods: {
    // 获取uuid
    getUUID () {
      return new Date().getTime();
    },
    close(){
	this.$router.push({ path: "/login" });
    },
    // 注册
    login() {
	var url=this.tableName+"/register";
      if((!this.ruleForm.yonghuzhanghao) && `jiaoshi` == this.tableName){
        this.$message.error(`username can't be null`);
        return
      }
      if((!this.ruleForm.yonghuzhanghao) && `xuesheng` == this.tableName){
        this.$message.error(`username can't be null`);
        return
      }
      this.$http({
        url: url,
        method: "post",
        data:this.ruleForm
      }).then(({ data }) => {
        if (data && data.code === 0) {
          this.$message({
            message: "sign up successfully",
            type: "success",
            duration: 1500,
            onClose: () => {
              this.$router.replace({ path: "/login" });
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
	.el-radio__input.is-checked .el-radio__inner {
		border-color: #00c292;
		background: #00c292;
	}

	.el-radio__input.is-checked .el-radio__inner {
		border-color: #00c292;
		background: #00c292;
	}

	.el-radio__input.is-checked .el-radio__inner {
		border-color: #00c292;
		background: #00c292;
	}

	.el-radio__input.is-checked+.el-radio__label {
		color: #00c292;
	}

	.el-radio__input.is-checked+.el-radio__label {
		color: #00c292;
	}

	.el-radio__input.is-checked+.el-radio__label {
		color: #00c292;
	}

	.h1 {
		margin-top: 10px;
	}

	body {
		padding: 0;
		margin: 0;
	}
	.nk-navigation {
		margin-top: 15px;

		a {
			display: inline-block;
			color: #fff;
			background: rgba(255, 255, 255, .2);
			width: 100px;
			height: 50px;
			border-radius: 30px;
			text-align: center;
			display: flex;
			align-items: center;
			margin: 0 auto;
			justify-content: center;
			padding: 0 20px;
		}

		.icon {
			margin-left: 10px;
			width: 30px;
			height: 30px;
		}
	}

	.register-container {
		margin-top: 10px;

		a {
			display: inline-block;
			color: #fff;
			max-width: 500px;
			height: 50px;
			border-radius: 30px;
			text-align: center;
			display: flex;
			align-items: center;
			margin: 0 auto;
			justify-content: center;
			padding: 0 20px;

			div {
				margin-left: 10px;
			}
		}
	}

	.container {
		height: 100vh;
		background-position: center center;
		background-size: cover;
		background-repeat: no-repeat;
    				background-image: url(https://uniconexed.org/wp-content/uploads/2022/02/Santa-Clara-University.jpg);
		    
		.login-form {
			right: 50%;
			top: 50%;
			transform: translate3d(50%, -50%, 0);
			border-radius: 10px;
			background-color: rgba(255,255,255,.5);
			font-size: 14px;
			font-weight: 500;
      box-sizing: border-box;

			width: 360px;
			height: auto;
			padding: 15px;
			margin: 0 auto;
			border-radius: 20px;
			border-width: 0;
			border-style: solid;
			border-color: rgba(255,0,0,0);
			background-color: rgba(255,255,255,.5);
			box-shadow: 0 0 6px rgba(255,0,0,.1);

			.h1 {
				width: 100%;
				height: auto;
				line-height: auto;
				color: #000;
				font-size: 26px;
				padding: 0;
				margin: 0 auto;
				border-radius: 0;
				border-width: 0;
				border-style: solid;
				border-color: rgba(255,0,0,0);
				background-color: rgba(255,0,0,0);
				box-shadow: 0 0 6px rgba(255,0,0,0);
				text-align: center;
			}

			.rgs-form {
				display: flex;
				flex-direction: column;
				justify-content: center;
				align-items: center;

        .el-form-item {
          width: 100%;
          display: flex;

          & /deep/ .el-form-item__content {
            flex: 1;
            display: flex;
          }
        }

				.input {
          width: 100%;
          height:auto;
          padding: 0;
          margin: 0 0 12px 0;
          border-radius: 0;
          border-width: 0;
          border-style: solid;
          border-color: rgba(255,0,0,0);
          background-color: rgba(255,0,0,0);
          box-shadow: 0 0 6px rgba(255,0,0,0);

					& /deep/ .el-form-item__label {
            width: 80px;
            line-height:44px;
            color: rgba(238, 141, 7, 1);
            font-size: rgba(255, 0, 0, 1);
            padding: 0 10px 0 0;
            margin: 0;
            border-radius: 0;
            border-width: 0;
            border-style: solid;
            border-color: rgba(255,0,0,0);
            background-color: rgba(255,0,0,0);
            box-shadow: 0 0 6px rgba(255,0,0,0);
					}

					& /deep/ .el-input__inner {
            width: 100%;
            height: 40px;
            line-height:40px;
            color: rgba(0, 0, 0, 1);
            font-size: 14px;
            padding: 0 12px;
            margin: 0;
            border-radius: 20px;
            border-width: 1px;
            border-style: solid;
            border-color: rgba(0, 0, 0, 1);
            background-color: rgba(248, 241, 241, 0.18);
            box-shadow: 0 0 6px rgba(255,0,0,0);
            text-align: left;
					}
				}

        .send-code {
          & /deep/ .el-input__inner {
            width: 100%;
            height: 44px;
            line-height:44px;
            color: #606266;
            font-size: 14px;
            padding: 0 12px;
            margin: 0;
            border-radius: 0;
            border-width: 1;
            border-style: solid;
            border-color: #606266;
            background-color: #fff;
            box-shadow: 0 0 6px rgba(255,0,0,0);
            text-align: left;
          }

          .register-code {
            margin: 0;
            padding: 0;
            width: 86px;
            height: 44px;
            line-height:44px;
            color: #fff;
            font-size: 14px;
            border-width: 0;
            border-style: solid;
            border-color: rgba(255,0,0,0);
            border-radius: 0;
            background-color: rgb(64, 158, 255);
            box-shadow: 0 0 6px rgba(255,0,0,0);
          }
        }

				.btn {
					margin: 0 10px;
          padding: 0;
					width: 88px;
					height: 44px;
          line-height:44px;
					color: rgba(255, 255, 255, 1);
					font-size: 14px;
					border-width: 1px;
					border-style: solid;
					border-color: rgba(64, 158, 255, 1);
					border-radius: 20px;
					background-color: rgba(84, 221, 231, 1);
          box-shadow: 0 0 6px rgba(255,0,0,0);
				}

				.close {
          margin: 0 10px;
          padding: 0;
          width: 88px;
          height: 44px;
          line-height:44px;
          color: rgba(255, 255, 255, 1);
          font-size: 14px;
          border-width: 1px;
          border-style: solid;
          border-color: #409EFF;
          border-radius: 21px;
          background-color: rgba(84, 221, 231, 1);
          box-shadow: 0 0 6px rgba(255,0,0,0);
				}

			}
		}
	}
</style>
