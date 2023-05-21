const menu = {
    list() {
        return [{"backMenu":[{"child":[{"buttons":["add","check","update","delete","list"],"menu":"classroom","menuJump":"list","tableName":"jiaoshixinxi"}],"menu":"classroom"},
                {"child":[{"buttons":["add","check","update","delete"],"menu":"student","menuJump":"list","tableName":"xuesheng"}],"menu":"student"},
                {"child":[{"buttons":["add","check","update","delete","review","schedule"],"menu":"apply","menuJump":"list","tableName":"xueshengshenqing"}],"menu":"apply"},
                {"child":[{"buttons":["check","update","cancel"],"menu":"cancel","menuJump":"list","tableName":"xueshengquxiaoyuyue"}],"menu":"cancel"}],
            "frontMenu":[],"hasBackLogin":"yes","hasBackRegister":"no","hasFrontLogin":"no","hasFrontRegister":"no","roleName":"admin","tableName":"users"},
            {"backMenu":[{"child":[{"buttons":["check","student application","list"],"menu":"classroom","menuJump":"list","tableName":"jiaoshixinxi"}],"menu":"classroom"},
                    {"child":[{"buttons":["check","cancel"],"menu":"apply","menuJump":"list","tableName":"xueshengshenqing"}],"menu":"apply"},
                    {"child":[{"buttons":["check"],"menu":"cancel","menuJump":"list","tableName":"xueshengquxiaoyuyue"}],"menu":"cancel"}],
                "frontMenu":[],"hasBackLogin":"yes","hasBackRegister":"yes","hasFrontLogin":"no","hasFrontRegister":"no","roleName":"student","tableName":"xuesheng"}]
    }
}
export default menu;
