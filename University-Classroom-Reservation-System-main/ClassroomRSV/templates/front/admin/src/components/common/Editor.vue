<template>
  <div>

    <quill-editor
      class="editor"
      v-model="value"
      ref="myQuillEditor"
      :options="editorOption"
      @blur="onEditorBlur($event)"
      @focus="onEditorFocus($event)"
      @change="onEditorChange($event)"
    ></quill-editor>
  </div>
</template>

<script>

import { quillEditor } from "vue-quill-editor";
import "quill/dist/quill.core.css";
import "quill/dist/quill.snow.css";
import "quill/dist/quill.bubble.css";
export default {
  props: {
    /*the content of editor*/
    value: {
      type: String
    },
    action: {
      type: String
    },
    maxSize: {
      type: Number,
      default: 4000 //kb
    }
  },

  components: {
    quillEditor
  },

  data() {
    return {
      content: this.value,
      quillUpdateImg: false,
      editorOption: {
        placeholder: "",
        theme: "snow", // or 'bubble'
        modules: {
          toolbar: {
            container: toolbarOptions,
            // container: "#toolbar",
            handlers: {
              image: function(value) {
                if (value) {
                  document.querySelector(".avatar-uploader input").click();
                } else {
                  this.quill.format("image", false);
                }
              }
            }
          }
        }
      },
      header: {
        // token: sessionStorage.token
       'Token': this.$storage.get("Token")
      }
    };
  },
  computed: {
    getActionUrl: function() {
      return `/${this.$base.name}/` + this.action;
    }
  },
  methods: {
    onEditorBlur() {
    },
    onEditorFocus() {
    },
    onEditorChange() {
      console.log(this.value);
      this.$emit("input", this.value);
    },
    beforeUpload() {
      this.quillUpdateImg = true;
    },

    uploadSuccess(res, file) {

      let quill = this.$refs.myQuillEditor.quill;
      if (res.code === 0) {
        let length = quill.getSelection().index;
        quill.insertEmbed(length, "image", this.$base.url+ "upload/" +res.file);
        quill.setSelection(length + 1);
      } else {
        this.$message.error("insert error");
      }
      this.quillUpdateImg = false;
    },
    uploadError() {
      this.quillUpdateImg = false;
      this.$message.error("insert error");
    }
  }
};
</script>
<style>
.editor {
  line-height: normal !important;
}

.ql-container {
	height: 400px;
}

.ql-snow .ql-picker.ql-size .ql-picker-label::before,
.ql-snow .ql-picker.ql-size .ql-picker-item::before {
  content: "14px";
}
.ql-snow .ql-picker.ql-size .ql-picker-label[data-value="small"]::before,
.ql-snow .ql-picker.ql-size .ql-picker-item[data-value="small"]::before {
  content: "10px";
}
.ql-snow .ql-picker.ql-size .ql-picker-label[data-value="large"]::before,
.ql-snow .ql-picker.ql-size .ql-picker-item[data-value="large"]::before {
  content: "18px";
}
.ql-snow .ql-picker.ql-size .ql-picker-label[data-value="huge"]::before,
.ql-snow .ql-picker.ql-size .ql-picker-item[data-value="huge"]::before {
  content: "32px";
}

</style>



